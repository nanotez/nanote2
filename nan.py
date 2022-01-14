import requests

nomer = input('Номер :')

a= requests.post("https://my.telegram.org/auth/send_password",
                 json={"phone": "+" + nomer},)
print("отправлено")
