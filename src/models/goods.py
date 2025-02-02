from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from typing import Annotated

from src.core.database import Base
from src.schemas.goods import CategoryReturn, ProductReturn, AdsReturn, SizeReturn


intpk = Annotated[int, mapped_column(autoincrement=True, primary_key=True)]

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    products: Mapped[list["Product"]] = relationship(back_populates="category", uselist=True)
    # category.products.append(product)

    def to_read_model(self) -> CategoryReturn:
        return CategoryReturn(
            id=self.id,
            name=self.name,
        )

    def __str__(self):
        return (f"{self.name}")

    def __repr__(self):
        return str(self.name)


class Product(Base):
    __tablename__ = "products"

    id: Mapped[intpk]
    image: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    price: Mapped[float] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=True)
    amount: Mapped[int] = mapped_column(nullable=False)
    category: Mapped["Category"] = relationship(back_populates="products", uselist=False)
    category_fk: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    size: Mapped["Size"] = relationship(back_populates="products", uselist=False)
    size_fk: Mapped[int] = mapped_column(ForeignKey("sizes.id"))
    ads: Mapped[list["AdditionalImage"]] = relationship(back_populates="product", uselist=True) 
    
    def to_read_model(self) -> ProductReturn:
        return ProductReturn(
            id=self.id,
            name=self.name,
            description=self.description,
            image=self.image,
            price=self.price,
            rating=self.rating,
            amount=self.amount,
            category_id=self.category_fk,
            size_id=self.size_fk,
        )

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"name={self.name!r},")

    def __repr__(self):
        return str(self)


class AdditionalImage(Base):
    __tablename__ = "ads"

    id: Mapped[intpk]
    path: Mapped[str]
    product: Mapped["Product"] = relationship(back_populates="ads", uselist=False)
    product_fk: Mapped[int] = mapped_column(ForeignKey("products.id"))

    def to_read_model(self) -> AdsReturn:
        return AdsReturn(
            id=self.id,
            path=self.path,
            product_id=self.product_fk
        )

class ProductAds(Base):
    __table_name__ = "product_ads"
    id: Mapped[intpk]
    product_fk = mapped_column(ForeignKey("products.id"))
    ads_fk = mapped_column(ForeignKey("ads.id"))

class Size(Base):
    __tablename__ = "sizes"
    id: Mapped[intpk]
    name: Mapped[str]
    products: Mapped[list["Product"]] = relationship(back_populates="size", uselist=True)

    def to_read_model(self) -> SizeReturn:
        return SizeReturn(
            id=self.id,
            name=self.name,
        )