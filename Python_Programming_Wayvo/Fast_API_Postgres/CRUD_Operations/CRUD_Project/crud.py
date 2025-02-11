from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import User
from schemas import UserCreate

# Create User
async def create_user(db: AsyncSession, user: UserCreate):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

# Get All Users
async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

# Get User by ID
async def get_user_by_id(db: AsyncSession, user_id: int):
    return await db.get(User, user_id)

# Update User
async def update_user(db: AsyncSession, user_id: int, user_data: UserCreate):
    user = await db.get(User, user_id)
    if user:
        user.name = user_data.name
        user.email = user_data.email
        await db.commit()
        await db.refresh(user)
    return user

# Delete User
async def delete_user(db: AsyncSession, user_id: int):
    user = await db.get(User, user_id)
    if user:
        await db.delete(user)
        await db.commit()
    return user
