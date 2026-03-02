from ...instance import sonolus
from sonolus_fastapi.utils.context import SonolusContext
from sonolus_models import (
    SonolusServerInfo,
    ServerInfoAuthenticationButton,
    ServerInfoItemButton,
    ServerInfoConfigurationButton,
    SonolusConfiguration,
    SonolusIcon,
    SonolusText
)
from ..config import config_option
from api.sonolus.utils import get_profile
from api.locale import Localization, Language

# ---------------------------------------------------------------

@sonolus.server.server_info(SonolusServerInfo)
async def server_info(ctx: SonolusContext) -> SonolusServerInfo:
    """
    GET /sonolus/info
    """
    try:
        lang = Language(ctx.localization)
        localization = Localization(lang=lang)
    except ValueError:
        lang = Language.ENGLISH
        localization = Localization(lang=lang)
    
    profile = get_profile(ctx, sonolus)
    
    title = localization.get("sonolus.title", "UntitledSekaiρ")
    description = title

    if profile:
        description = f"{title}\n\n{profile.name}#{profile.handle}"

    return SonolusServerInfo(
        title=title,
        description=description,
        buttons=[
            ServerInfoAuthenticationButton(type="authentication"),
            ServerInfoItemButton(
                type="post",
                title=SonolusText.ANNOUNCEMENT,
                icon=SonolusIcon.Announcement,
                infoType="announcement",
            ),
            ServerInfoItemButton(type="level"),
            ServerInfoItemButton(type='background'),
            ServerInfoItemButton(type='effect'),
            ServerInfoItemButton(type='skin'),
            ServerInfoItemButton(type='particle'),
            ServerInfoItemButton(type='engine'),
            ServerInfoConfigurationButton(type='configuration'),
        ],
        configuration=SonolusConfiguration(
            options=config_option
        ),
        banner=None
    )