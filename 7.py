orgid = "test"
orgpw = "1234"

inpid = input("Enter ID")
if inpid == orgid :
    inppw = input("Enter PW")
    if inppw == orgpw :
        print("환영합니다.")
    else :
        print("비밀번호가 틀렸습니다.")
else :
    print("아이디가 틀렸습니다.")
