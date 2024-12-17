
# FastAPI Imports
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

# Config Imports
from config import settings

# Mangum
from mangum import Mangum

# Modules
from modules.categorizor import categorize_content

# Constants
from modules.constants import API_PREFIX

# API Types
from modules.api_types import ContentRequestBody, ContentResponseBody


# @asynccontextmanager
# async def lifespan(app: FastAPI):

#     # load_dotenv()

#     yield

# Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.BACKEND_CORS_ORIGINS,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    debug=settings.DEBUG,
)

router = APIRouter(prefix=API_PREFIX)


@router.get("/")
async def root():
    return {"message": "Hello from fastapi-lambda-test-deploy!"}


@router.get("/health")
async def health_check():
    return {"status": "healthy"}


@router.post("/categorize")
async def categorize(content: ContentRequestBody):
    return await categorize_content(content)


if settings.ENVIRONMENT != 'development':
    app = Mangum(app)


app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
