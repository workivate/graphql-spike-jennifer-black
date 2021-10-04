from dataclasses import dataclass
from typing import Optional


@dataclass
class SearchRequest:
    query: str
    limit: Optional[int]
    cursor: Optional[str]
