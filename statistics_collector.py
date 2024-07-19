import logging
import csv


class ChatHistoryCollector:
    def __init__(self):
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def collect(self, interactor):
        self.logger.info("Collecting Chat History Statistics...")
        with open(f'/opt/project/statistics/ChatHistory-{interactor.get_model_name()}.csv', 'w') as f:
            header = ['role', 'content']
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            for row in interactor.get_chat_history():
                writer.writerow(row)


class LLMStatisticsCollector:
    def __init__(self):
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def collect(self, interactor):
        self.logger.info("Collecting LLM Statistics...")
        with open(f'/opt/project/statistics/LLMStatistics-{interactor.get_model_name()}.csv', 'w') as f:
            header = list(interactor.get_response_statistics()[1].keys())
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            for row in interactor.get_response_statistics():
                writer.writerow(row)


class FeedbackStatisticsCollector:

    def __init__(self):
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def collect(self, interactor):
        self.logger.info("Collecting Feedback Statistics...")

        collected_list = [interactor.iterations_to_solve_the_task, interactor.json_format_re_requested, interactor.json_format_provided, interactor.json_parsed_via_llama3, interactor.llama3_helped, interactor.final_answer]
        row_names = ['iterations_to_solve_the_task', 'json_format_re_requested', 'json_format_provided', 'json_parsed_via_llama3', 'llama3_helped', 'final_answer']

        with open(f'/opt/project/statistics/FeedbackStatistics-{interactor.get_model_name()}.csv', 'w') as f:
            header = ['name'] + list(interactor.iterations_to_solve_the_task.keys())
            writer = csv.writer(f)
            writer.writerow(header)

            for idx, d in enumerate(collected_list):
                row = [row_names[idx]] + [value for key, value in d.items()]
                writer.writerow(row)
