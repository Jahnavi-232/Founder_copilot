from monday.client import MondayClient
from monday.queries import GET_BOARD_ITEMS
from config import DEALS_BOARD_ID, WORK_ORDERS_BOARD_ID


class BoardService:
    def __init__(self):
        self.client = MondayClient()

    def get_deals(self):
        return self.client.execute_query_with_variables(
            GET_BOARD_ITEMS,
            {"boardId": DEALS_BOARD_ID}
        )

    def get_work_orders(self):
        return self.client.execute_query_with_variables(
            GET_BOARD_ITEMS,
            {"boardId": WORK_ORDERS_BOARD_ID}
        )