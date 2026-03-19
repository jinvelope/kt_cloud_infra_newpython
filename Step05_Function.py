# Step05_Funtion.py

"""
    function type
    - 특점 시점에 여러줄의 code를 일괄 실행하고자 할 때 사용한다.
    - 함수도 data이다. (변수에 담을 수 있다.)
    - 함수안에 저장된 code를 일괄실행 하는 것을 함수를 call 한다고 이야기한다.
    - 함수는 저장된 code를 다 실행하고 나면 원래 call 했던 위치로 실행의 흐름이 넘어온다.
    - call 했던 위치로 돌아오면서 어떤 data를 반드시 가져온다.
"""

from math import nan

from sqlalchemy import null


def test1():
    print("test1() 호출됨")

test1()
result1 = test1()

def test2(arg):
    print("전달 받은 내용 :", arg)
    print(f"전달 받은 내용 : {arg}")

test2(None)
test2(10)
test2("kim")

def print_sum(num1: int, num2: int):
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum}")

print_sum(22, 11)

def print_info(name: str, addr: str):
    print(f"이름은 {name}이고 주소는 {addr}입니다.")

print_info("최진제", "대구")
# keyword를 이용해서 인자(argument)를 전달할수도 있다.
print_info(addr="행신동", name="해골")

def get_sum(n1: int, n2: int):
    sum = n1 + n2
    return sum

val = get_sum(500, 2)
print(val)

print("종료합니다")