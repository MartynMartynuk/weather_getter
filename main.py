import requests


places = ['Лондон', 'Шереметьево', 'Череповец']

for place in places:
    url = r'http://wttr.in/{}?nTq&lang=ru'.format(place)
    response = requests.get(url)
    print(response.text[:-48])