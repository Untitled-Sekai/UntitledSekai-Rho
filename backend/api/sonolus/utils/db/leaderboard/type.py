from pydantic import BaseModel

class Leaderboard_info(BaseModel):
    subtitle: str

    score: int
    accuracy_score: int
    rank: str

    perfect_count: int
    great_count: int
    good_count: int
    miss_count: int