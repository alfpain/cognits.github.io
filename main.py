"""`main` is the top level module for your Flask application."""

from google.appengine.api import mail

# Import the Flask Framework
from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
app = Flask(__name__)

app.debug = False
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
params = {'app_name': 'Cognits'}

EMAIL = "s@cognits.co"

def send_mail(sender_address, user_address, subject, body):
    mail.send_mail(sender_address, user_address, subject, body)


@app.route('/', methods=['GET', 'POST'])
def hello():
    """Return Home Page."""

    if request.method == 'POST':

        try:
        	email = request.form('email')
        	body = request.form('content')

            contact_message = "Thanks for your email!"

            params['contact_message'] = contact_message

            send_mail(email, EMAIL, "Message from webpage", body)
        except:
            pass


    return render_template('index.html', **params)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
