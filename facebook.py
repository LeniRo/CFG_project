app_id = ""
app_secret = "fa6efcbe06cfcab606f67fd53cc21a29"
user_token = "EAACoU1HVs3sBABHVMVZAhKN59rGZAAxp5D2a3KXv8iTejYcp9rsNmEZCKWodxsmcHVKkaYUbKwL0vqT6TgVtMbB75ZAZAMgBWXfIDjLWjKGJOAlGJZBZAyqubZA6RlSqix9bWnrvcNJUxX0vhqcVbiebkawfRHX9Hj7itAOzdlhq2NzRoFLQV6MkGQyZAZC1rfjE0ZD"
app_token = "185075808711547|v8--zQKpzoJ2vH_XhOkt7Kvs0jg"



from facebook import get_user_from_cookie, GraphAPI
from flask import g, render_template, redirect, request, session, url_for

from app import app, db
from .models import User

# Facebook app details
FB_APP_ID = '185075808711547'
FB_APP_NAME = 'CFG_ER_app'
FB_APP_SECRET = 'fa6efcbe06cfcab606f67fd53cc21a29'


@app.route('/')
def index():
    # If a user was set in the get_current_user function before the request,
    # the user is logged in.
    if g.user:
        return render_template('findex.html', app_id=FB_APP_ID,
                               app_name=FB_APP_NAME, user=g.user)
    # Otherwise, a user is not logged in.
    return render_template('flogin.html', app_id=FB_APP_ID, name=FB_APP_NAME)