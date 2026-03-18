# Step04_Str2.py

"""
    여러분의 이름과 주소 좋아하는 음식 2가지를 작성해서 채팅창에 올려보세요

"""

# json import 하기
import json

# str type 이긴 하지만 문자열이 특별한 형식(json)을 띄고있다.

info = '''{
    "name" : "최진제",
    "addr" : "대구",
    "foods" : ["치킨", "삼겹살"]
}'''

result = json.loads(info)
print(result["name"])
print(result["addr"])
print(result["foods"])
print(result["foods"][0])

result2 = json.dumps(result)

print(result2)