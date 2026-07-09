from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class AdminDashboardResponse(BaseModel):
    total_users: int
    total_profiles: int
    total_sips: int
    total_transactions: int


class AdminUserResponse(BaseModel):
    id: UUID
    email: str
    role: str
    is_email_verified: bool

    class Config:
        from_attributes = True


class AdminUserListResponse(BaseModel):
    page: int
    limit: int
    total: int
    users: list[AdminUserResponse]


class AdminUserDetailResponse(BaseModel):
    id: UUID
    email: str
    role: str
    is_email_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AdminActionResponse(BaseModel):
    message: str