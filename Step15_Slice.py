# Step15_Slice.py

nums = [10, 20, 30, 40, 50]

print(nums[:])
print(nums[1:])
print(nums[2:])
print(nums[3:])

print("--------------")

print(nums[:3])
print(nums[:2])
print(nums[:1])

'''
    slice의 기본 문법
    [시작 : 끝 : 증감]

    - 시작은 해당 인덱스 포함(이상)
    - 끝은 해당 인덱스 제외(미만)
'''

print("---------------")

print(nums[1:4])
print(nums[2:4])

print("---------------")

print(nums[::1])
print(nums[::2])
print(nums[::3])