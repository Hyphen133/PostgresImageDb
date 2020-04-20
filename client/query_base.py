import psycopg2

from client.config import config


class QueryBase():
    def __init__(self) -> None:
        super().__init__()

    def execute(self):
        result = None
        try:
            self.create_cursor()
            result = self.execute_query()
            self.connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            self.cursor.close()
            if self.connection is not None:
                self.connection.close()

        return result


    def execute_query(self):
        pass

    def create_cursor(self):
        # read database configuration
        params = config()
        # connect to the PostgresQL database
        self.connection = psycopg2.connect(**params)
        # create a new cursor object
        self.cursor = self.connection.cursor()

