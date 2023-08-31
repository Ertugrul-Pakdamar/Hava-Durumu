import requests
from googletrans import Translator

translator = Translator()

def KelvinConverter(temp):
    temp = int(temp - 272.15)
    return temp

api_key = 'YOUR_API_KEY_FROM_OPENWEATHERMAP'

city = input('Şehir adını giriniz: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']

    desc = translator.translate(desc, dest='tr').text
    temp = KelvinConverter(temp)

    print(f'Sıcaklık: {temp} C')
    print(f'Açıklama: {desc}')
else:
    print('Hava durumu verileri alınırken hata oluştu')

