#! /bin/env python
from rosettastones.lib.engine import temp_db_connect

if __name__ == "__main__":
    with temp_db_connect() as c:
        c.execute("CREATE TABLE keys (id text, key text);")
        c.connection.commit()
