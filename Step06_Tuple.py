tuple1: tuple = ("one", "two", "three")

result1 = tuple1[0]
result2 = tuple1[1]
result3 = tuple1[2]

# readonly 이기 때문에 수정 삭제가 불가능하다
# del tuple1[0]
# tuple1.remove(0)
# tuple1[0] = "xxx"

# 방 1개짜리 tuple type을 만들때는 주의!!
tuple2 = ("김구라",) # , 를 넣어줘야함

# 괄호 없는 튜플 생성
tuple3 = 10, 20, 30

# 튜플에 저장된 값을 여러 변수에 나눠 담기
a, b, c = tuple3

# 두 변수에 있는 값을 서로 바꾸려면?
first = "girl"
second = "boy"
'''
temp = first
first = second
second = temp
'''
# tuple 이용하기
first, second = second, first

print("종료합니다")