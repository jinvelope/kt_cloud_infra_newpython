# Step11_Class2.py

class MyCar:
    def __init__(self, name: str):
       print("생성자가 호출됨")
       print(self)
       self.name = name

    def drive(self):
       print(f"{self.name} 이가 달려요~")

if __name__ == "__main__":
    c1: MyCar = MyCar("소나타")
    c2: MyCar = MyCar("아반떼")
    c1.drive()
    c2.drive()