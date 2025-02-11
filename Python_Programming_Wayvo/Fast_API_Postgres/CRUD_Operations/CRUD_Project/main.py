from fastapi import FastAPI
from database import engine, Base
from routes import router

app = FastAPI()

# Create database tables
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def startup():
    await init_db()

# Include API router
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "FastAPI CRUD App is Running!"}
