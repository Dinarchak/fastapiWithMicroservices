from database import async_session_maker
from sqlalchemy import select, delete as sqlalchemy_delete
from sqlalchemy.exc import SQLAlchemyError
from models import Role, User

class RoleDAO():

    @staticmethod
    async def get_role(role_name: str):
        async with async_session_maker() as session:
            query = select(Role).filter_by(role=role_name)
            result = await session.execute(query)

            return result.scalar_one_or_none()


class UserDAO():

    @staticmethod
    async def get_user(**filters):
        async with async_session_maker() as session:
            query = select(User).filter_by(**filters)
            result = await session.execute(query)

            return result.scalar_one_or_none()


    @staticmethod
    async def get_all_users():
        async with async_session_maker() as session:
            query = select(User)
            result = await session.execute(query)

            return result.scalars().all()
        
    # почему отличается от остальных методов
    @staticmethod
    async def create_user(**values):
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = User(**values)
                session.add(new_instance)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return new_instance
            
    
    @staticmethod
    async def delete_user(id: int):
        async with async_session_maker() as session:
            async with session.begin():
                query = sqlalchemy_delete(User).filter_by(id=id)
                result = await session.execute(query)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
            return result.rowcount
