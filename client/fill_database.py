import random

from client.query_base import QueryBase
from client.write_image import ImageWriteQuery


class FillDataQuery(QueryBase):
    def __init__(self) -> None:
        super().__init__()

    def execute_query(self):
        images_size = 10

        image_ids = []
        for i in range(images_size):
            id = str(random.getrandbits(60))
            image_ids.append(id)
            ImageWriteQuery.create_query(id, "test_images/lenna.png", ".png").execute()


        tag_ids = []
        id = str(random.getrandbits(60))
        tag_ids.append(id)
        self.cursor.execute("""
                            INSERT INTO public."Tag"(id,name)
                            VALUES(%s,%s)""",
                            (id, "person"))
        id = str(random.getrandbits(60))
        tag_ids.append(id)
        self.cursor.execute("""
                            INSERT INTO public."Tag"(id,name)
                            VALUES(%s,%s)""",
                            (id, "car"))
        id = str(random.getrandbits(60))
        tag_ids.append(id)
        self.cursor.execute("""
                            INSERT INTO public."Tag"(id,name)
                            VALUES(%s,%s)""",
                            (id, "chair"))

        datasets_ids = []
        id = str(random.getrandbits(60))
        datasets_ids.append(id)
        self.cursor.execute("""
                            INSERT INTO public."Dataset"(id,name, description)
                            VALUES(%s,%s,%s)""",
                            (id, "train", "training set for classification"))

        id = str(random.getrandbits(60))
        datasets_ids.append(id)
        self.cursor.execute("""
                            INSERT INTO public."Dataset"(id,name, description)
                            VALUES(%s,%s,%s)""",
                            (id, "test", "test set for classification"))

        id = str(random.getrandbits(60))
        datasets_ids.append(id)
        self.cursor.execute("""
                            INSERT INTO public."Dataset"(id,name, description)
                            VALUES(%s,%s,%s)""",
                            (id, "predict", "predict set for classification"))


        for image_id in image_ids:
            range_left = random.randint(0, len(tag_ids)-1)
            range_size = random.randint(1, len(tag_ids)-range_left)
            for tag_idx in range(range_size):
                tag_idx = tag_idx + range_left
                id = str(random.getrandbits(60))
                self.cursor.execute("""
                            INSERT INTO public."ImageTag"(id,"imageId", "tagId")
                            VALUES(%s,%s,%s)""",
                            (id, image_id, tag_ids[tag_idx]))

        for dataset_id in datasets_ids:
            range_left = random.randint(0, len(image_ids)-1)
            range_size = random.randint(1, len(image_ids)-range_left)
            for image_idx in range(range_size):
                image_idx = tag_idx + range_left
                id = str(random.getrandbits(60))
                self.cursor.execute("""
                            INSERT INTO public."ImageDataset"(id,"imageId", "datasetId")
                            VALUES(%s,%s,%s)""",
                            (id, image_ids[image_idx], dataset_id))


    @staticmethod
    def create_query():
        return FillDataQuery()


