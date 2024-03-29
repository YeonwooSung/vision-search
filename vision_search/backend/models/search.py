from pydantic import BaseModel


class Metadata(BaseModel):
    path: str
    score: float


class SearchResult(BaseModel):
    results: list[Metadata]


class TextQueryData(BaseModel):
    query: str
