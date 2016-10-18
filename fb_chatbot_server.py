# Import Flask    
from flask import Flask, request
import requests

app = Flask(__name__)

# Provide Access Token
"""
Alike -
EACYKP066VrUBAP0YUzCYMsbk1543fXCqAPrC5NEUfmkZC1JJRHkwzZBOKPXKuxhzliy7hMjVuVBhsu6fxzB6B9t87kO9eCK7vR8mU6sBAMLZB14j72fqWJeUfWu7IZBV8vwfdZCDmCFdOK2HSJUXW2KjaRqvaxUW36u2fHwRXbAZDZD
"""
ACCESS_TOKEN = " "
VERIFY_TOKEN = " "

# Reply Request
def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

# Access Route - GET Call
@app.route('/', methods=['GET'])
def handle_verification():
    if request.args['hub.verify_token'] == VERIFY_TOKEN:
        return request.args['hub.challenge']
    else:
        return "Invalid verification token"

# Access Route - POST Call
@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, message)

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
