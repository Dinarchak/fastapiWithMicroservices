from database import async_session_maker
from sqlalchemy import select, delete as sqlalcenmy_delete
from sqlalchemy.exc import SQLAlchemyError
from models import Order

class OrderDAO():
    @staticmethod
    async def get_all_orders():
        async with async_session_maker() as session:
            query = select(Order)
            result = await session.execute(query)
            
            return result.scalars().all()
        
    @staticmethod
    async def create_order(**values):
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = Order(**values)
                session.add(new_instance)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return new_instance
            
    @staticmethod
    async def get_order(id):
        async with async_session_maker() as session:
            query = select(Order).filter_by(id=id)
            result = await session.execute(query)

            return result.scalar_one_or_none()
