import requests as r
from flask import Flask
from threading import Thread

app = Flask(__name__)


def aa():
  app.run(host="0.0.0.0")

def bb():
  while True:
    r.get('https://hdiahdisbn7383692649.onrender.com/')

ax = Thread(target=aa)
bx = Thread(target=bb)

ax.start()
bx.start()
