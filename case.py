import sys
import json
import time
import hmac
import hashlib
import requests
from colorama import init, Fore
from urllib.parse import unquote


init(autoreset=True)


class Data:
    def __init__(self, init_data, userid, username, secret):
        self.init_data = init_data
        self.userid = userid
        self.username = username
        self.secret = secret


class PixelTod:
    def __init__(self):
        self.INTERVAL_DELAY = 1
        self.base_headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
            "Host": "api.app.steamify.io",
            "X-Requested-With": "org.telegram.messenger",
            'origin': 'https://app.steamify.io',
            'referer': 'https://app.steamify.io',
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        }

    def get_secret(self, userid):
        rawr = "adwawdasfajfklasjglrejnoierjboivrevioreboidwa"
        secret = hmac.new(rawr.encode("utf-8"), str(userid).encode("utf-8"), hashlib.sha256).hexdigest()
        return secret

    def data_parsing(self, data):
        return {key: value for key, value in (i.split('=') for i in unquote(data).split('&'))}

    def main(self):
        with open("initdata.txt", "r") as file:
            datas = file.read().splitlines()

        print(f'{Fore.LIGHTYELLOW_EX}Обнаружено аккаунтов: {len(datas)}')
        if not datas:
            print(f'{Fore.LIGHTYELLOW_EX}Пожалуйста, введите свои данные в initdata.txt')
            sys.exit()
        print('-' * 50)
        while True:
            for no, data in enumerate(datas):
                print(f'{Fore.LIGHTYELLOW_EX}Номер аккаунта: {Fore.LIGHTWHITE_EX}{no + 1}')
                data_parse = self.data_parsing(data)
                user = json.loads(data_parse['user'])
                userid = str(user['id'])
                first_name = user.get('first_name')
                last_name = user.get('last_name')
                username = user.get('username')

                print(f'{Fore.LIGHTYELLOW_EX}Аккаунт: {Fore.LIGHTWHITE_EX}{first_name} {last_name}')
                secret = self.get_secret(userid)
                new_data = Data(data, userid, username, secret)
                self.process_account(new_data)
                print('-' * 50)
                self.countdown(self.INTERVAL_DELAY)

    def process_account(self, data: Data):

        id_input, num = self.show_case_options(data)

        try:
            num = int(num)
        except ValueError:
            print(f'{Fore.LIGHTRED_EX}Неверное количество кейсов. Пожалуйста, введите целое число.')
            return

        for _ in range(num):
            self.claim_case(data, id_input)
            self.countdown(self.INTERVAL_DELAY)

    def countdown(self, t):
        while t:
            one, two = divmod(t, 3600)
            three, four = divmod(two, 60)
            print(f"{Fore.LIGHTWHITE_EX}Ожидание до {one:02}:{three:02}:{four:02} ", flush=True, end="\r")
            t -= 1
            time.sleep(1)
        print("                          ", flush=True, end="\r")

    def api_call(self, url, data=None, headers=None, method='GET'):
        while True:
            try:
                if method == 'GET':
                    res = requests.get(url, headers=headers)
                elif method == 'POST':
                    res = requests.post(url, headers=headers, data=data)
                else:
                    raise ValueError(f'Не поддерживаемый метод: {method}')

                if res.status_code == 401:
                    print(f'{Fore.LIGHTRED_EX}{res.text}')

                open('.http.log', 'a', encoding='utf-8').write(f'{res.text}\n')
                return res
            except (
            requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
            requests.exceptions.Timeout):
                print(f'{Fore.LIGHTRED_EX}Ошибка подключения соединения!')
                continue



    def claim_case(self, data: Data, id_input):
        url = f"https://api.app.steamify.io/api/v1/game/case/{id_input}/open"
        headers = self.base_headers.copy()
        headers["Authorization"] = f"Bearer {data.init_data}"
        payload = {'count': 1}
        res = self.api_call(url, data=json.dumps(payload), headers=headers, method='POST')
        response_json = res.json()
        #print(f'{response_json}')
        suc = response_json.get('success', {})
        cases = response_json.get('data', [])

        if suc:
            for case in cases:
                case_name = case.get('name')
                if case_name:
                    print(f"{Fore.LIGHTBLUE_EX}{case_name}")
        else:
            print(f"{Fore.LIGHTRED_EX}Не удалось открыть кейс.")

    def show_case_options(self, data: Data):
        url = "https://api.app.steamify.io/api/v1/game/case/list"
        headers = self.base_headers.copy()
        headers["Authorization"] = f"Bearer {data.init_data}"
        res = self.api_call(url, headers=headers)
        response_json = res.json()
        #print(f'{response_json}')

        url_balance = 'https://api.app.steamify.io/api/v1/user/me'
        headers_balance = self.base_headers.copy()
        headers_balance["Authorization"] = f"Bearer {data.init_data}"
        res_balance = self.api_call(url_balance, headers=headers_balance)
        response_json_balance = res_balance.json()
        balance = response_json_balance.get('data', {}).get('points', 0)
        print(f'{Fore.LIGHTYELLOW_EX}Общий баланс: {Fore.LIGHTWHITE_EX}{balance}')
        cases = response_json.get('data', [])
        if not cases:
            print(f'{Fore.LIGHTRED_EX}Не удалось получить список кейсов.')
            return None, 0

        print(f'{Fore.LIGHTYELLOW_EX}Доступные кейсы:')
        for case in cases:
            case_id = case.get('id')
            name = case.get('name')
            price = case.get('price')
            max_count = balance // price
            print(f"{Fore.LIGHTYELLOW_EX}{case_id} = {Fore.LIGHTWHITE_EX}{name} {Fore.LIGHTYELLOW_EX}Цена: {price} Можно открыть: {Fore.LIGHTWHITE_EX}{int(max_count)}")

        id_input = input(f"{Fore.LIGHTYELLOW_EX}Введи номер кейса:\n")
        num = input(f"{Fore.LIGHTYELLOW_EX}Сколько открывать?\n")

        return id_input, num


if __name__ == "__main__":
    try:
        app = PixelTod()
        app.main()
    except KeyboardInterrupt:
        sys.exit()
