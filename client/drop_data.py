from client.query_base import QueryBase


class DropDataQuery(QueryBase):
    def __init__(self) -> None:
        super().__init__()

    def execute_query(self):
        self.cursor.execute(dropDataTag)
        self.cursor.execute(dropDataImage)
        self.cursor.execute(dropDataDataset)
        self.cursor.execute(dropDataImageDataset)
        self.cursor.execute(dropDataImageTag)


    @staticmethod
    def create_query():
        return DropDataQuery()


dropDataTag = """ DELETE FROM public."Tag" """
dropDataImage = """ DELETE FROM public."Image" """
dropDataDataset = """ DELETE FROM public."Dataset" """
dropDataImageDataset = """ DELETE FROM public."ImageDataset" """
dropDataImageTag = """ DELETE FROM public."ImageTag" """


