import requests
from urllib.parse import quote


def search_request(string):
    encoded_query = quote(string)

    url = f"https://search.wb.ru/exactmatch/ru/male/v7/search?ab_testing=false&appType=1&curr=rub&dest=-1257403&query={encoded_query}&resultset=catalog&sort=popular&spp=30&suppressSpellcheck=false&uclusters=3&uiv=7&uv=MDGvyyBBI96tKhwiLTKlcyX4Lb0umDE2q3mklJ8UHKYlsa_-p9UvhLAFosmo8rBuLbwscixGKyIpKKx9rEyqGa1fMTGmVKyjL_Glra3JruGu4yz1MJmrYKqBKQyuHLH3LhcudKxILWYnj67HLwuqb6isqyqwGxlNshSr7qmWLH-t2jF_J9KkfbFlKAiVnzCHq44p8SjAMJ8mY6aWknkqdqvxrRYxLzJMHSys77ANsI0vWa2sLBKr7i7SIfmm4aSCpcUR8quYK7qgBCO3qASqSyMmrZArFS6KL96nx6gPMISh96UnsfKcCbILq5Sv6i-ooQMer6jLrjQurjEsLkGsEA"

    params = {
        "ab_testing": "false",
        "appType": "1",
        "curr": "rub",
        "dest": "-1257403",
        "query": "%D1%81%D1%82%D1%83%D0%BB",
        "resultset": "catalog",
        "sort": "popular",
        "spp": "30",
        "suppressSpellcheck": "false",
        "uclusters": "3",
        "uiv": "7",
        "uv": "MDGvyyBBI96tKhwiLTKlcyX4Lb0umDE2q3mklJ8UHKYlsa_-p9UvhLAFosmo8rBuLbwscixGKyIpKKx9rEyqGa1fMTGmVKyjL_Glra3JruGu4yz1MJmrYKqBKQyuHLH3LhcudKxILWYnj67HLwuqb6isqyqwGxlNshSr7qmWLH-t2jF_J9KkfbFlKAiVnzCHq44p8SjAMJ8mY6aWknkqdqvxrRYxLzJMHSys77ANsI0vWa2sLBKr7i7SIfmm4aSCpcUR8quYK7qgBCO3qASqSyMmrZArFS6KL96nx6gPMISh96UnsfKcCbILq5Sv6i-ooQMer6jLrjQurjEsLkGsEA"
    }

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ru-RU,ru;q=0.9",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjkwOTMyNjAsInZlcnNpb24iOjIsInVzZXIiOiI2MTU4NjI3MyIsInNoYXJkX2tleSI6IjEiLCJjbGllbnRfaWQiOiJ3YiIsInNlc3Npb25faWQiOiIzZmU4ZGQzNThhZWI0NzQ3YTlhMjhlNmFiYzc2YTI4MiIsInVzZXJfcmVnaXN0cmF0aW9uX2R0IjoxNjYwNDcwODUzLCJ2YWxpZGF0aW9uX2tleSI6ImIxMWM3MjQ4NTczMWVjYTk0MDNhMGYxMTQzOWViM2Y1YjUwNWFlMWVhMjQ2OGFhYzIyZWMxZjM3OTljMjQ2ZDMiLCJwaG9uZSI6InEzbm45QlFINk5jUmR5bEs1SUFEYkE9PSJ9.I5a6sFHDReVEwulVeIj_2XslDxqprVm1x9VEPV7tRx-7LCIsnjvkoxyrOaruDqABpiB3rp0p8BL1deWdIrd3mf55AEjlRyxZksxU4qR3PPc5O8QCIOLSIGAcohjbbWkRdonLLK7HUZD9gP3P60aeqdmWT7xvQFlJC4G_Zi_liCLxu9FiEdJ32KVjV0td8CGC6BZGS7jZFhZptilxh34W0bmJ8eFmvCcTeqIny0HowVwvTgP-LA4vxDtRdn5cfm_K72ojBUwFRFAmUwv1lfZBZH1RdVzc1KsTjXT89AjSCRTi9auYFwXR3-FBuDqZsVABeTusEQKBVXVqJUWwHpS54w",
        "Connection": "keep-alive",
        "Host": "search.wb.ru",
        "Origin": "https://www.wildberries.ru",
        "Referer": "https://www.wildberries.ru/catalog/0/search.aspx?search=%D1%81%D1%82%D1%83%D0%BB",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "x-queryid": "qid15781490172495954020241016160745",
        "x-userid": "61586273"
    }

    response = requests.get(url, headers=headers, params=params)

    return response


def data_processor(data, article):
    for index, product in enumerate(data['data']['products']):
        if product['id'] == article:
            return (index + 1) if index < 5000 else None
    else:
        return None


def article_position(string, article):
    response = search_request(string)
    return data_processor(response.json(), article)


print(article_position('Велосипед', 206710175))
