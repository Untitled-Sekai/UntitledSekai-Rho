import math

from ...instance import sonolus
from fastapi import HTTPException, status
from sonolus_fastapi.utils.context import SonolusContext
from sonolus_models import (
    ServerItemInfo,
    ServerItemList,
    ServerItemDetails
)
from api.sonolus.utils.db import get_level_by_name, get_search_levels_return_names
from db.session import get_db_session

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
    page = int(query.get("page", 0))
    keywords = query.get("keywords")
    title = query.get("title")
    author = query.get("author")
    minrating = int(query.get("minrating"))
    maxrating = int(query.get("maxrating"))

    items_per_page = 20
    page_count = math.ceil(total_count / items_per_page)

    with get_db_session() as db:
        level_names, total_count = get_search_levels_return_names(
            db=db,
            keywords=keywords,
            title=title,
            author=author,
            minrating=minrating,
            maxrating=maxrating,
            offset=page * items_per_page,
            limit=items_per_page
        )

    items = sonolus.items.level.get_many(level_names)

    return ServerItemList(
        pageCount=page_count,
        items=items,
        searches=[sonolus.search.level]
    )

# ---------------------------------------------------------------

@sonolus.level.detail(ServerItemDetails)
async def level_details(ctx: SonolusContext, name: str) -> ServerItemDetails:
    """
    GET /sonolus/levels/{name}
    """    
    with get_db_session() as db:
        level = get_level_by_name(db=db, name=name)
        if level is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Level not found")

    item = sonolus.items.level.get(name)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Level not found")
    
    return ServerItemDetails(
        item=item,
        description=level.description,
        actions=[],
        leaderboards=[],
        sections=[],
        hasCommunity=True,
    )