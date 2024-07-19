from json import JSONDecodeError

import ollama
import json
import logging
import config
import ast


class LLMInteractor:
    def __init__(self, llm):
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

        self.llm = llm
        self.client = ollama.Client(host=llm.host)
        self.messages = list()
        self.response_statistics = list()

        self.iterations_to_solve_the_task = dict()
        self.json_format_re_requested = dict()
        self.json_format_provided = dict()
        self.json_parsed_via_llama3 = dict()
        self.llama3_helped = dict()
        self.final_answer = dict()

    def get_model_name(self):
        return str(self.llm.model_name)

    def get_response_statistics(self):
        return self.response_statistics

    def get_response(self, content):
        msg = {'role': 'user',
              'content': content
              }

        self.messages.append(msg)

        response = self.client.chat(model=self.llm.model_name, messages=self.messages)
        self.response_statistics.append(response)

        while response['message']['content'] == '':
            self.update_chat_history(''),
            msg = {'role': 'user',
                   'content': "Do not give an empty response!"
                   }
            self.messages.append(msg)
            response = self.client.chat(model=self.llm.model_name, messages=self.messages)
            self.response_statistics.append(response)

        try:
            reply = ast.literal_eval(response['message']['content'])
            self.update_chat_history(reply)
            return config.MAPPINGS[reply['machine']], reply['command']
        except:
            self.update_chat_history(response['message']['content'])
            return None, response['message']['content']

    def give_feedback(self, feedback):
        msg = {'role': 'user',
              'content': feedback
              }

        self.messages.append(msg)

        response = self.client.chat(model=self.llm.model_name, messages=self.messages)

        reply = response['message']['content']

        self.update_chat_history(reply)

    def update_chat_history(self, reply):
        self.messages.append({
            'role': 'system',
            'content': str(reply),
        })

    def get_chat_history(self):
        return self.messages

    def try_to_get_proper_json(self, input):

        msg = {'role': 'user',
              'content': f'Can you extract the machine and command in only JSON format from the following text: '
                         f'\"{input}\"'
                         f'The keys are "machine" and "command". You do not speak natural language. '
                         f'Do not include any other text than JSON in your answer. '
              }

        response = self.client.chat(model=self.llm.model_name, messages=[msg])

        try:
            reply = ast.literal_eval(response['message']['content'])
            return config.MAPPINGS[reply['machine']], reply['command']
        except:
            return None, None
