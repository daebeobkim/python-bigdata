# 함수 항목

## 변수선언 항목
aa = input('문자열을 입력하시오: ')
bb = []
result = []

count = 0

### 메인 항목
for i in range(len(aa)):
    if  aa[i].isdigit() == True:
        bb.append(aa[i])
        count = 0


    elif  aa[i].isalpha() == True:
        bb.append(aa[i])
        count = 0
    
    elif  aa[i].isspace() == True and aa[i+1].isspace() == True :

        count = count + 1
        if count < 2:
            bb.append(aa[i])

    elif aa[i].isspace() == True:
        if  count == 0:
            bb.append(aa[i])
            
    else:
        bb.append(aa[i])
        count = 0


 
if  bb[0].isspace() == True:
    for i in range(len(bb)-1):
        result.append(bb[i+1])
else:
    for i in range(len(bb)):
        result.append(bb[i])


print(''.join(result),":",len(result))
