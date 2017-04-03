sum = 0;
while 1 :
    inp = int(input("숫자를 입력하시오."))
    sum = sum + inp
    if input("계속?(yes/no)") == "no" :
        break
print("합계는 : ",sum)
    
