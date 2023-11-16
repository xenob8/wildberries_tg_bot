import aiohttp


def get_session(path):
    return aiohttp.ClientSession(path)


async def get_product(number):
    par = {
        "appType": 1,
        "curr": "rub",
        "dest": -1257786,
        "nm": number,
    }
    async with get_session("https://card.wb.ru/") as session:
        async with session.get("/cards/detail", params=par) as resp:
            data = await resp.json()
            product = data["data"]["products"]
            return product


async def get_image(number):
    number = int(number)
    async with get_session(f"https://basket-{number // 100000 % 144 + 1}.wb.ru/") as session:
        print(f"https://basket-{number // 100000 % 144 + 1}.wb.ru/")
        print(f"/vol{number // 100000}/part{number // 1000}/{number}/images/big/1.webp")
        async with session.get(f"/vol{number // 100000}/part{number // 1000}/{number}/images/big/1.webp") as resp:
            if resp.ok:
                img_bytes = resp.content
                return img_bytes
            else:
                return None


async def get_price_history(number):
    number = int(number)
    async with get_session(f"https: // basket - {number // 100000 % 144 + 1}.wb.ru /") as session:
        async with session.get(
                "/vol{number // 100000} / partl{number // 1000} / {number} / info / price - history.json") as resp:
            return resp.json() if resp.ok else None
