import psycopg2

from client.config import config
from client.query_base import QueryBase


class ImageWriteQuery(QueryBase):
    def __init__(self, id, image_path, format) -> None:
        super().__init__()
        self.id = id
        self.image = open(image_path, 'rb').read()
        self.format = format

    def execute_query(self):
        self.cursor.execute("""
                    INSERT INTO public."Image"(id,image,format)
                    VALUES(%s,%s,%s)""",
                            (self.id, psycopg2.Binary(self.image), self.format))

        self.connection.commit()

    @staticmethod
    def create_query(id, image,format):
        return ImageWriteQuery(id,image,format)

