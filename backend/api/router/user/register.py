from fastapi import APIRouter, Depends, Body, HTTPException, status
from sonolus_fastapi.utils.generate import generate_random_string
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from db.session import get_db
from db.models import User
from api.model.user import UserRegister_Login_Request_Body, UserRegisterResponse, UserSchema
from datetime import datetime, timezone

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=UserRegisterResponse)
async def register_user(
    db: Session = Depends(get_db),
    body: UserRegister_Login_Request_Body = Body(...)
) -> UserRegisterResponse:
    """
    POST /api/user/register
    """
    exsting_user = db.query(User).filter(User.name == body.name).first()
    if exsting_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists | ユーザーは既に存在しています")
    
    id = generate_random_string(16)
    hashed_password = pwd_context.hash(body.password)
    created_at = datetime.now(timezone.utc)

    db_user = User(
        id=id,
        name=body.name,
        password=hashed_password,
        profile=None,
        created_at=created_at
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return UserRegisterResponse()