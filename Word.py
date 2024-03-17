import requests
from twillio.rest import Client

# Def a funtion that gets the Word of the day
def get_word():
    url = "http://api.wordnik.com/v4/words.json/wordOFTheDay"
    params = {
        "api_key" : "API_KEY"
    }
    response  = requests.get(url, params=params)
    data = response.json
    word = data["word"]
    return word

# Defining a function that sends the eord of the day using the twillio API 
def send_word(word):
    ACCOUNT_SID =  'ACCOUNT_SID'
    auth_token =  'AUTH_TOKEN'
    client = twillio.rest.Client

    message  = client.messages.create(
        body = "Today's Word of the Day {word}"
        from_='YOUR TWILIO PHONE NUMBER'
        to="YOUR_PHONE_NUMBER"



    )
    
def main():
    word = get_word()
    send_word(word)

