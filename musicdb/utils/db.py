from django.db import connection

def nextval(sequence, cursor=None):
    if cursor is None:
        cursor = connection.cursor()

    cursor.execute("SELECT NEXTVAL(%s)", (sequence,))

    return cursor.fetchone()[0]
