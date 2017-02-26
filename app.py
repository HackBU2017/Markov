from flask import Flask, render_template, request
import sys
import twitter
from Grabber import *
#from MakeMarkov import *

app = Flask(__name__)

def makeMarkov(twitter_handle):
    text = grabber(twitter_handle)
    text_model = markovify.Text(text)

    output = text_model.make_sentence()
    print(output, file=sys.stderr)
    return output

@app.route("/", methods=['GET', 'POST'])
def home():
    print(request.method, request.method == 'POST')
    if request.method == 'POST':
        tweet = makeMarkov(request.form['handle'])
        print("Tweet", tweet)
        return render_template('Markov.html', tweet=tweet, itried=True)
    else:
        return render_template('Markov.html')

if __name__ == "__main__":
    app.run(debug=True)
