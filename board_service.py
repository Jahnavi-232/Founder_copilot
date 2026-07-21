from monday.client import MondayClient
from queries import DEALS_QUERY


class BoardService:

    def __init__(self):
        self.client = MondayClient()


    def get_deals(self):

        response = self.client.query(DEALS_QUERY)

        try:

            items = (
                response
                ["data"]
                ["boards"][0]
                ["items_page"]
                ["items"]
            )

            deals = []

            for item in items:

                deal = {
                    "name": item["name"]
                }

                for column in item["column_values"]:
                    deal[column["id"]] = column["text"]

                deals.append(deal)


            return deals


        except Exception as e:
            print(response)
            raise e
