import os.path
import sys
import json
import apiai
from api.ai import Agent

CLIENT_ACCESS_TOKEN = '871dda22df9b4278b2c1f7de27d5b9ab'
def websitelink(arg):
    pass

def main():
    user_input = ''
    while user_input!= 'exit':
        user_input = input('Me: ')
        if user_input == 'exit':
            break
        ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
        request = ai.text_request()
        request.lang = 'en'
        request.query = user_input
        response = request.getresponse().read()
        response_str = response.decode('utf-8')
        response_dict = json.loads(response_str)
        print(response_dict)
        query_response = (response_dict['result']['fulfillment']['speech'])
        print('Bot: '+ query_response)
        if ['result']['parameters']['Symptoms']:
            websitelink(['result']['parameters']['Symptoms'])

if __name__ == "__main__":
    main()