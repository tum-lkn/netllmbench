import logging


class Framework:
    def __init__(self, interactor, emulator, tasks, statistics_collectors, max_task_attempts=3, master_llm=None):
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

        self.interactor = interactor
        self.emulator = emulator
        self.tasks = tasks
        self.statistics_collectors = statistics_collectors
        self.max_task_attempts = max_task_attempts  # This has to be 3 at the moment for the code to work.
        self.master_llm = master_llm

        self.emulator.deploy_lab()

    def answer_task(self, task_id, task):
        attempt = 0
        while attempt < self.max_task_attempts:
            hostname, cmd_to_be_executed = self.interactor.get_response(task)

            # If unable to parse the LLM output, ask for a correctly formatted response.
            if hostname is None:
                if not self.interactor.json_format_re_requested[task_id]:
                    task = (f'I cannot understand your command.'
                            f'Give your answer in JSON format. '
                            f'The keys are "machine" and "command". '
                            f'Do not include any other text in your answer. ')
                    self.interactor.iterations_to_solve_the_task[task_id] += 1
                    self.interactor.json_format_re_requested[task_id] = True
                    attempt += 1
                    continue

                if not self.interactor.json_format_provided[task_id]:
                    task = ('Give your answer in JSON format. '
                            'Correct format should look like: \'{"machine": "NAME", "command": "COMMAND"}\'. '
                            'Do not include any other text in your answer. ')
                    self.interactor.iterations_to_solve_the_task[task_id] += 1
                    self.interactor.json_format_provided[task_id] = True
                    attempt += 1
                    continue

                if not self.interactor.json_parsed_via_llama3[task_id]:

                    master_llm_hostname, master_llm_cmd = self.master_llm.try_to_get_proper_json(cmd_to_be_executed)

                    self.interactor.iterations_to_solve_the_task[task_id] += 1
                    self.interactor.json_parsed_via_llama3[task_id] = True

                    if master_llm_hostname is not None:
                        master_output = self.emulator.exec_command(master_llm_hostname, master_llm_cmd)
                        self.interactor.llama3_helped[task_id] = True

                        if not master_output:
                            self.interactor.final_answer[task_id] = True

                    attempt += 1
                    continue

            output = self.emulator.exec_command(hostname, cmd_to_be_executed)

            # if the output was successful
            if not output:
                self.interactor.iterations_to_solve_the_task[task_id] += 1
                self.interactor.final_answer[task_id] = True
                break
            # if output was unsuccessful
            else:
                try:
                    if 'ttl' in str(output[0][0]):
                        self.interactor.iterations_to_solve_the_task[task_id] += 1
                        self.interactor.final_answer[task_id] = True
                        break
                except:
                    pass
                try:
                    task = (f'I have the following error: {output[0][1].strip().decode("utf-8")}. Can you please try again? '
                            f'Give your answer in JSON format. The keys are "machine" and "command". '
                            f'Do not include any other text in your answer.')
                except:
                    task = (f'I have the following error: {output}. Can you please try again? '
                            f'Give your answer in JSON format. The keys are "machine" and "command". '
                            f'Do not include any other text in your answer.')

                self.interactor.iterations_to_solve_the_task[task_id] += 1

            attempt += 1

    def evaluate(self):
        for task_id, task in enumerate(self.tasks):
            self.logger.info(f"Executing task number {task_id+1}")
            self.interactor.iterations_to_solve_the_task[task_id+1] = 0
            self.interactor.json_format_re_requested[task_id+1] = False
            self.interactor.json_format_provided[task_id+1] = False
            self.interactor.json_parsed_via_llama3[task_id+1] = False
            self.interactor.llama3_helped[task_id+1] = False

            self.interactor.final_answer[task_id + 1] = False

            self.answer_task(task_id+1, task)

    def collect_statistics(self):
        for collector in self.statistics_collectors:
            collector.collect(self.interactor)

    def stop(self):
        self.emulator.undeploy_lab()

    def run(self):
        self.evaluate()
        self.stop()
        self.collect_statistics()

