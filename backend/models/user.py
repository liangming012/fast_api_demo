from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base


class User(Base):

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)

    items: Mapped[List["Item"]] = relationship(back_populates="owner", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, full_name={self.full_name!r}, email={self.email!r}), " \
               f"is_active={self.is_active!r}, is_superuser={self.is_superuser!r})"




