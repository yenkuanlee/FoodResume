import psycopg2
import sys
TID = sys.argv[1]

conn = psycopg2.connect(database="postgres",user="postgres",host="127.0.0.1", port="5432")
cur = conn.cursor()
cur.execute("SELECT Ufrom,Uto,Date FROM transaction where TID = '"+TID+"';")
rows = cur.fetchall()
for row in rows:
    Ufrom = row[0]
    Uto = row[1]
    Date = row[2]

cur.execute("SELECT md5(array_agg(md5((t.*)::varchar))::varchar)  FROM ( SELECT * FROM transaction where TID = '"+TID+"' ORDER BY 1) AS t;")
rows = cur.fetchall()
for row in rows:
    Thash = row[0]
    break
conn.close()

print TID,Ufrom,Uto,Date,Thash
