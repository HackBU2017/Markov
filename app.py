from flask import Flask, render_template, request
import sys
import twitter
from Grabber import *
from MakeMarkov import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        tweet = makeMarkov(request.form['handle'])
        return render_template('Markov.html', tweet=tweet, itried=True)
    else:
        return render_template('Markov.html')

if __name__ == "__main__":
    app.run(debug=True)
