from sonolus_models import ServerForm, SonolusText
from pydantic import BaseModel

level_result = ServerForm(
    type="replay",
    title=SonolusText.REPLAY,
    requireConfirmation=False,
    options=[]
)

class ServerUploadLevelResultResponse(BaseModel):
    success: bool