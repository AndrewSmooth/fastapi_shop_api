from models.goods import Category, Product, Size, AdditionalImage
from .base_repository import SQLAlchemyRepository


class CategoryRepository(SQLAlchemyRepository):
    model = Category

class ProductRepository(SQLAlchemyRepository):
    model = Product

class SizeRepository(SQLAlchemyRepository):
    model = Size

class AdsRepository(SQLAlchemyRepository):
    model = AdditionalImage