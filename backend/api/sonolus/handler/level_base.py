from ...instance import sonolus
from fastapi import HTTPException, status
from sonolus_fastapi.utils.context import SonolusContext
from sonolus_models import (
    ServerItemInfo,
    ServerItemList,
    ServerItemDetails
)

# --------------------------------------------------------------- 

@sonolus.level.info(ServerItemInfo)
async def level_info(ctx: SonolusContext) -> ServerItemInfo:
    """
    GET /sonolus/levels/info
    """
    return ServerItemInfo(
        creates=[],
        searches=[sonolus.search.level],
        sections=[],
        banner=None
    )

# ---------------------------------------------------------------

@sonolus.level.list(ServerItemList)
async def level_list(ctx: SonolusContext, query) -> ServerItemList:
    """
    GET /sonolus/levels/list
    """
    return ServerItemList(
        pageCount=1,
        items=[],
        searches=[sonolus.search.level]
    )

# ---------------------------------------------------------------

@sonolus.level.details(ServerItemDetails)
async def level_details(ctx: SonolusContext, name: str) -> ServerItemDetails:
    """
    GET /sonolus/levels/{name}
    """
    # TODO: DBを宣言して、そこからdescriptionを取得するようにする
    # 現在はdescriptionは空文字列で返すようにしている
    # また、dbを参照してnameが存在しない場合は404を返すようにする
     
    item = sonolus.items.level.get(name)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Level not found")
    
    return ServerItemDetails(
        item=item,
        description="",
        actions=[],
        leaderboards=[],
        sections=[],
        hasCommunity=True,
    )