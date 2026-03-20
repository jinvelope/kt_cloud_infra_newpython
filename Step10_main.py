# Step10_main.py

'''
    현재 파일 즉 step10_main.py 에서 run 해서 실행을 하면
    __name__ 은 "__main__" 이라는 문자열이 들어있다.
    따라서 __name__을 확인해보면 해당 파일이 main으로 실행되었는지 여부를 확인할 수 있다.
    다른 곳에서 import 했을 때 실행되지 않는 코드 블럭을 만들 때 사용한다.
'''

print("Step10_main.py 가 실행됩니다")
print(__name__)

# 테스트 용도의 클래스 생성
class TestClass:
    pass

if __name__ == "__main__":
    print(__name__)