import random
while 1 :
    while 1 :
        num1 = random.randrange(1,50)
        num2 = random.randrange(1,50)
        if num1 > num2 :
            break
    print(num1," - ",num2)
    inp = int(input(" "))
    if inp == num1 - num2 :
        print("잘했어요!")
    else :
        print("다음에는 잘할수 있죠?")

