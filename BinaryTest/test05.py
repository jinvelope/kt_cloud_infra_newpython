# test05.py

source = "00011111"

print(int(source, 2))


source2 = "1111003"
result1 = set(source).issubset({"0", "1"})
result2 = set(source2).issubset({"0", "1"})

print(f"{source}가 0과 1로 되어있는지 여부: {result1}")
print(f"{source2}가 0과 1로 되어있는지 여부: {result2}")