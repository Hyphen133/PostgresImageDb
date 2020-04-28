import sys

from PIL import Image

from client.change_format import ChangeFormatQuery
from client.read_image import ImageReadQuery, save_image_from_bytes_locally
from client.select_tags import SelectQuery, selectImages

format = sys.argv[1]

format_name = sys.argv[2]

ids = SelectQuery.create_query(selectImages).execute()

for id in ids:
    image_bytes = ImageReadQuery.create_query(id).execute()
    save_image_from_bytes_locally(image_bytes, "temp.png")
    image = Image.open("temp.png")
    ChangeFormatQuery.create_query(image,id,format,format_name).execute()