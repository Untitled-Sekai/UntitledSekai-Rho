from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey, JSON, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import TypeDecorator
from typing import Optional
from datetime import datetime, timezone
from sonolus_models import ServiceUserProfile
from pydantic import ValidationError

Base = declarative_base()


class PydanticJSONType(TypeDecorator):
    """PydanticモデルをサポートするカスタムJSON型"""
    impl = JSON
    cache_ok = True

    def __init__(self, pydantic_type):
        super().__init__()
        self.pydantic_type = pydantic_type

    def process_bind_param(self, value, dialect):
        """Pydanticモデル → JSON"""
        if value is None:
            return None
        if isinstance(value, self.pydantic_type):
            return value.dict(by_alias=True)
        return value

    def process_result_value(self, value, dialect):
        """JSON → Pydanticモデル（バリデーション付き）"""
        if value is None:
            return None
        try:
            return self.pydantic_type(**value)
        except ValidationError as e:
            raise ValueError(f"Invalid {self.pydantic_type.__name__}: {e}")

class User(Base):
    __tablename__ = 'users'

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    profile: Mapped[Optional[ServiceUserProfile]] = mapped_column(PydanticJSONType(ServiceUserProfile), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

class Level(Base):
    __tablename__ = 'levels'

    name: Mapped[str] = mapped_column(String, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    author_handle: Mapped[str] = mapped_column(String, nullable=False)
    author_name: Mapped[str] = mapped_column(String, nullable=False)

    rating: Mapped[float] = mapped_column(Float, nullable=True)

    difficulty: Mapped[str] = mapped_column(String, nullable=False)
    genre: Mapped[str] = mapped_column(String, nullable=False)

    uploaded_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc)) # アップロード日時はレコード作成時に自動で設定されるため、defaultを指定する
    published_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True) # 公開日時は後から設定される可能性があるため、nullable=Trueとする

class Level_Like(Base):
    __tablename__ = 'level_likes'
    __table_args__ = (
        UniqueConstraint('level_name', 'liked_by_handle', name='uq_level_like'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    level_name: Mapped[str] = mapped_column(String, ForeignKey('levels.name'), nullable=False)
    liked_by_handle: Mapped[str] = mapped_column(String, nullable=False)
    liked_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))