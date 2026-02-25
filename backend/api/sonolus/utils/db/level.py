from db.models import Level
from sqlalchemy.orm import Session
from typing import List

def get_level_by_name(
    db: Session,
    name: str
) -> Level | None:
    """
    レベル名からDBのレコードを取得する
    """
    return db.query(Level).filter(Level.name == name).first()

def get_search_levels_return_names(
    db: Session,
    keywords: str | None = None,
    title: str | None = None,
    author: str | None = None,
    minrating: float | None = None,
    maxrating: float | None = None,
    offset: int = 0,
    limit: int = 20
) -> tuple[List[str], int]:
    """
    レベルの検索結果を、nameのリストとして検索順に取得し、返す
    """
    query = db.query(Level)

    if keywords:
        for keyword in keywords.split():
            query = query.filter(
                (Level.name.contains(keyword)) |
                (Level.title.contains(keyword)) |
                (Level.author_handle.contains(keyword)) |
                (Level.author_name.contains(keyword))
            )
    
    if title:
        query = query.filter(Level.title.contains(title))
    
    if author:
        query = query.filter(
            (Level.author_handle.contains(author)) |
            (Level.author_name.contains(author))
        )
    
    if minrating is not None:
        query = query.filter(Level.rating >= minrating)
    
    if maxrating is not None:
        query = query.filter(Level.rating <= maxrating)

    total_count: int = query.count() # ここですべての条件を満たすレコード数を取得しておく
    query = query.offset(offset).limit(limit) # ページネーションのため、ここでクエリにoffsetとlimitを適用する
    names = [level.name for level in query.all()] # クエリを実行して、条件を満たすレコードのnameをリストとして取得する
    
    return names, total_count