# Step16_Regexp4.py

import re

if __name__ == "__main__":
    # 임의의 문자열을 입력 받는다.
    user_id = input("아이디를 입력(영문자 대소문자, 숫자만 가능) : ")

    regstr = r"^[a-zA-Z0-9]+$asdfasdf"
    if re.match(regstr, user_id):
        print("가입되었습니다")
    else:
        print("사용할수 없는 아이디입니다")