import csv
import pymysql

conn = pymysql.connect(host='localhost',user='root',password='0000',db="sakila",charset='utf8')
curs = conn.cursor()
sql = "select * from 고객"
f = open("C:/Users/rlaeo/OneDrive/문서/GitHub/python-bigdata/데이터사이언스_분석/test.csv", "w", encoding='utf-8',newline='')
wr = csv.writer(f)
curs.execute(sql)
rows = curs.fetchall()

for row in rows:
    print(row)
conn.commit()
conn.close()
f.close()

#sql = "insert into 고객(고객아이디,고객이름,나이) values (%s,%s,%s)"
#f = open("C:/Users/rlaeo/OneDrive/문서/GitHub/python-bigdata/데이터사이언스_분석/test.csv", "r", encoding='utf-8')
#rd = csv.reader(f)
#for line in rd:
 #   curs.execute(sql,(line[0],line[1],line[2]))
#conn.commit()
#conn.close()
#f.close()
