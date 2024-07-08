import os
import sqlite3

def init_db():
    db_path = '/tmp/db.sqlite3'

    # Create the database if it doesn't exist
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        conn.close()

    # Set the correct permissions
    os.chmod(db_path, 0o666)
