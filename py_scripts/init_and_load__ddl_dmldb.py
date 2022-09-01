
def create_db(cursor):
    try:
        with open('sql_scripts/ddl_dml.sql', 'r', encoding='utf-8') as f:
            script = f.read()

        cursor.executescript(script)
    except: 
        print('Database\'s already existed.')
