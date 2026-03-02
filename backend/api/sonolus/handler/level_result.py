from fastapi import HTTPException, status
from ...instance import sonolus
from api.sonolus.result.level import level_result, ServerUploadLevelResultResponse
from sonolus_fastapi.utils.context import SonolusContext
from sonolus_models import (
    ServerLevelResultInfo,
    ServerSubmitLevelResultResponse,
    ServerSubmitLevelResultRequest,
)
from api.sonolus.utils import get_profile
from api.sonolus.utils.db.leaderboard import sort_leaderboard_entries, Leaderboard_info
from db.session import get_db_session
from db.models import Level_Readerboard
from sqlalchemy.orm import Session

# ---------------------------------------------------------------

@sonolus.level.result_info(ServerLevelResultInfo)
async def level_result_info(ctx: SonolusContext) -> ServerLevelResultInfo:
    """
    GET /sonolus/levels/result/info
    """
    return ServerLevelResultInfo(
        submits=[level_result]
    )

# ---------------------------------------------------------------

@sonolus.level.result_submit(ServerSubmitLevelResultResponse)
async def level_result_submit(ctx: SonolusContext, request: ServerSubmitLevelResultRequest) -> ServerSubmitLevelResultResponse:
    """
    POST /sonolus/levels/result/submit
    """
    profile = get_profile(ctx=ctx, sonolus=sonolus)
    if not profile:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    
    replay_item = request.replay
    if not replay_item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Replay data is required")
    
    subtitle = replay_item.subtitle
    leaderboard_info = sort_leaderboard_entries(subtitle)
    hashes = [
        replay_item.data.hash,
        replay_item.configuration.hash
    ]
    id = f"{replay_item.name}_{hashes[0]}"

    with get_db_session() as db:
        db: Session
        leaderboard_record = Level_Readerboard(
            id=id,
            hash=hashes[0],
            level_name=replay_item.level.name,
            player_handle=profile.handle,
            subtitle=subtitle,
            score=leaderboard_info.score,
            accuracy_score=leaderboard_info.accuracy_score,
            rank=leaderboard_info.rank,
            perfect_count=leaderboard_info.perfect_count,
            great_count=leaderboard_info.great_count,
            good_count=leaderboard_info.good_count,
            miss_count=leaderboard_info.miss_count
        )
        db.add(leaderboard_record)
        db.commit()
    
    return ServerSubmitLevelResultResponse(
        key=id,
        hashes=hashes
    )

# ---------------------------------------------------------------

@sonolus.level.result_upload(ServerUploadLevelResultResponse)
async def level_result_upload(ctx: SonolusContext, upload_key: str, files: list) -> ServerUploadLevelResultResponse:
    """
    POST /sonolus/levels/result/upload
    """
    for i, file in enumerate(files):
        content = await file.read()
        file_type = "data" if i == 0 else "configuration"
