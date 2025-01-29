from models.goods import Category
from .base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    model = Category