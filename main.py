import requests

places = ['Лондон', 'Шереметьево', 'Череповец']
for place in places:
    url = "https://wttr.inaa/{}".format(place)
    settings = {'nTq': '', 'lang': 'ru'}
    response = requests.get(url, params=settings)
    response.raise_for_status()
    author_application = -48    #для удаления строки с ссылкой на автора weather.in
    print(response.text[:author_application])
