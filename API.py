import json
import apiai
from google import search
import requests, bs4

CLIENT_ACCESS_TOKEN = '871dda22df9b4278b2c1f7de27d5b9ab'

def websitelink(symptom):
    list = []
    for result in search(symptom + ' symptom mayo clinic', stop = 20):
        list.append(result)
    url = list[0]
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text)
    print(url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html5lib')
    find_Match = soup.find('p', text='Signs and symptoms of ' + symptom + ' may include:')
    soup2 = bs4.BeautifulSoup(res.text, 'html5lib')
    loc = soup2.prettify().index('Signs and symptoms of ' + symptom + ' may include:')
    soup2 = bs4.BeautifulSoup(soup2.prettify()[loc:], 'html5lib')
    find_Match2 = soup2.find('ul')
    list = []
    for item in find_Match2:
        list.append(str(item))
    symptomsList = []
    for item in list:
        item = item.replace('\n', '').replace('<li>', '').replace('</li>', '').strip()
        if item != '':
            symptomsList.append(item)
    print(find_Match.text)
    for x in symptomsList:
        print('-' + x)

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
