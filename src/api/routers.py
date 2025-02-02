from src.api.goods.category import router as category_router
from src.api.goods.product import router as product_router
from src.api.goods.size import router as size_router
from src.api.goods.ads import router as ads_router

all_routers = [
    category_router,
    product_router,
    size_router,
    ads_router
]