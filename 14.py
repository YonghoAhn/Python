import random
orgnum = random.randrange(1,100)
print("1부터 100까지의 숫자를 맞추시오.")
cnt = 0;
while 1 :
    inp = int(input("숫자를 입력하시오 : "))
    if inp == orgnum :
        break
    elif inp > orgnum :
        cnt = cnt + 1
        print("높음!")
    elif inp < orgnum :
        cnt = cnt + 1
        print("낮음!")
print("축하합니다. 시도횟수 ",cnt)
