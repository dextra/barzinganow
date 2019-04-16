import csv, json
import requests

## ESTE Script atualiza a quantidade de produtos com o valor que estiver no csv

X = []
Y = []
with open('quantity_product.csv', 'rb') as data:
    reader = csv.reader(data, delimiter=',')
    headers = {'content-type' : 'application/x-www-form-urlencoded', 'Authorization' : 'Bearer NHogQU8SvqDdiFWiJCeQIkDzo1JSEhRH'}
    params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}
    for line in reader:
        url = "https://barzinganow.appspot.com/api/product/"
        # url = "http://localhost:8080/api/product/"
        url += line[0]
        url += "/quantity"
        data = {"quantity": int(line[4]), 'name' : line[1]}
        print data
        print requests.put(url, data=data, headers=headers, params=params)