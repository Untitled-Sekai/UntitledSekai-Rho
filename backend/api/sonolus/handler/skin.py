from ...instance import sonolus
from sonolus_models import ServerItemInfo, ServerItemList, ServerItemDetails, SkinSection, SonolusText

# --------------------------------------------------------------- 

@sonolus.skin.info(ServerItemInfo)
async def get_skin_info(ctx) -> ServerItemInfo:
    items = sonolus.items.skin.list()[:3]
    searches = []
    return ServerItemInfo(
        creates=[],
        searches=searches,
        sections=[
            SkinSection(
                title=SonolusText.NEWEST,
                items=items,
            )
        ],
        banner=None
    )

# --------------------------------------------------------------- 
    
@sonolus.skin.list(ServerItemList)
async def list_skins(ctx, query) -> ServerItemList:
    items = sonolus.items.skin.list()
    return ServerItemList(
        pageCount=1,
        items=items,
        searches=[]
    )

# --------------------------------------------------------------- 
    
@sonolus.skin.detail(ServerItemDetails)
async def get_skin_details(ctx, name: str) -> ServerItemDetails:
    item = sonolus.items.skin.get(name)
    return ServerItemDetails(
        item=item,
        description=item.subtitle,
        actions=[],
        leaderboards=[],
        sections=[],
        hasCommunity=False
    )