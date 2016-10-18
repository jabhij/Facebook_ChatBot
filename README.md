## Facebook ChatBot

Creating a ChatBot using Python for my facebook page.

## Description



## How To?

### Install Dependencies 

#### Python Packages

Install Flask and requests using `pip` if you already don't have any in your machine.

`pip install flask
pip install requests`

#### ngrok

For the headache free webhook integrations and securing tunnel connection with facebook.

Install `ngrok` from [web - ngrok](https://ngrok.com/)

### Runing Server & Tunnel Connection

- Run the dev server using    
`fb_chatbot_server.py`

- Now use `ngrok` to tunnel the connection, as:   
`ngrok http 80`

- Now, you'll get to see a active url for your local server, as:    
`https://4e9f87b7.ngrok.io`

