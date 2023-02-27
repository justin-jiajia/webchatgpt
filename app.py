from flask import Flask, request
from json import loads
from chat import askq

app = Flask(__name__)
with open('index.html', encoding='UTF-8') as f:
    home_h=f.read()

@app.post('/ask/')
def ask():
    jsonq = request.get_data()
    if jsonq is None or jsonq == '':
        return 'empty question', 400
    try:
        q=loads(jsonq)['question']
    except:
        return 'question not in json', 400
    else:
        try:
            return askq(q)
        except:
            return '出错了！请再试一次', 500
        else:
            pass

@app.get('/')
def home():
    return home_h
