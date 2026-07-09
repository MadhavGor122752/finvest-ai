import httpx

from app.core.config import settings


class MutualFundAPIClient:

    def __init__(self):
        self.base_url = settings.MF_API_BASE_URL

    def get_all_funds(self):

        response = httpx.get(
            self.base_url,
            timeout=30.0,
        )

        response.raise_for_status()

        return response.json()

    def get_fund_details(
        self,
        scheme_code: int,
    ):

        response = httpx.get(
            f"{self.base_url}/{scheme_code}",
            timeout=30.0,
        )

        response.raise_for_status()

        return response.json()