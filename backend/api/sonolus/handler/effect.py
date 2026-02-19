from ...instance import sonolus
from sonolus_models import ServerItemInfo, ServerItemList, ServerItemDetails, EffectSection, SonolusText

# --------------------------------------------------------------- 

@sonolus.effect.info(ServerItemInfo)
async def get_effect_info(ctx) -> ServerItemInfo:
    items = sonolus.items.effect.list()[:3]
    searches = []
    return ServerItemInfo(
        creates=[],
        searches=searches,
        sections=[
            EffectSection(
                title=SonolusText.NEWEST,
                items=items,
            )
        ],
        banner=None
    )
    
# --------------------------------------------------------------- 

@sonolus.effect.list(ServerItemList)
async def list_effects(ctx, query) -> ServerItemList:
    items = sonolus.items.effect.list()
    return ServerItemList(
        pageCount=1,
        items=items,
        searches=[]
    )

# --------------------------------------------------------------- 
    
@sonolus.effect.detail(ServerItemDetails)
async def get_effect_details(ctx, name: str) -> ServerItemDetails:
    item = sonolus.items.effect.get(name)
    return ServerItemDetails(
        item=item,
        description=item.subtitle,
        actions=[],
        leaderboards=[],
        sections=[],
        hasCommunity=False
    )