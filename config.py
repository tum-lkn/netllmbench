from collections import namedtuple

Model = namedtuple('Model', ['model_name', 'host'])

llama3_70b = Model(model_name='llama3:70b-instruct-q8_0', host='OLLAMA_SERVER_IP:11434')
llama3_8b = Model(model_name='llama3:8b-instruct-fp16', host='OLLAMA_SERVER_IP:11434')
mistral_7b = Model(model_name='mistral:7b-instruct-fp16', host='OLLAMA_SERVER_IP:11434')
gemma_7b = Model(model_name='gemma:7b-instruct-v1.1-fp16', host='OLLAMA_SERVER_IP:11434')
gemma_2b = Model(model_name='gemma:2b-instruct-v1.1-fp16', host='OLLAMA_SERVER_IP:11434')
qwen_4b = Model(model_name='qwen:4b-chat-v1.5-fp16', host='OLLAMA_SERVER_IP:11434')


MAPPINGS = {
    "R1": "router1",
    "S1": "switch1",
    "S2": "switch2",
    "H1": "host1",
    "H2": "host2",
    "H3": "host3"
}

