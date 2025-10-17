import psycopg2


connect = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='623528',
    host='localhost',
    port='5432'
    )

cursor = connect.cursor()