from revChatGPT.V1 import Chatbot
from os import getenv

chatbot = Chatbot(config={
    'session_token': getenv('CHATGPT_TOKEN')
})

def askq(q):
    prev_text = ""
    for data in chatbot.ask(q):
        message = data["message"][len(prev_text) :]
        yield message
        prev_text = data["message"]
