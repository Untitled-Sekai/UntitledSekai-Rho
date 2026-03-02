from db.models import Level_Readerboard, Level
from sqlalchemy.orm import Session
from typing import List

# score: 全体的なスコア
# accuracy_score: 精度スコア
# rank: AP / FC / Pass / Failのランク
# perfect_count, great_count, good_count, miss_count: 各ノートの判定数
# cleared_at: クリア日時

# これらで、レベルのリーダーボードの順位、ページネーションなどを実装する。
# ここのみSonolusFastAPIに依存しない。
# ここを依存すると、ランキングの順位を出す部分が非常に書きづらくなるため、自前にし、動的に順位を出すようにする。

