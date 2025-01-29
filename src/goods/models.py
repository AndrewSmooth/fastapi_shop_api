from sqlalchemy import ForeignKey, text, Text, String, Sequence
from sqlalchemy.orm import relationship, Mapped, mapped_column

from datetime import date
from typing import Annotated

from database import Base

intpk = Annotated[int, mapped_column(autoincrement=True, primary_key=True)]

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    products: Mapped["Product"] = relationship("Product", uselist=True)
    # accessories: Mapped[list["Accessory"]] = relationship()

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"name={self.name!r},")

    def __repr__(self):
        return str(self)

class Product(Base):
    __tablename__ = "products"

    id: Mapped[intpk]
    image: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    price: Mapped[float] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=True)
    amount: Mapped[int] = mapped_column(nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    # category: Mapped["Category"] = mapped_column(nullable=False)
    # size: Mapped["Size"] = relationship()
    # size_fk: Mapped[int] = mapped_column(ForeignKey("sizes.id"))
    # ads: Mapped["AdditionalImage"] = relationship()
    # ads_fk: Mapped[int] = mapped_column(ForeignKey("ads.id"))
    
    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"name={self.name!r},")

    def __repr__(self):
        return str(self)


# class AdditionalImage(Base):
#     __tablename__ = "ads"

#     id: Mapped[intpk]
#     path: Mapped[str]
#     product: Mapped["Product"] = relationship()
#     product_fk: Mapped[int] = mapped_column(ForeignKey("products.id"))

# class Size(Base):
#     __tablename__ = "sizes"
    
#     id: Mapped[intpk]
#     name: Mapped[str]