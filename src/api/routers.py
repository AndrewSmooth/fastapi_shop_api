from api.goods.category import router as category_router
from api.goods.product import router as product_router
from api.goods.size import router as size_router
from api.goods.ads import router as ads_router

all_routers = [
    category_router,
    product_router,
    size_router,
    ads_router
]