from pydantic import BaseModel


class MutualFundResponse(BaseModel):
    scheme_code: int
    scheme_name: str


class MutualFundDetailResponse(BaseModel):
    scheme_code: int
    scheme_name: str
    fund_house: str
    category: str
    risk_level: str
    expense_ratio: float
    nav: float