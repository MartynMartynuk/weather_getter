import requests


urls = [r'http://wttr.in/Лондон?nTq&lang=ru',
        r'http://wttr.in/Шереметьево?nTq&lang=ru',
        r'http://wttr.in/Череповец?nTq&lang=ru']

for url in urls:
    response = requests.get(url)
    print(response.text[:-48])