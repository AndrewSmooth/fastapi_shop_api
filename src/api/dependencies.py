from repositories.category_repository import CategoryRepository
from services.goods.category_service import CategoryService


def category_service():
    return CategoryService(CategoryRepository)