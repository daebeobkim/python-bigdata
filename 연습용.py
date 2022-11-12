a = []
count=0
while True:
    per = input('메뉴를 입력하시오')
    if per == 'quit':
            break
    while True:
        
        if per == 'add':
            count += 1
            a.append([input(str('이름을 입력하시오')),input('전화번호를 입력하시오'),input('메일을 입력하시오'),input('주소를 입력하시오')])
            break
        elif per == 'all':
            
            a.sort()
            for i in range(count):
                print('%s' %a[i])
            break
        elif per == 'search':
            name = input('이름입력시 정보 출력')
            for i in range(count):
                if name == a[i][0]:
                    print('%s' %(a[i]))
                    break
            if name != a[i][0]:
                print("해당이름이 없습니다")
                break
            break
        elif per == 'change':
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
        elif per == 'delete':
            name = input('전화번호를 삭제 할 사용자의 이름을 입력하시오')
            for i in range(count):
                if name == a[i][0]:
                    a[i][1] = ("삭제된 전화번호")
                    break
            if name != a[i][0]:
                print("해당이름이 없습니다")
        else:
            print("메뉴를 다시 선택하시오")
            break
        break
