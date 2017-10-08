import os.path
import sys
import json
import apiai
from google import search

CLIENT_ACCESS_TOKEN = '871dda22df9b4278b2c1f7de27d5b9ab'

def websitelink(symptom):
    list = []
    for result in search(symptom + ' symptom mayo clinic', stop = 20):
        list.append(result)
    url = list[0]
    print(url)

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
        try:
            if response_dict['result']['parameters']['Symptoms']:
                websitelink(response_dict['result']['parameters']['Symptoms'][0])
        except:
            pass

if __name__ == "__main__":
    main()
