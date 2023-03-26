import os
import requests
import json

class Discord():
    #send meessage to discord channel
    def send_to_discord(message):
        # Set discord webhook env variable beforehand
        WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK')

        # Define the payload for the webhook request
        payload = {
            'content': message
        }

        # Send the webhook request
        response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

        # Check the response status code
        if response.status_code == 204:
            print('Message sent successfully')
        else:
            print(f'Error sending message: {response.status_code} - {response.text}')