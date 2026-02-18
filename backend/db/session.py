from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .models import Base
from typing import Generator
from contextlib import contextmanager
from pathlib import Path

data_dir = Path(__file__).parent.parent.parent.parent / "data"
data_dir.mkdir(exist_ok=True)

db_path = data_dir / "main.db"

engine = create_engine(
    f"sqlite:///{db_path.as_posix()}", # あとで、PostgreSQLに切り替えることも考慮して、SQLiteの接続URLを使用
    connect_args={"check_same_thread": False} # SQLiteで複数スレッドからアクセスするための設定
)

Base.metadata.create_all(engine)
sessionMaker = sessionmaker(engine, autocommit=False, autoflush=False)

def get_db() -> Generator[Session, None, None]:
    db = sessionMaker()
    try:
        yield db
    finally:
        db.close()

@contextmanager
def get_db_session() -> Generator:
    gen = get_db()
    session = next(gen)
    try:
        yield session
    finally:
        gen.close()