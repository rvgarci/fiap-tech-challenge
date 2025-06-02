from fastapi import FastAPI
from routers.routers import router

app = FastAPI()

# Include the router from production_router.py
app.include_router(router)
