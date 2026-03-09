from fastapi import APIRouter, Depends, HTTPException, status
from sonolus_models import (
    ServerAuthenticateExternalRequest,
    ServerAuthenticateExternalResponse,
    ServiceUserProfile
)
from db.models import User
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()

@router.post("/sonolus/external", response_model=ServerAuthenticateExternalResponse)
async def authenticate_external(
    req: ServerAuthenticateExternalRequest,
    db: Session = Depends(get_db)
) -> ServerAuthenticateExternalResponse:
    """
    POST /api/user/sonolus/external
    """