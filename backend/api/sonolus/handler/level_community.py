from ...instance import sonolus
from sonolus_fastapi.utils.context import SonolusContext
from sonolus_models import (
    ServerItemCommunityInfo,
    ServerSubmitItemCommunityActionResponse,
    ServerSubmitItemCommunityActionRequest,
    ServerItemCommunityComment,
    ServerItemCommunityCommentList
)
from api.sonolus.community.level import level_comment
from api.sonolus.utils import get_profile
from urllib.parse import parse_qs
from fastapi import HTTPException, status

import time
import math

# --------------------------------------------------------------- 

@sonolus.level.community.info(ServerItemCommunityInfo)
async def level_community_info(ctx: SonolusContext, name: str) -> ServerItemCommunityInfo:
    """
    GET /sonolus/levels/{name}/community/info
    """
    store = sonolus.items.level_comments.for_item(item_name=name)
    comments = store.list(limit= 3, offset=0)

    return ServerItemCommunityInfo(
        actions=[level_comment],
        topComments=comments
    )

# --------------------------------------------------------------- 

@sonolus.level.community.comments(ServerItemCommunityCommentList)
async def level_community_comments(ctx: SonolusContext, name: str, query) -> ServerItemCommunityCommentList:
    """
    GET /sonolus/levels/{name}/community/comments/list
    """
    page = int(query.get('page', 0))
    items_per_page = 20
    offset = page * items_per_page
    store = sonolus.items.level_comments.for_item(item_name=name)
    comments = store.list(limit=items_per_page, offset=offset)
    return ServerItemCommunityCommentList(
        pageCount=math.ceil(store.count() / items_per_page),
        comments=comments
    )

# --------------------------------------------------------------- 

@sonolus.level.community.actions(ServerSubmitItemCommunityActionResponse)
async def level_community_actions(ctx: SonolusContext, name: str, req:ServerSubmitItemCommunityActionRequest) -> ServerSubmitItemCommunityActionResponse:
    """
    POST /sonolus/levels/{name}/community/submit
    """
    profile = get_profile(ctx, sonolus)
    if profile == None:
        return HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)
    store = sonolus.items.level_comments.for_item(item_name=name)
    value = parse_qs(req['values'])
    comment_content = value.get('comment', [''])[0]
    comment_name = f"{name}_comment_{int(time.time * 1000)}"
    comment_time = int(time.time() * 1000)

    new_comment = ServerItemCommunityComment(
        name=comment_name,
        author=f"{profile.name}#{profile.handle}",
        time=comment_time,
        content=comment_content,
        actions=[]
    )
    store.add(new_comment)
    return ServerSubmitItemCommunityActionResponse(
        key=comment_name,
        hashes=[],
        shouldUpdateComments=True
    )