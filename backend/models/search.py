from pydantic import BaseModel


class Metadata(BaseModel):
    path: str
    score: float


class SearchResult(BaseModel):
    results: list[Metadata]
    request_id: str

class ElasticSearchResult(BaseModel):
    hits: list[dict]
    request_id: str

class TextQueryData(BaseModel):
    query: str


class PostgresSearchResult(BaseModel):
    results: list[Metadata]
    request_id: str
