import psycopg2

from client.config import config
from client.query_base import QueryBase


class ImageReadQuery(QueryBase):
    def __init__(self, id) -> None:
        super().__init__()
        self.id = id

    def execute_query(self):
        self.cursor.execute(""" SELECT image
                                FROM public."Image"
                                WHERE id = %s """,
                    (self.id,))

        return self.cursor.fetchone()[0].tobytes()

    @staticmethod
    def create_query(id):
        return ImageReadQuery(id)


def save_image_from_bytes_locally(image_bytes, out_filepath):
    open(out_filepath, 'wb').write(image_bytes)


