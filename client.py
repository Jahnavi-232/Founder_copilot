import requests
from config import MONDAY_API_TOKEN, MONDAY_API_URL


class MondayClient:
    def __init__(self):
        self.url = MONDAY_API_URL
        self.headers = {
            "Authorization": MONDAY_API_TOKEN,
            "Content-Type": "application/json",
        }

    def execute_query(self, query: str):
        """Execute a GraphQL query against Monday.com."""

        response = requests.post(
            self.url,
            json={"query": query},
            headers=self.headers,
            timeout=30,
        )

        if response.status_code != 200:
            raise Exception(
                f"Monday API Error {response.status_code}: {response.text}"
            )

        data = response.json()

        if "errors" in data:
            raise Exception(data["errors"])

        return data["data"]

    # 👇 ADD THIS NEW METHOD
    def execute_query_with_variables(self, query: str, variables: dict):
        """Execute a GraphQL query with variables."""

        response = requests.post(
            self.url,
            json={
                "query": query,
                "variables": variables
            },
            headers=self.headers,
            timeout=30,
        )

        if response.status_code != 200:
            raise Exception(
                f"Monday API Error {response.status_code}: {response.text}"
            )

        result = response.json()

        if "errors" in result:
            raise Exception(result["errors"])

        return result["data"]