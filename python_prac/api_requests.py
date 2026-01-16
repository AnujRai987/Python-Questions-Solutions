import requests


url="https://api.freeapi.app/api/v1/public/randomproducts/product/random"
response = requests.get(url)
data =response.json()

info=data['data'] # storing data inside response data

if data['success']==True and 'data' in data:
    print(data)
    print(data['statusCode'])
    print(data['data']['title'])
    print(data['data']['description'])


    print('\n\n\n')
    for key,value in info.items():
        print(f"{key}={value}")




