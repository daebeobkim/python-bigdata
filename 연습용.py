name1 = input(str("A학생의 이름을 쓰시오"))
old1 = int(input("A학생의 나이를 쓰시오"))


grade1 = float(input("A학생의 학점를 쓰시오"))

name2 = input("B학생의 이름을 쓰시오")
old2 = int(input("B학생의 나이를 쓰시오"))
grade2 = float(input("B학생의 학점를 쓰시오"))

name3 = input("B학생의 이름을 쓰시오")
old3 = int(input("B학생의 나이를 쓰시오"))
grade3 = float(input("B학생의 학점를 쓰시오"))

oldall=old1+old2+old3
gradeall = grade1+grade2+grade3

print("평균 나이는 %0.1f" %(oldall/3))
print("평균 학점은 %0.1f" %(gradeall/3))

maxold = old1

if old2 > maxold:
    maxold = old2
if old3 > maxold:
    maxold = old3


maxgrade = grade1

if grade2 > maxgrade:
    maxgrade = grade2
if grade3 > maxgrade:
    maxgrade = grade3

    
if maxold == old1:
    print("최고 나이 : %s" %name1)
if maxold == old2:
    print("최고 나이 : %s" %name2)
if maxold == old3:
    print("최고 나이 : %s" %name3)

if maxgrade == grade1:
    print("최고 학점 : %s" %name1)
if maxgrade == grade2:
    print("최고 학점 : %s" %name2)
if maxgrade == grade3:
    print("최고 학점 : %s" %name3)
