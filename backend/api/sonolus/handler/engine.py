from ...instance import sonolus
from sonolus_models import ServerItemInfo, ServerItemList, ServerItemDetails, EngineSection, SonolusText

# --------------------------------------------------------------- 

@sonolus.engine.info(ServerItemInfo)
async def get_engine_info(ctx) -> ServerItemInfo:
    items = sonolus.items.engine.list()[:3]
    searches = []
    return ServerItemInfo(
        creates=[],
        searches=searches,
        sections=[
            EngineSection(
                title=SonolusText.NEWEST,
                items=items,
            )
        ],
        banner=None
    )

# --------------------------------------------------------------- 
    
@sonolus.engine.list(ServerItemList)
async def list_engines(ctx, query) -> ServerItemList:
    items = sonolus.items.engine.list()
    return ServerItemList(
        pageCount=1,
        items=items,
        searches=[]
    )

# --------------------------------------------------------------- 
    
@sonolus.engine.detail(ServerItemDetails)
async def get_engine_details(ctx, name: str) -> ServerItemDetails:
    item = sonolus.items.engine.get(name)
    return ServerItemDetails(
        item=item,
        description=item.subtitle,
        actions=[],
        leaderboards=[],
        sections=[],
        hasCommunity=False
    )