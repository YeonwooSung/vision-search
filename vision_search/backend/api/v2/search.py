from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    HTTPException,
    Request,
    Form,
    status,
)

# custom modules
from backend.api.utils.image_parse import load_image_into_numpy_array
from backend.engine.v1 import get_engine
from backend.searcher.es_base_searcher import ElasticBaseSearcher
from backend.models.search import SearchResult, TextQueryData
from backend.utils import Logger


logger = Logger()
engine = get_engine()

# Create a router for the search endpoint
search_router = r = APIRouter()


@r.post("/query/text")
async def search_by_text(
    request: Request,
    data: TextQueryData,
    searcher: ElasticBaseSearcher = Depends(ElasticBaseSearcher),
):
    req_id = request.state.request_id

    query = data.query
    if not query or len(query) < 3:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Query must be at least 3 characters long")

    # search images by full text search via metadata in the database
    #TODO: implement the search logic here
    results = []

    # return the search results
    return SearchResult(results=results, req_id=req_id)
