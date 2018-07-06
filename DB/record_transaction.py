import psycopg2
import sys
TID = sys.argv[1]
IID = sys.argv[2]
Ufrom = sys.argv[3]
Uto = sys.argv[4]
Date = sys.argv[5]
other = sys.argv[6]

conn = psycopg2.connect(database="postgres",user="postgres",host="127.0.0.1", port="5432")
cur = conn.cursor()
cur.execute('create table IF NOT EXISTS transaction(TID text,IID text, Ihash text, Ufrom text, Uto text, Date text, other text);')
conn.commit()
cur.execute("SELECT md5(array_agg(md5((t.*)::varchar))::varchar)  FROM ( SELECT * FROM item where IID = '"+IID+"' ORDER BY 1) AS t;")
rows = cur.fetchall()
for row in rows:
    Ihash = row[0]
    break
cur.execute("insert into transaction values('"+TID+"','"+IID+"','"+Ihash+"','"+Ufrom+"','"+Uto+"','"+Date+"','"+other+"');")
conn.commit()
conn.close()
