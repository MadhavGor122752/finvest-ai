from pydantic import BaseModel


class AdminDashboardResponse(BaseModel):
    total_users: int
    total_profiles: int
    total_sips: int
    total_transactions: int