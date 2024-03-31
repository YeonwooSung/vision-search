from fastapi import APIRouter, UploadFile, HTTPException, Request, Form, status

# custom modules
from backend.api.utils.image_parse import load_image_into_numpy_array
from backend.engine.v1 import get_engine
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


@r.post("/query/image")
async def search_by_image(
    request: Request,
    img_file: UploadFile = Form(...),
):
    req_id = request.state.request_id

    # validate image
    if img_file.content_type not in ['image/png', 'image/jpeg', 'image/jpg']:
        logger.log_warning(f'Invalid image: image type is not supported: image="{img_file.filename}"')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid image: image type is not supported")

    image = load_image_into_numpy_array(await img_file.read())
    # extract features
    features = engine.arun_engine(image)

    #TODO search images via vector similarity
    results = []

    # return the search results
    return SearchResult(results=results, req_id=req_id)
