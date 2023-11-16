import requests
def get_product(number):
    url = f"https://card.wb.ru/cards/detail?appType=1&curr=rub&dest=-1257786&spp=29&nm={number}"
    response = requests.get(url)
    data = response.json()
    product = data["data"]["products"]
    return product

def get_image(number):
    url = f"https://basket-{number//100000%144+1}.wb.ru/vol{number//100000}/partl{number//1000}/{number}/images/big/1.webp"
    response = requests.get(url)
    if response.status_code == 200:
        img_bytes = response.content
        return img_bytes
    else:
        return None

def get_price_history(number):
    url = f"https: // basket - {number // 100000 % 144 + 1}.wb.ru / vol{number // 100000} / partl{number // 1000} / {number} / info / price - history.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None