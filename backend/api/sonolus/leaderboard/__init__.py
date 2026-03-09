from api.locale import Localization
from sonolus_models import ServerItemLeaderboard
from typing import List

def build_leaderboard(localization: Localization) -> List[ServerItemLeaderboard]:
    """
    リーダーボード情報を構築する関数
    """
    return [
        ServerItemLeaderboard(
            name="grade-judgment-accuracy",
            title=localization.get("sonolus.leaderboard.grade-judgment-accuracy")
        ),
        ServerItemLeaderboard(
            name="grade-accuracy",
            title=localization.get("sonolus.leaderboard.grade-accuracy")
        ),
        ServerItemLeaderboard(
            name="judgment-accuracy",
            title=localization.get("sonolus.leaderboard.judgment-accuracy")
        ),
        ServerItemLeaderboard(
            name="arcade-accuracy",
            title=localization.get("sonolus.leaderboard.arcade-accuracy")
        ),
        ServerItemLeaderboard(
            name="accuracy",
            title=localization.get("sonolus.leaderboard.accuracy")
        )
    ]