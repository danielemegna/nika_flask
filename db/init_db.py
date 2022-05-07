import sqlite3

sqlite_file_path = 'db/db.sqlite'
print(f'Initalizing empty sqlite file {sqlite_file_path} ...')
with open('db/schema.sql', 'r') as schema_file:
    schema_content = schema_file.read()
    db = sqlite3.connect(sqlite_file_path)
    db.executescript(schema_content)
    db.commit()
    db.close()

print('Done.')
