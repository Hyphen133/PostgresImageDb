from client.query_base import QueryBase


class SelectQuery(QueryBase):
    def __init__(self, query) -> None:
        super().__init__()
        self.query = query

    def execute_query(self):
        self.cursor.execute(self.query)

        return self.cursor.fetchall()

    @staticmethod
    def create_query(query):
        return SelectQuery(query)


selectTags = """ SELECT name FROM public."Tag" """
selectDatasets = """ SELECT name FROM public."Dataset" """


