from pydantic import BaseModel
from typing import (
    Generic,
    TypeVar,
    List,
    Optional
)

T = TypeVar("T")


class ResponseBaseSchema(BaseModel, Generic[T]):
    count: Optional[int] = 0
    next: Optional[str] = None
    result: Optional[List[T]] = []
