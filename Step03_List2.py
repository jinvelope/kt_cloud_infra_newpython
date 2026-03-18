# list type에 대해서 알아보기

nums = [10, 20, 30, 40, 50]
names = ["kim", "park", "jo", "oh", "choi"]

for item in nums:
    print(item)

for item in names:
    print(item)

r1 = range(5)
r2 = range(10)

for item in r2:
    print(item,"번")

for i in range(len(names)):
    # print("list의 index와 함께 출력합니다")
    print(i, names[i])

print("종료합니다")