# 한 줄 주석입니다.

"""
여러줄
주석
입니다.
python을 배우는 이유
1. infra 구성에 필요한 shell 프로그래밍에 활용할 수 있다.
2. iac을 할때 역시 프로글밍에 대한 감각이 필요하다.
3. fastapi를 구성해서 웹 application을 만들 예정
"""

print("Step01 시작")

# python 의 여러가지 데이터 type에 대해서 알아보자
num1 = 10 # int
num2 = 10.1 # float

# str type
myName = '최진제'
yourName = "해골"
ourName = """
    KT Cloud Infra
    화이팅!
"""

# print(ourName)

# 순서가 중요한 여러개의 데이터 관리
foods = ["삼겹살", "김밥", "닭발"]

print(foods[0:2])

# 순서가 중요하지 않지만 여러개의 데이터 관리
mem1 = {"num":1, "name":"김구라", "addr":"노량진"}
print(mem1)

# 순서가 중요하지 않지만 여러개의 데이터 관리(키값 없이)
mySet1 = {"빨강", "노랑", "파랑"}
print(mySet1)

# 특정 코드 블럭을 필요한 시점에 일괄 실행
def logic():
    print("냉장고 문을 연다")
    print("물건을 저장한다")
    print("냉장고 문을 닫는다\n")

# logic()
# logic()

a = None
print("어떤 작업을 하고 ")
print("필요할 때 값을 넣는다")
a = "test"

print(a)

# 참과 거짓을 나타내는 data type (Bool)
isMan = True # 남자
isWoman=False # 여자가 아니다
isDifferent=True # 다르다
isRun=False
canEat=True # 먹을 수 있다