from ...instance import sonolus
from sonolus_models import ServerItemInfo, ServerItemList, ServerItemDetails, PostSection, SonolusText

# --------------------------------------------------------------- 

@sonolus.post.info(ServerItemInfo)
async def get_skin_info(ctx) -> ServerItemInfo:
    items = sonolus.items.post.list()[:3]
    searches = []
    return ServerItemInfo(
        creates=[],
        searches=searches,
        sections=[
            PostSection(
                title=SonolusText.NEWEST,
                items=items,
            )
        ],
        banner=None
    )

# --------------------------------------------------------------- 
    
@sonolus.post.list(ServerItemList)
async def list_posts(ctx, query) -> ServerItemList:
    items = sonolus.items.post.list()
    return ServerItemList(
        pageCount=1,
        items=items,
        searches=[]
    )

# --------------------------------------------------------------- 
    
@sonolus.post.detail(ServerItemDetails)
async def get_post_details(ctx, name: str) -> ServerItemDetails:
    item = sonolus.items.post.get(name)
    return ServerItemDetails(
        item=item,
        description=item.description,
        actions=[],
        leaderboards=[],
        sections=[],
        hasCommunity=False
    )