import csv
f = open('dong.csv', 'r', encoding='utf-8')
rd = csv.reader(f)
for line in rd:
    print(line)
f.close()
f = open()