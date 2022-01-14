import requests

nomer = input('Номер :')

a= requests.post("https://rider.uklon.com.ua/api/v1/phone/send-code",
                 json={"phone": nomer},)
print(a.отправлено)
