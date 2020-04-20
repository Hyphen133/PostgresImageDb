from client.query_base import QueryBase


class DropDataQuery(QueryBase):
    def __init__(self, id) -> None:
        super().__init__()
        self.id = id

    def execute_query(self):
        self.cursor.execute(dropDataTag, self.id)
        self.cursor.execute(dropDataImage, self.id)
        self.cursor.execute(dropDataDataset, self.id)
        self.cursor.execute(dropDataImageDataset, self.id)
        self.cursor.execute(dropDataImageTag, self.id)


    @staticmethod
    def create_query(id, query):
        return DropDataQuery(id, query)


dropDataTag = """ DELETE * FROM public."Tag" """
dropDataImage = """ DELETE * FROM public."Image" """
dropDataDataset = """ DELETE * FROM public."Dataset" """
dropDataImageDataset = """ DELETE * FROM public."ImageDataset" """
dropDataImageTag = """ DELETE * FROM public."ImageTag" """


