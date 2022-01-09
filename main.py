import requests

places = ['Лондон', 'Шереметьево', 'Череповец']
for place in places:
    url = "https://wttr.in/{}".format(place)
    settings = {'nTq': '', 'lang': 'ru'}
    response = requests.get(url, params=settings)
    response.raise_for_status()
    # для удаления строки с ссылкой на автора weather.in
    author_application = -48
    print(response.text[:author_application])
    
