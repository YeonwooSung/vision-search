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
from backend.models.search import ElasticSearchResult
from backend.utils import Logger


logger = Logger()
engine = get_engine()

# Create a router for the search endpoint
search_router = r = APIRouter()


@r.post("/query/image")
async def search_by_image(
    request: Request,
    img_file: UploadFile = Form(...),
    searcher: ElasticBaseSearcher = Depends(ElasticBaseSearcher),
):
    req_id = request.state.request_id

    # validate image
    if img_file.content_type not in ['image/png', 'image/jpeg', 'image/jpg']:
        logger.log_warning(f'Invalid image: image type is not supported: image="{img_file.filename}"')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid image: image type is not supported")

    image = load_image_into_numpy_array(await img_file.read())
    # extract features
    features = engine.arun_engine(image)

    # search images via vector similarity
    response = searcher.knn_search(features, k=10)
    results = response["hits"]["hits"]

    # return the search results
    return ElasticSearchResult(hits=results, request_id=req_id)
