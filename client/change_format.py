import io

import psycopg2
from PIL import Image

from client.config import config
from client.query_base import QueryBase
from client.read_image import ImageReadQuery


class ChangeFormatQuery(QueryBase):
    def __init__(self, image,id, target_format_extension, target_format_name) -> None:
        super().__init__()
        self.id = id
        self.image = image
        self.target_format_extension = target_format_extension
        self.target_format_name = target_format_name

    def execute_query(self):
        super().execute_query()
        new_blob = self.image_to_byte_array(self.image, self.target_format_name)
        self.cursor.execute(""" UPDATE public."Image"
                                SET  image=%s, format=%s
                                WHERE id=%s; """,
                            (psycopg2.Binary(new_blob), self.target_format_extension, self.id))
        self.connection.commit()

    def image_to_byte_array(self,image, target_format):
        imgByteArr = io.BytesIO()
        image.save(imgByteArr, format=target_format)
        imgByteArr = imgByteArr.getvalue()
        return imgByteArr

    @staticmethod
    def create_query(image,id, target_format_extension, target_format_name):
        return ChangeFormatQuery(image,id, target_format_extension, target_format_name)
