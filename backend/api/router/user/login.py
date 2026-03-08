from fastapi import APIRouter, Depends, Body, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from db.session import get_db
from db.models import User
from api.model.user import UserRegister_Login_Request_Body, UserLoginResponse

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/login", response_model=UserLoginResponse)
async def login_user(
    db: Session = Depends(get_db),
    body: UserRegister_Login_Request_Body = Body(...)
) -> UserLoginResponse:
    """
    POST /api/user/login
    """
    user = db.query(User).filter(User.name == body.name).first()
    if not user or not pwd_context.verify(body.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password | ユーザー名またはパスワードが無効です")
    
    return UserLoginResponse()