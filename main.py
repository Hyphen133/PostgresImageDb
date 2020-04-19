from client.read_image import read_blob
from client.save_image import write_blob


write_blob("12", "test_images/lenna.png", ".png")
read_blob("12", "out.png")
