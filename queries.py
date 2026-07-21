# Get all boards
GET_BOARDS = """
{
    boards {
        id
        name
    }
}
"""

# Get all items from a specific board
GET_BOARD_ITEMS = """
query ($boardId: [ID!]) {
  boards(ids: $boardId) {
    id
    name

    columns {
      id
      title
      type
    }

    items_page {
      items {
        id
        name

        column_values {
          id
          text
          value
        }
      }
    }
  }
}
"""