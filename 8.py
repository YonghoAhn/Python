import random
num1 = random.randrange(1,100)
num2 = random.randrange(1,100)
ans = int(num1-num2)
print(num1)
print(" - ")
print(num2)
print(ans)
answer = input("\nEnter Answer")
if int(answer) == ans :
    print("맞았습니다")
else :
    print("틀렸습니다.")
