from flask import Flask, escape, request
import lib.hello as lib

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "world!")
    lang = request.args.get("lang", "en")
    return f'{lib.hello(lang)}, {escape(name)}!'