from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL with your credentials
DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost:5432/fastdb"

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create session
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


# Base class for models
Base = declarative_base()

# Dependency to get database session
async def get_db():
    async with SessionLocal() as session:
        yield session

