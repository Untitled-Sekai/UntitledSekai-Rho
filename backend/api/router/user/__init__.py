from fastapi import APIRouter

from .login import router as login_router
from .register import router as register_router
from .sonolus import router as sonolus_router

user_router = APIRouter(prefix="/user")

user_router.include_router(login_router, prefix="/login")
user_router.include_router(register_router, prefix="/register")
user_router.include_router(sonolus_router, prefix="/sonolus")