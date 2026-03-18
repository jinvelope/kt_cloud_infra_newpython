# str type

text = "    Cloud Infra    "
result1 = text.strip()

myIp = "192.168.0.2"
result2 = myIp.split(".")

print(text)
print(result1)
print(result2)

result3 = ".".join(result2)
print(result3)

result4 = result3.replace(".", "-")
print(result4)

result5 = "python".upper()
result6 = "PYTHON".lower()
print(result5)
print(result6)