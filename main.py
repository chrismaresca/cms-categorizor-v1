from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings

# Mangum
from mangum import Mangum

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    debug=settings.DEBUG
)

# Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.BACKEND_CORS_ORIGINS,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/")
async def root():
    return {"message": "Hello from fastapi-lambda-test-deploy!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if settings.ENVIRONMENT != 'development':
    app = Mangum(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 