from flask import Flask, request
from json import loads
from func import jsonerror
from chat import askq, get

app = Flask(__name__)
with open('index.html', encoding='UTF-8') as f:
    home_h = f.read()


@app.post('/ask/')
def ask():
    jsonq = request.get_data()
    if jsonq is None or jsonq == '':
        return jsonerror('空请求')
    try:
        q = loads(jsonq)['question']
    except:
        return jsonerror('json中没有`question`')
    else:
        return askq(q)


@app.post('/ans/')
def ans():
    jsonq = request.get_data()
    if jsonq is None or jsonq == '':
        return jsonerror('空请求')
    try:
        id = loads(jsonq)['id']
    except:
        return jsonerror('json中没有`id`')
    else:
        return get(id)

@app.get('/')
def home():
    return home_h
