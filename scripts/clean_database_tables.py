from django.db import connections, OperationalError

"""
    Drop all tables from a given database
    Must Use PostgreSQL database
    Must need django-extension package installed
    Command: python manage.py runscript clean_database_tables
    
"""


def run():
    primary_db = connections['default']

    try:
        primary_conn = primary_db.cursor()
    except OperationalError as err:
        print("Error",err)
        return None

    try:
        primary_conn.execute(
            "SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema,table_name")
        rows = primary_conn.fetchall()
        for row in rows:
            print("dropping table: ", row[1])
            primary_conn.execute("drop table " + row[1] + " cascade")
        primary_conn.close()
        primary_conn.close()
    except Exception as err:
        print("Final Exp",err)
