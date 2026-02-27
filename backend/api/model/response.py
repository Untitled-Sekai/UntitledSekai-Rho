from pydantic import BaseModel
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class ResponseModel(BaseModel):
    """
    基本的なレスポンス形
    data を持たない汎用レイアウト。
    """
    success: bool
    message: Optional[str] = None


class DataResponseModel(BaseModel, Generic[T]):
    """
    継承ではなくジェネリックを使うことで、エンドポイントごとに
    レスポンスデータ型を指定できる。
    """
    success: bool
    data: Optional[T] = None
    message: Optional[str] = None