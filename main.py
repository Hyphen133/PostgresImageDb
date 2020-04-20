import random
import time

from PIL import Image

from client.change_format import ChangeFormatQuery
from client.drop_data import DropDataQuery
from client.fill_database import FillDataQuery
from client.read_image import save_image_from_bytes_locally, ImageReadQuery
from client.select_function import SelectQuery, selectAllTagsForDataset
from client.write_image import ImageWriteQuery

id = str(random.getrandbits(60))
DropDataQuery.create_query().execute()
FillDataQuery.create_query().execute()



# ImageWriteQuery.create_query(id, "test_images/lenna.png", ".png").execute()
# image_bytes = ImageReadQuery.create_query(id).execute()
# save_image_from_bytes_locally(image_bytes, "out.png")
# image = Image.open("out.png")
# ChangeFormatQuery.create_query(image,id,".spi","SPIDER").execute()
# print(SelectQuery.create_query(id, selectAllTagsForDataset).execute())
