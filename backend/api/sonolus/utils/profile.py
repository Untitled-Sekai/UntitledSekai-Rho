from sonolus_fastapi import Sonolus
from sonolus_fastapi.utils.context import SonolusContext
from sonolus_models import ServiceUserProfile

def get_profile(ctx: SonolusContext, sonolus: Sonolus) -> ServiceUserProfile | None:
    session = ctx.user_session
    if session is None:
        return None
    
    session_data = sonolus.session_store.get(session)
    if session_data:
        return session_data.profile
    
    return None