from fastapi import FastAPI
from fast_car_api.routers import router as cars_router

app = FastAPI(title='fast car api')

app.include_router(cars_router)




