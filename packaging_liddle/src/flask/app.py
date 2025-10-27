import requests
from flask import Flask

app = Flask(__name__)

def get_w():
    x = requests.get('https://liddlegithub.github.io/')
    print(x.status_code)

@app.route('/')
def hello_world():
    get_w()
    print("ullo")
    return 'Hullo from Liddle Flask!'

@app.route('/about')
def about():
    return '(2025.10.28)Today we learn Flask'