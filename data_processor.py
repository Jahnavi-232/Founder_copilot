def process_deals(board_data):
    deals = []

    for board in board_data["boards"]:
        for item in board["items_page"]["items"]:

            deal = {
                "name": item["name"],
                "id": item["id"]
            }

            for column in item["column_values"]:
                if column["id"] == "text_mm5fm7w1":
                    deal["owner"] = column["text"]

                elif column["id"] == "text_mm5f885d":
                    deal["client"] = column["text"]

                elif column["id"] == "text_mm5f19r3":
                    deal["value"] = column["text"]

                elif column["id"] == "color_mm5f5dg4":
                    deal["stage"] = column["text"]

                elif column["id"] == "text_mm5ftwf6":
                    deal["sector"] = column["text"]

            deals.append(deal)

    return deals