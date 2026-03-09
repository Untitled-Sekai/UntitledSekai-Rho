from fastapi import APIRouter

from .user import user_router
from .chart import chart_router

api_router = APIRouter(prefix="/api")

api_router.include_router(user_router)
api_router.include_router(chart_router)