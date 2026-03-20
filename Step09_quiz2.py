# Step09_quiz2.py

'''

'''

disk_usage: int = int(input("디스크 사용량을 입력(0~100) : "))

if disk_usage >= 90:
    print("디스크 용량이 부족합니다!")
elif disk_usage >= 70:
    print("디스크 사용량이 높습니다. 확장을 준비하세요")
else:
    print("정상입니다")