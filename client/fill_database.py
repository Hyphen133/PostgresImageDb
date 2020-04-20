from client.query_base import QueryBase


class FillDataQuery(QueryBase):
    def __init__(self, id) -> None:
        super().__init__()
        self.id = id

    def execute_query(self):
        self.cursor.execute(fillData, self.id)

        return self.cursor.fetchall()

    @staticmethod
    def create_query(id, query):
        return FillDataQuery(id, query)


fillData = """ SELECT name FROM public."Tag" """


