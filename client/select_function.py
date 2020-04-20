from client.query_base import QueryBase


class SelectQuery(QueryBase):
    def __init__(self, id, query) -> None:
        super().__init__()
        self.id = id
        self.query = query

    def execute_query(self):
        self.cursor.execute(self.query, self.id)

        return self.cursor.fetchall()

    @staticmethod
    def create_query(id, query):
        return SelectQuery(id, query)


selectAllTagsForDataset = """ SELECT name FROM public."Tag" """


