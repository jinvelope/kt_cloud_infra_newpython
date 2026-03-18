# dict type에 대해서 알아보자

"""
    - dict type
    1. key:value 형태로 데이터를 저장한다.
    2. 순서가 없는 데이터를 
"""

mem1 = {"num" : 1, "name" : "kimgura", "isMan" : True}
info1 = [1, "kimgura", True] # True가 뭐지??
print(mem1["num"])
print(mem1["name"])
print(mem1["isMan"])

a = mem1["num"]
b = mem1["name"]
c = mem1["isMan"]

# dict 안의 내용을 수정하기
mem1["num"] = 2
mem1["name"] = "ragukim"
mem1["isMan"] = False

mem2={"num":2, "name":"해골", "isMan":False}

# 특정 key 값으로 저장된 내용 삭제
del mem1["isMan"]

#모든 값 삭제
mem1.clear()

print("종료합니다")