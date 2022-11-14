import csv
import pymysql

conn = pymysql.connect(host='localhost',user='root',password='0000',db="sakila",charset='utf8')
curs = conn.cursor()

sql = "insert into data_a(사고유형대분류,사고유형중분류,사고유형,사고건수,사망자수,중상자수,경상자수,부상신고자수) values(%s,%s,%s,%s,%s,%s,%s,%s)"
f = open("C:/Users/rlaeo/OneDrive/바탕 화면/도로교통공단_사고유형별 교통사고 통계_20211231 (1).csv", "r", encoding='utf-8')
rd = csv.reader(f)
for line in rd:
   curs.execute(sql,(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]))
conn.commit()
conn.close()
f.close()