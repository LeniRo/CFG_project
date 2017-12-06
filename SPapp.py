import tweepy
import os

auth = tweepy.OAuthHandler('UjwtjLkQDn3fbmS1jN1Yhb99R', 'JfsDcBWAInOVbq1uJplEVpzFEVdhvY2pmpA7TLXZ5qZ9AXxlxg')
auth.set_access_token('790140278506217472-pgWkxH7Fynax6GMh0hfGfu2F9q9P0MF', 'IT6buN6Th1Khn5M8NxlFkRUd8QhXMQMkWjAgh0h0u8wQn')

api = tweepy.API(auth)

public_tweets = api.search(
    q = "shefcodefirst")



from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', tweets=public_tweets)


if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)
