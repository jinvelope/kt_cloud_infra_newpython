# Step03_Example.py

"""
    회원 한명의 정보는 번호, 이름, 주소로 이루어져있다.
    그리고 그러한 회원이 여러명이다.
    여러명의 회원 목록을 하나의 묶음으로(하나의 data) 관리하고싶다면..?
"""

# 3명의 회원정보를 각각 dict에 담은 다음 그 dict를 list에 담는 코드를 작성

d1 = {"num":1, "name":"kim", "addr":"seoul"}
d2 = {"num":2, "name":"lee", "addr":"deagu"}
d3 = {"num":3, "name":"choi", "addr":"busan"}

members = [d1, d2, d3]

a = members
b = members[0]
c = members[0]["num"]
d = members[0]["name"]