from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
    status,
)

# custom modules
from backend.engine import get_engine
from backend.engine.threadpool_executor import MultimodalThreadPoolEngine
from backend.searcher.pg_base_searcher import PostgresBaseSearcher
from backend.models.search import TextQueryData, PostgresSearchResult
from backend.utils import Logger


logger = Logger()

# Create a router for the search endpoint
search_router = r = APIRouter()


@r.post("/query/text")
async def search_by_text(
    request: Request,
    data: TextQueryData,
    engine: MultimodalThreadPoolEngine = Depends(get_engine),
    searcher: PostgresBaseSearcher = Depends(PostgresBaseSearcher),
):
    req_id = request.state.request_id

    query = data.query
    if not query or len(query) < 3:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Query must be at least 3 characters long")

    # search images by using text embeddings
    query_features = await engine.arun_engine_with_text(query)
    results = searcher.knn_search(query_features, k=10)

    # return the search results
    return PostgresSearchResult(results=results, request_id=req_id)
