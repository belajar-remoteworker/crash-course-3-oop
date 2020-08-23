import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
try :
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Sukses Response {response.status_code}')
        #print(f'content{response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print((f'Hasil Pemanggilan {url}'))
        print(f'Title: {soup.title.string}')

    else:
        print(f'Ada kesalahan request{response.status_code}')

except Exception :
    print('There is an error')
print('Program ended')
