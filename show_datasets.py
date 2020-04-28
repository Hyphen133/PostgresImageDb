from client.select_tags import SelectQuery, selectDatasets

print(SelectQuery.create_query(selectDatasets).execute())