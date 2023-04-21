from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base


class Item(Base):

    __tablename__ = "item"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(index=True)
    description: Mapped[str] = mapped_column(index=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    owner: Mapped["User"] = relationship(back_populates="items")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, title={self.title!r}, description={self.description!r}), " \
               f"owner_id={self.owner_id!r})"



