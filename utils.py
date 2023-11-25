from api import api_service


def validate_articul(number) -> bool:
    return number.isdigit() and len(number) <= 20


async def exist_in_api(number):
    return await api_service.get_product(number)


info = ("Привет! Я бот для мониторинга цен на маркетплейсе Wildberries. ...")