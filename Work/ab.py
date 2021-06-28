import psycopg2

con = psycopg2.connect(host='192.168.205.163',
                      user='bpmn',
                      password='bpmn',
                       port=5000)

cur = con.cursor()

cur.execute("select * from doc_files where doc_type=13 and doc_id in (7113)")

rows = cur.fetchone()

print(rows)

con.close()