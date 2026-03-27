import os

if __name__ == "__main__":
    letter_path = os.path.join(os.getcwd(), "Zoo.txt")

    with open(letter_path, "r", encoding="utf-8") as f:
        for line in f:
            print(line,end="")