from sqlalchemy import insert
from sqlalchemy.orm import sessionmaker, Session
from db.models.product import Product
from db.models.user import User
from db.models.user_product import UserProduct
from db.product_service import ProductService
from db.utils import session_decorator, session_decorator_nested


class UserService:

    def __init__(self, engine):
        self.session = sessionmaker(bind=engine)

    @session_decorator
    def get_user(self, telegram_id, session: Session):
        return session.query(User).filter_by(telegram_id=telegram_id).first()

    @session_decorator
    def add_user(self, telegram_id, session: Session):
        inserting_user = insert(User).values(telegram_id=telegram_id)
        session.execute(inserting_user)

    @session_decorator
    def get_user_products(self, telegram_id: int, session: Session):
        products = session.query(Product).join(UserProduct).filter(UserProduct.user_telegram_id == telegram_id).all()
        return products

    @session_decorator_nested
    def delete_user_product(self, telegram_id, product_number, session: Session):
        user_product = session.query(UserProduct).filter_by(user_telegram_id=telegram_id).join(Product).filter_by(
            number=product_number).first()
        if user_product:
            session.delete(user_product)
            session.commit()

    @session_decorator_nested
    def patch_alert_threshold(self, telegram_id, product_number, alert_threshold: int, session: Session):
        product_id = session.query(Product).filter_by(number=product_number).first()
        user_product = session.query(UserProduct).filter_by(user_telegram_id=telegram_id, product_id=product_id)
        if user_product:
            user_product.update({"alert_threshold": alert_threshold})
            session.commit()

    @session_decorator
    def add_user_product(self, telegram_id, product: Product, session: Session):
        if not ProductService.product_exists_by_number(product.number, session):
            ProductService.add_product(product, session)
        user_product = UserProduct(telegram_id, product.id, product.price, 0)
        session.add(user_product)
