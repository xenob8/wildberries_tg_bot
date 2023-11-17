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


def get_image(number) -> str:
    return f"https://basket-{number//100000//144+1:02}.wb.ru/vol{number//100000}/part{number//1000}/{number}/images/big/{1}.webp"


async def get_price_history(number):
    number = int(number)
    async with get_session(f"https://basket-{number//100000//144+1:02}.wb.ru/") as session:
        async with session.get(
                f"/vol{number//100000}/part{number//1000}/{number}/info/price-history.json") as resp:
            return resp.json() if resp.ok else None

