import sys
input = sys.stdin.readline
memos = {}
names = []
def memo_create():
    print("메모의 이름을 입력하세요. :", end=" ")
    name = input().rstrip()
    names.append(name)
    print("메모의 내용을 입력하세요. 입력이 끝났다면 줄바꿈을 두번 해주세요. :", end=" ")
    count = 0
    detail = []
    while True:
        detail.append(input().rstrip())
        if detail[count] == "" and detail[count-1] == "":
            detail.pop()
            detail.pop()
            break
        count += 1
    memos[name] = detail
def memo_read():
    print("읽을 메모의 이름을 입력해주세요.")
    for i in range(len(memos)):
        print(i+1,". ",names[i],sep="")
    print("이름 입력 :",end=" ")
    memo_read_name = input().rstrip()
    while not memo_read_name in memos:
        print("값이 올바르지 않습니다. ")
        print("읽을 메모의 이름을 입력해주세요.")
        for i in range(len(memos)):
            print(i+1,". ",names[i],sep="")
        print("이름 입력 :",end=" ")
        memo_read_name = input().rstrip()
    for i in memos[memo_read_name]:
        print(i)
def memo_delete():
    print("지울 메모의 이름을 입력해주세요.")
    for i in range(len(memos)):
        print(i+1,". ",names[i],sep="")
    print("이름 입력 :",end=" ")
    memo_delete_name = input().rstrip()
    while not memo_delete_name in memos:
        print("값이 올바르지 않습니다. ")
        print("지울 메모의 이름을 입력해주세요.")
        for i in range(len(memos)):
            print(i+1,". ",names[i],sep="")
        print("이름 입력 :",end=" ")
        memo_delete_name = input().rstrip()
    memos.pop(memo_delete_name)
while True:
    if len(memos) == 0:
        print("메모가 존재하지 않습니다.\n새 메모를 작성하세겠습니까? 새 메모를 작성하지 않는다면 종료됩니다.(y/n) :", end=" ")
        first_memo = input().rstrip()
        while first_memo != "y" and first_memo != "n":
            print("값이 올바르지 않습니다.\n새 메모를 작성하세겠습니까? 새 메모를 작성하지 않는다면 종료됩니다.(y/n) :", end=" ")
            first_memo = input().rstrip()
        if first_memo == "y":
            memo_create()
        else:
            break
    else:
        print("모드를 선택해주세요. \nCREATE(c), READ(r), UPDATE(u), DELETE(d) (데이터베이스에서 쓰이는 것 맞습니다.) :", end=" ")
        mode = input().rstrip()
        while mode != "c" and mode != "r" and mode != "u" and mode != "d":
            print("값이 올바르지 않습니다. \n모드를 선택해주세요. \nCREATE(c), READ(r), UPDATE(u), DELETE(d) (데이터베이스에서 쓰이는 것 맞습니다.) :")
            mode = input().rstrip()
        if mode == "c":
            memo_create()
        elif mode == "r":
            memo_read()
        elif mode == "u":
            print("대충 Update 어떻게 코드 짜야할지 모르겠음")
        elif mode == "d":
            memo_delete()