# gui01.py

# ui Toolkit을 사용할 수 있는 interface 객체 import 하기
import tkinter as tk

def clicked():
    print("버튼을 클릭했네요!")
    try:
        # Entry(입력창)에 입력한 문자열 읽어오기
        num = int(name_entry.get())

        if num >=0 and num <= 255:
            label2.config(text=f"변환한 2진수 : {num:08b}")
        else:
            label2.config(text=f"0~255 정수를 입력하세요")
    except Exception as e:
        label2.config(text=f"0~255 정수를 입력하세요")

if __name__ == "__main__":
    # root 창 생성
    root = tk.Tk()
    # 제목 설정
    root.title("나의 2진수 변환기 App")
    # 창의 크기
    root.geometry("400x400")

    # 레이블
    label = tk.Label(root, text="안녕하세요! python GUI 입니다\n변환할 10진수(0~255)를 입력하세요")
    label.pack(pady=20)

    # 입력창
    name_entry = tk.Entry(root, font=("Arial", 12))
    name_entry.pack(pady=5)
    name_entry.focus() # 포커스 주기



    btn = tk.Button(root, text="전송", command=clicked, width=10, bg="lightgray")
    btn.pack(pady=15)

    label2 = tk.Label(root, text="결과...")
    label2.pack(pady=20)

    # 창이 닫힐 때 까지 무한 대기
    root.mainloop()