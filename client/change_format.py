import io

import psycopg2
from PIL import Image

from client.config import config
from client.query_base import QueryBase
from client.read_image import ImageReadQuery


class ChangeFormatQuery(QueryBase):
    def __init__(self, id, target_format) -> None:
        super().__init__()
        self.id = id
        self.target_format = target_format

    def execute_query(self):
        super().execute_query()
        new_blob = self.change_format(id, self.target_format)
        self.cursor.execute(""" UPDATE public."Image"
                                SET  image=%s, format=%s
                                WHERE id=%s; """,
                            (psycopg2.Binary(new_blob), self.target_format, self.id))
        self.connection.commit()

    def change_format(self, id, target_format):
        blob = ImageReadQuery.create_query(id).execute()
        blob_img = Image.open(io.BytesIO(blob))
        return self.change_format_in_memory(blob_img, target_format)

    def change_format_in_memory(self, im, format):
        with io.BytesIO() as f:
            im.save(f, format=format)
            return f.getvalue()

    @staticmethod
    def create_query(id, target_format):
        return ChangeFormatQuery(id, target_format)
