import csv
f = open('C:/Users/rlaeo/OneDrive/바탕 화면/subwaytime.csv','rt',encoding='UTF8')
data = csv.reader(f)
next(data)
next(data)
mx = 0
mx_station = ''
for row in data:
    row[4:] = map(float,row[4:])
    a = row[11:16:2] #하차 인원 값 추출하기
    if sum(a) > mx:
        mx = sum(a)
        mx_station = row[3]+'('+row[1]+')'
print(mx_station,mx)
