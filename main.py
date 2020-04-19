import random

from client.read_image import read_blob
from client.save_image import write_blob


id = str(random.getrandbits(60))

write_blob(id, "test_images/lenna.png", ".png")
read_blob(id, "out.png")
