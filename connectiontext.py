"""
Just for connection check up, nothing more than that.
Ignore this file
"""

# Importing FLASK 
from flask import Flask, request

app = Flask(__name__)

# Setting a ROUTE through GET method
@app.route('/', methods=['GET'])
def handle_verification():
    return request.args['hub.challange']
    
if __name__  == '__main__':
    app.run(debug=True)
