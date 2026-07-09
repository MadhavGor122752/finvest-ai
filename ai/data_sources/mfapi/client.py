import httpx


class MFAPIClient:

    BASE_URL = "https://api.mfapi.in/mf"

    def get_scheme_list(self):

        response = httpx.get(
            self.BASE_URL,
            timeout=60,
        )

        response.raise_for_status()

        return response.json()

    def get_scheme_history(
        self,
        scheme_code: int,
    ):

        response = httpx.get(
            f"{self.BASE_URL}/{scheme_code}",
            timeout=60,
        )

        response.raise_for_status()

        return response.json()