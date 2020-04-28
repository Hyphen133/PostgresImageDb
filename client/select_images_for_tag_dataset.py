from client.query_base import QueryBase


class SelectImagesForTagsDatasetQuery(QueryBase):
    def __init__(self, tag_name, dataset_name) -> None:
        super().__init__()
        self.tag_name = tag_name
        self.dataset_name = dataset_name

    def execute_query(self):
        self.cursor.execute(query(self.tag_name, self.dataset_name))

        return self.cursor.fetchall()

    @staticmethod
    def create_query( tag_name, dataset_name):
        return SelectImagesForTagsDatasetQuery( tag_name, dataset_name)

query = lambda tag_name, dataset_name: "SELECT DISTINCT \"imageId\" FROM public.\"ImageDataset\" WHERE \"imageId\" IN (SELECT \"imageId\" FROM public.\"ImageTag\" WHERE \"tagId\" = ( SELECT id FROM public.\"Tag\" WHERE name='" + tag_name + "') AND \"imageId\" IN (SELECT \"imageId\" FROM public.\"ImageDataset\"	WHERE \"datasetId\" = (	SELECT id FROM public.\"Dataset\" WHERE name='" + dataset_name + "')))"


