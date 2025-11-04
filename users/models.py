from typing import List
from database import Base, int_pk, str_uniq
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class User(Base):
    id: Mapped[int_pk]
    username: Mapped[str_uniq]
    email: Mapped[str_uniq]
    full_name: Mapped[str_uniq]
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id'), nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    role: Mapped['Role'] = relationship('Role', back_populates='users')


class Role(Base):
    id: Mapped[int_pk]
    role: Mapped[str_uniq]

    users: Mapped[List['User']] = relationship('User', back_populates='role')
