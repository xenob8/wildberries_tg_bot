from api import api_service


def validate_articul(number) -> bool:
    return True if number.isdigit() and len(number) <= 20 else False


def exist_in_api(number):
    return True if api_service.get_product(number) else False


def item_in_bd():
    return True


def user_already_have_its_item():
    return True
