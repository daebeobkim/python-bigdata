a = []
count = 0
def number_command(i):
    if i == 'add':
        number_add()
    elif i == 'all':
        number_all()
    elif i == 'search':
        number_search()
    elif i == 'change':
        number_change()
    elif i == 'delete':
        number_delete()
    elif i == 'quit':
        print("전화번호부를 종료합니다.")
        exit(1)

def number_add():
    global count
    count += 1
    a.append([input(str('이름을 입력하시오')),input('전화번호를 입력하시오'),input('메일을 입력하시오'),input('주소를 입력하시오')])


def number_all():
    a.sort()
    for i in range(count):
        print('%s' %a[i])
    
def number_search():
    name = input('이름입력시 정보 출력')
    for i in range(count):
        if name == a[i][0]:
            print('%s' %(a[i]))
            break
    if name != a[i][0]:
        print("해당이름이 없습니다")


def number_change():
    index = 0
    name = input('정보를 수정하고싶은 사용자의 이름을 입력하시오')
    for i in range(count):
        if name != a[i][0]:
            index = 1
            continue
        elif name == a[i][0]:
            del a[i]
            a.append([input('이름을 입력하시오'),input('전화번호를 입력하시오'),input('메일을 입력하시오'),input('주소를 입력하시오')])
            index = 0
            break
    if index == 1:
        print("해당 이름이 없습니다.")

def number_delete():
    name = input('전화번호를 삭제 할 사용자의 이름을 입력하시오')
    for i in range(count):
        if name == a[i][0]:
            a[i][1] = ("삭제된 전화번호")
            break
    if name != a[i][0]:
        print("해당이름이 없습니다")

print("---------------------------전화번호부 명령어---------------------------")
print("[add(추가),all(출력),quit(종료),search(검색),change(수정),delete(삭제)]")
print("-----------------------------------------------------------------------")
while (True):
    i = input('메뉴를 입력하시오')
    number_command(i)           
