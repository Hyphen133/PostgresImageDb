from array import array

import psycopg2

from client.config import config


def read_blob(id, out_filepath):
    """ read BLOB data from a table """
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgresQL database
        conn = psycopg2.connect(**params)
        # create a new cursor object
        cur = conn.cursor()
        # execute the SELECT statement
        cur.execute(""" SELECT image
                        FROM \"public\".\"Image\"
                        WHERE id = %s """,
                    (id,))

        blob = cur.fetchone()
        open(out_filepath, 'wb').write(blob[0].tobytes())
        # close the communication with the PostgresQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()