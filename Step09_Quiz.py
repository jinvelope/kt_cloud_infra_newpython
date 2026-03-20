# Step09_Quiz.py

'''
    비밀번호를 입력받아서 입력한 비밀번호가 8자 이상이면
    "사용가능한 비밀번호입니다"
    아니면
    "사용 불가입니다"
'''

while(1):
    pw = input("비밀번호를 입력하세요 : ")
    
    if pw == "exit":
        break;
    
    pw_len = len(pw)

    if pw_len >= 8:
        print("사용가능한 비밀번호입니다")
    else:
        print("사용불가입니다.")