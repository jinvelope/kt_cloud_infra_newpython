# Step17_File4.py

import os, re

if __name__ == "__main__":
    # 문자열 한줄 한줄을 저장할 list
    updated_lines=[]

    pattern = r"SELINUX=[a-zA-Z]+"

    # 읽어들일 파일의 경로
    file_path = os.path.join(os.getcwd(), "config.txt")

    # 읽기 전용으로 읽어들이기
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if re.match(pattern, line):
                updated_lines.append(re.sub(pattern, "SELINUX=disabled", line))
            else:
                updated_lines.append(line)
    
    print(updated_lines)

    # list에 저장된 문자열을 이용해서 file을 새로 만들기
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

    print("config.txt 파일을 수정했습니다")