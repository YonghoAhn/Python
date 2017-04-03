def sum_digit(number):
    result = 0 
    for i in str(number): 
        result = result + int(i)
    return result     
 
inp = input("Enter number")
print("결과 : ")
print(format(sum_digit(int(inp))))
