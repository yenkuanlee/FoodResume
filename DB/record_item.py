import psycopg2
import sys
IID = sys.argv[1]
NAME = sys.argv[2]
Composition = sys.argv[3]
other = sys.argv[4]

conn = psycopg2.connect(database="postgres",user="postgres",host="127.0.0.1", port="5432")
cur = conn.cursor()
cur.execute('create table IF NOT EXISTS item(IID text, NAME text, composition text, other text);')
cur.execute("insert into item values('"+IID+"','"+NAME+"','"+Composition+"','"+other+"');")
conn.commit()
conn.close()
