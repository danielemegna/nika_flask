import sqlite3

def run(sqlite_filepath):
    print(f'Initalizing empty sqlite file {sqlite_filepath} ...')
    with open('db/schema.sql', 'r') as schema_file:
        schema_content = schema_file.read()
        db = sqlite3.connect(sqlite_filepath)
        db.executescript(schema_content)
        db.commit()
        db.close()

    print('Done.')
