from revChatGPT.V3 import Chatbot
from os import getenv
from threading import Thread
from uuid import uuid4
from func import okreturn, jsonerror

chatbot = Chatbot(api_key=getenv('CHATGPT_TOKEN'))

dic = {}


def get(uu):
    try:
        a = dic[uu]
        if (a['finish']):
            dic.pop(uu)
        return okreturn(a)
    except KeyError:
        return jsonerror('不存在的对话')


def th(q, uu):
    dic[uu] = {'ans': '', 'finish': False}
    for data in chatbot.ask(q):
        dic[uu]['ans'] += data
    dic[uu]['finish'] = True


def askq(q):
    uu = uuid4().hex
    t = Thread(target=th, kwargs={'q': q, 'uu': uu})
    t.start()
    return okreturn({'id': uu})
