import sys
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
import traceback

# Add the root directory to the path so that we can import the settings
sys.path.append("..")

from backend.server.app import init_app
from backend.utils import Logger
from backend.api.search import search_router

app: FastAPI = init_app(use_cors=True, cors_headers=["*"], cors_methods=["*"], cors_origins=["*"])
logger = Logger()

# add API routers
app.include_router(search_router, prefix="/api/search")


#
# exception handling
#

@app.exception_handler(Exception)
async def exception_handler(request, exc):
    # log the traceback and return 500
    logger.log_error(f"method={request.method} | {request.url} | {request.state.request_id} | 500 | details: {traceback.format_exc()}")
    return {"detail": "Internal Server Error"}, 500

@app.exception_handler(StarletteHTTPException)
async def starlette_http_exception_handler(request, exc):
    await log_http_exception(request, exc)
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    await log_http_exception(request, exc)
    return {"detail": exc.detail}, exc.status_code

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    exc.detail = exc.errors()
    await log_http_exception(request, exc)
    return {"detail": exc.detail}, 400

async def log_http_exception(request, exc):
    logger.log_warning(f"method={request.method} | {request.url} | {request.state.request_id} | {exc.status_code} | details: {exc.detail}")


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", reload=True)
