# gui03.py

# ui Toolkit을 사용할 수 있는 interface 객체 import 하기
import tkinter as tk
from tkinter import messagebox

def clicked():
    print("버튼을 클릭했네요!")
    # Entry(입력창)에 입력한 문자열 읽어오기
    input_value = entry.get().strip()

    if not input_value:
        result_label.config(text="결과...", fg="black")
        return
        
    try:
        if len(input_value) > 8:
            messagebox.showerror("에러", "최대 8비트 2진수만 입력 가능합니다")
            result_label.config(text="결과...", fg="black")
            return
        
        if not(set(input_value).issubset({"0", "1"})):
            messagebox.showerror("에러", "0과 1로 이루어진 2진수만 입력 가능합니다")
            result_label.config(text="결과...", fg="black")
            return

        result_label.config(text=f"변환성공!\n2진수 : {input_value} -> 10진수 : {int(input_value, 2)}", fg="blue")
    except Exception as e:
        result_label.config(text="숫자만 입력 가능합니다", fg="red")

if __name__ == "__main__":
    # root 창 생성
    root = tk.Tk()
    # 제목 설정
    root.title("나의 2진수 변환기 App")
    # 창의 크기
    root.geometry("400x400")

    # 레이블
    label = tk.Label(root, text="10진수로 변환할 2진수(최대 8비트)를 입력하세요")
    label.pack(pady=20)

    # 입력창
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    entry.focus() # 포커스 주기

    btn = tk.Button(root, text="변환", command=clicked, width=10, bg="lightgray")
    btn.pack(pady=15)

    result_label = tk.Label(root, text="결과...")
    result_label.pack(pady=20)

    # 창이 닫힐 때 까지 무한 대기
    root.mainloop()