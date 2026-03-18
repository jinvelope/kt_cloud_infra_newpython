# yaml 형식의 문자열 다루기

# yaml 문자열을 다룰때는 외부 모듈을 pip로 설치해서 import 해야한다.

info = '''
name: 최진제
addr: 대구
foods: 
  - 맥주
  - 베이컨
isMan: true
body:
  weight: 75
  height: 174
'''

# 과제 검색 혹은 ai의 도움을 받아서 info에 들어있는 문자열을 dict type으로 바꾸세요
# 그런 다음 dict에 들어있는 내용을 확인 후 다시 dict에 있는 내용을 이용해서 yaml 문자열 형식으로 변환해보세요.
import yaml

result = yaml.load(info, Loader=yaml.FullLoader)
result2 = yaml.dump(result)

print(result)
print(result2)