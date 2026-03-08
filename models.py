from pydantic import BaseModel
from typing import Optional

class Game(BaseModel):
    title: str
    genre: str
    platform: str
    rating: float
    released: int
    description: Optional[str] = None