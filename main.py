import requests

places = ['Лондон', 'Шереметьево', 'Череповец']

try:
    for place in places:
        url = "https://wttr.in/{}".format(place)
        settings = {'nTq':'', 'lang':'ru'}
        response = requests.get(url, params=settings)
        response.raise_for_status()
        author_application = -48    #строка с ссылкой на автора weather.in
        print(response.text[:author_application])
except requests.exceptions.ConnectionError:
    print('ERROR! ConnectionError')
