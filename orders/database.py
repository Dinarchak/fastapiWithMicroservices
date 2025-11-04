from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

DB_NAME = 'fast_api_microservices2'
DATABASE_URL = f'sqlite+aiosqlite:///{DB_NAME}.db'

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
