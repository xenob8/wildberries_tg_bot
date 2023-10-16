from sqlalchemy.orm import sessionmaker
from db.models.product import Product

class ProductService:

    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)

    def product_exists_by_number(self, number):
        session = self.Session()
        try:
            product = session.query(Product).filter_by(number=number).first()
            return product is not None
        finally:
            session.close()
