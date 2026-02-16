from sonolus_models import ServerForm, SonolusText

level_result = ServerForm(
    type="replay",
    title=SonolusText.REPLAY,
    requireConfirmation=False,
    options=[]
)