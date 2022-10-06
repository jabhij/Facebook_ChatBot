## Facebook ChatBot

Creating a ChatBot using Python for my [Facebook Page](https://www.facebook.com/geeksangle/).

## Description

- Language: Python
- Packages: `Flask & Requests`
- Input: `From your Facebook Page`
- Output: `Message Deliveries, Message Reads, Messages, Message Echoes, Messaging Options, Messaging Postbacks, etc info.`

## How To?

Follow the steps described below.

### 1 - Install Dependencies 

#### 1.1 Python Packages

Install Flask and requests using `pip` if you already don't have any in your machine.

`pip install flask`    
`pip install requests`

#### 1.2 ngrok

For the headache free webhook integrations and securing tunnel connection with facebook.

Install `ngrok` from [web - ngrok](https://ngrok.com/)

### 2 - Runing Server & Tunnel Connection

- Run the dev server using    
`fb_chatbot_server.py`

- Now use `ngrok` to tunnel the connection, as:   
`ngrok http 80`

- Now, you'll get to see a active url for your local server, as:    
`https://4e9f87b7.ngrok.io`

### 3 - Setup Facebook App (Guidelines)

- Create a [Facebook App](https://developers.facebook.com/apps/).
- Add a Product- `Messenger`.
- Enable webhooks. Use the above URL as the callback webhook URL.
- Edit [fb_chatbot_server.py](https://github.com/jabhij/Facebook_ChatBot/blob/master/fb_chatbot_server.py) and update the `VERIFY_TOKEN` with the token you set.
- Once the callback is verified, subscribe the app to one of your pages.
- Generate a `Page Access Token` for your page.
- Edit [fb_chatbot_server.py](https://github.com/jabhij/Facebook_ChatBot/blob/master/fb_chatbot_server.py) and update the `ACCESS_TOKEN` with the new token.

### Catch me

For any query, ping me on 
- LinkedIn: [@jabhij](https://www.linkedin.com/in/jabhij/)
- Twitter: [@jabhij](https://twitter.com/jabhij)
- Web: [LetUsTweak](http://letustweak.com)

Hope, it helps!! ヅ
