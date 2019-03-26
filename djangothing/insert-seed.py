#!/usr/bin/env python3

import psycopg2

conn = psycopg2.connect(dbname='mystuff', user='postgres', password='japhahd4phah3ixood3u')
cur = conn.cursor()
cur.execute('CREATE TABLE thing (id serial PRIMARY KEY, dl varchar, dr varchar);')
cur.execute('INSERT INTO thing (dl, dr) VALUES ("abc", "def")')
cur.execute('SELECT * FROM thing;')
print(cur.fetchone())
conn.commit()
cur.close()
conn.close()
