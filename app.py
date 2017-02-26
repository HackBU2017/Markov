from flask import Flask, render_template, request
import sys
import twitter
api = twitter.Api(consumer_key='BQRfMJOhdiARaRBwlOpo78ktp',
      consumer_secret='RxF8PngRe44jVMQDUdunfTy9KLRCqbp9NKFYX3fuHFkx2MvsHX',
      access_token_key='2498510321-AC9ycNnMzoug1iniU544RvceQkRNQxOS25qdaTr',
      access_token_secret='5odRjLJdgntK0mffliAbIARphkqDyPrJ0UjqeUMI9bmo7')
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    sys.exit("This worked")
    print("Request coming in")
    if request.method == 'POST':
        print("data below")
        print(request.data)

    {"id": 16133, "location": "Philadelphia", "name": "bear"}

    t = api.GetUserTimeline(screen_name='incrubberduck')

    tweets = [i.AsDict() for i in t]
    for t in tweets:
        print (t['text'].encode("utf-8"))

    return render_template("Markov.html")

if __name__ == "__main__":
    app.run(debug=True)
