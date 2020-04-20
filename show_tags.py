from client.select_tags import SelectQuery, selectTags

print(SelectQuery.create_query(selectTags).execute())