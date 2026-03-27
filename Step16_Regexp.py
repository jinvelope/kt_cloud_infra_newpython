# Step16_Regexp.py

'''
    정규표현식 (Regular Expression) 에 대해서 알아보자
'''

# 우리는 어떤 문자열을 검증하거나 혹은 특정 문자열에서 원하는 단어나 기호를 찾아야 될때가 있다.

import re

data:str = "heallo, world!"

result = re.findall(r"a", data)

print(result)

# 대상 문자열2
text:str = "Contact: 010-1111-2222 입니다"

m_obj = re.search(r"010-[0-9]{4}-[0-9]{4}", text)

print(m_obj.group())