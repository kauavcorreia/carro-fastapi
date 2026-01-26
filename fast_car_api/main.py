from fastapi import FastAPI
from routers import router as cars_router

app = FastAPI(title="Fast Car API")

app.include_router(cars_router)

