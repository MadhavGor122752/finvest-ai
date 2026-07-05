from fastapi import FastAPI
from app.authentication.routes import router as auth_router
from app.core.config import settings
from app.profile.routes import router as profile_router

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="AI-Powered Wealth Management Platform",
)

app.include_router(auth_router)
app.include_router(profile_router)
@app.get("/", tags=["Health"])
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "status": "running",
        "version": "1.0.0",
    }


@app.get("/health", tags=["Health"])

def health_check():
    return {
        "status": "healthy",
        "environment": settings.APP_ENV,
    }