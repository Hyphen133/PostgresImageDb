from client.drop_data import DropDataQuery
from client.fill_database import FillDataQuery

DropDataQuery.create_query().execute()
FillDataQuery.create_query().execute()
