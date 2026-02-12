from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, auth, schemas

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(models.User).filter(models.User.email == email))
    return result.scalars().first()

async def create_user(db: AsyncSession, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_devices(db: AsyncSession, user_id: int):
    result = await db.execute(select(models.Device).filter(models.Device.user_id == user_id))
    return result.scalars().all()

async def create_device(db: AsyncSession, device: schemas.DeviceCreate, user_id: int):
    db_device = models.Device(**device.dict(), user_id=user_id)
    db.add(db_device)
    await db.commit()
    await db.refresh(db_device)
    return db_device
