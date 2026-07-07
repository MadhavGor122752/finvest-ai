from fastapi import FastAPI
from app.authentication.routes import router as auth_router
from app.core.config import settings
from app.profile.routes import router as profile_router
from app.market.routes import router as market_router
from app.mutual_fund.routes import router as mutual_fund_router
from app.sip.routes import router as sip_router
from app.portfolio.routes import router as portfolio_router    
from app.transaction.routes import router as transaction_router
from app.sip.routes import router as sip_router
from app.recommendation.routes import router as recommendation_router
from app.dashboard.routes import router as dashboard_router
app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="AI-Powered Wealth Management Platform",
)

app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(market_router)
app.include_router(mutual_fund_router)
app.include_router(sip_router)
app.include_router(portfolio_router)
app.include_router(transaction_router)
app.include_router(sip_router)
app.include_router(recommendation_router)
app.include_router(dashboard_router)
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