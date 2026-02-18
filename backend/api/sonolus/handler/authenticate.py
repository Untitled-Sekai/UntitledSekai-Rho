from ...instance import sonolus
from sonolus_models import ServerAuthenticateResponse, ServiceUserProfile
from sonolus_fastapi.utils.context import SonolusContext
from sonolus_fastapi.utils.generate import generate_random_string
from sonolus_fastapi.utils.session import SessionData
import time

# ---------------------------------------------------------------

@sonolus.server.authenticate(ServerAuthenticateResponse)
async def authenticate(ctx: SonolusContext) -> ServerAuthenticateResponse:
    """
    POST /sonolus/authenticate
    """
    session = generate_random_string(32)
    expiration = int(time.time() * 1000) + 3600 * 1000 # 1時間後に期限切れ
    profile: ServiceUserProfile = ctx.request.user_profile

    session_data = SessionData(session=session, expiretion=expiration, profile=profile)
    sonolus.session_store.set(session, session_data)

    return ServerAuthenticateResponse(
        session=session,
        expiretion=expiration,
    )