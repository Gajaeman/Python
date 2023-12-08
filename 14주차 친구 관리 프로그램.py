friendlist=[]
while True : 
    print('1. 친구 리스트 출력')
    print('2. 친구추가')
    print('3. 친구삭제')
    print('4. 이름변경')
    print('9. 종료')
    menu=int(input('메뉴를 선택하시오 : '))
    if menu == 1 : print(friendlist)
    if menu == 2 :
        name=input('이름을 입력하시오 : ')
        friendlist.append(name)
    if menu == 3 :
        print(friendlist)
        name=input('삭제할 이름을 입력하시오 : ')
        if name in friendlist :
            friendlist.remove(name)
        else : print('해당 이름은 존재하지 않습니다.')
    if menu == 4 :
        print(friendlist)
        name=input('이름을 변경할 대상을 입력하시오 : ')
        change=input('바꿀 이름을 입력하시오 : ')
        friendlist.remove(name)
        friendlist.append(change)
        print(friendlist)
    if menu == 9 :
        break
    else : print('')
