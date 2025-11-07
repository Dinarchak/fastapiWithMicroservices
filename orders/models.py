from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime
from sqlalchemy import func
from database import Base


class Order(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(nullable=False)
    item: Mapped[str] = mapped_column(nullable=False)

    created_by: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=datetime.now)
