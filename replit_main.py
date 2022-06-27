# the os module helps us access environment variables
# i.e., our API keys
import os

# these modules are for querying the Hugging Face model
import json
import requests

# the Discord Python API
import discord

# this is my Hugging Face profile link
API_URL = 'https://api-inference.huggingface.co/models/TejasARathod/'

class MyClient(discord.Client):
    def __init__(self, model_name): # Here the model name is DialoGPT-medium-BatmanBot
        super().__init__()
        # We store the api endpoint by concatenating profile link and the model
        self.api_endpoint = API_URL + model_name
        # retrieve the secret API token from the system environment
        huggingface_token = os.environ['HUGGINGFACE_TOKEN']
        # format the header in our request to Hugging Face
        self.request_headers = {
            'Authorization': 'Bearer {}'.format(huggingface_token)
        }
# here we are creating a payload that takes in the dump
# we dump the payload as a json string
    def query(self, payload):
        """
        make request to the Hugging Face model API
        """
        data = json.dumps(payload)
        # use the request module to make an http post request to the api endpoint using our defined request headers which contains our hugging face api key and passing the data
        response = requests.request('POST',
                                    self.api_endpoint,
                                    headers=self.request_headers,
                                    data=data)
      # Once the request finishes it should give us a response object and we decode it from utf-8 and load the result as a string and return the string
        ret = json.loads(response.content.decode('utf-8'))
        return ret

# Here we define asynchronous function
    async def on_ready(self):
        # print out information when the bot wakes up
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        # send a request to the model without caring about the response
        # just so that the model wakes up and starts loading
        self.query({'inputs': {'text': 'Hello!'}})

    async def on_message(self, message):
        """
        this function is called whenever the bot sees a message in a channel
        """
        # ignore the message if it comes from the bot itself
        if message.author.id == self.user.id:
            return

        # form query payload with the content of the message
        payload = {'inputs': {'text': message.content}}

        # while the bot is waiting on a response from the model
        # set the its status as typing for user-friendliness
        async with message.channel.typing():
          response = self.query(payload)
        bot_response = response.get('generated_text', None)
        
        # we may get ill-formed response if the model hasn't fully loaded
        # or has timed out
        if not bot_response:
            if 'error' in response:
                bot_response = '`Error: {}`'.format(response['error'])
            else:
                bot_response = 'Hmm... something is not right.'

        # send the model's response to the Discord channel
        await message.channel.send(bot_response)

def main():
    # DialoGPT-medium-Batman is my model name ; just pass in the model
    client = MyClient('DialoGPT-medium-BatmanBot')
    client.run(os.environ['DISCORD_TOKEN'])

if __name__ == '__main__':
  main()