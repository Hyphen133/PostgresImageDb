import random

from client.change_format import ChangeFormatQuery
from client.read_image import save_image_from_bytes_locally, ImageReadQuery
from client.write_image import ImageWriteQuery

id = str(random.getrandbits(60))

ImageWriteQuery.create_query(id, "test_images/lenna.png", ".png").execute()
image_bytes = ImageReadQuery.create_query(id).execute()
save_image_from_bytes_locally(image_bytes, "out.png")
ChangeFormatQuery.create_query(id,"jpg").execute()