from flask import Flask, render_template, request
import sys
import twitter
from Grabber import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    grabber()
    return render_template('Markov.html')

if __name__ == "__main__":
    app.run()
