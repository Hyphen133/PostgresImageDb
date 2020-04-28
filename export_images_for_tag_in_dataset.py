import sys

from client.read_image import ImageReadQuery, save_image_from_bytes_locally
from client.select_images_for_tag_dataset import SelectImagesForTagsDatasetQuery

tag = sys.argv[1]

dataset = sys.argv[2]

ids = SelectImagesForTagsDatasetQuery.create_query(tag, dataset).execute()

for id in ids:
    print(id)
    image_bytes = ImageReadQuery.create_query(id).execute()
    save_image_from_bytes_locally(image_bytes, "output_images/" + str(id[0]) + ".png")