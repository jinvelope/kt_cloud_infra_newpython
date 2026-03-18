# list type에 대해서 알아보자
"""
    - list type
    1. 순서가 있다.
    2. 여러 type 의 데이터를 저장할 수 있다.
    3. 값 변경 가능
"""

nums = [10, 20, 30] # 보통 한가지 data type 을 담는다
names = ["김구라", "해골", "원숭이"]
datas = [10, "xxx", True] # 여러가지 data type을 섞어서 담을 수도 있다.

nums.append(40)

# len() builtin 함수를 이용해서 list의 길이를 알 수 있다.
nums_len = len(nums)

# index를 이용해서 참조
name0 = names[0]
print("name0 : ",name0)

# index를 이용해서 삭제
del names[0]
# names.remove(0)

# 값에 의한 삭제
names.remove("원숭이")

# 맨 마지막 index를 삭제하면서 값을 가져오기
result = nums.pop()
print(result)

print(nums_len ,"종료합니다")