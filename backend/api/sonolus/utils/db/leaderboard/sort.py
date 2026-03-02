from .type import Leaderboard_info

def sort_leaderboard_entries(subtitle: str) -> Leaderboard_info:
    """
    subtitleをもとに、スコアやランクなどを、切り離して返す関数
    """
    try:
        parts = subtitle.split('|')
        if len(parts) == 2:
            left_part = parts[0].strip().split()
        if len(left_part) == 3:
            rank = left_part[0]
            score = int(left_part[1])
            accuracy_score = int(left_part[2])

        right_part = parts[1].strip().split()
        if len(right_part) == 4:
            perfect_count = int(right_part[0])
            great_count = int(right_part[1])
            good_count = int(right_part[2])
            miss_count = int(right_part[3])
            
    except Exception as e:
        raise ValueError(f"Invalid subtitle format: {subtitle}. Error: {e}")

    return Leaderboard_info(
        subtitle=subtitle,
        score=score,
        accuracy_score=accuracy_score,
        rank=rank,
        perfect_count=perfect_count,
        great_count=great_count,
        good_count=good_count,
        miss_count=miss_count
    )