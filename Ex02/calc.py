from re import L
from turtle import right
from pip import main
from cProfile import label
import tkinter as tk
import tkinter.messagebox as tkm


def num_button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]が押されました")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("calc")
    #root.geometry("300x500")

    entry = tk.Entry(width = 10,
                    justify = "right",
                    font = "OPTITimes-Roman, 40"
                    )
    #entry.insert(tk.END,)
    entry.grid(columnspan=10)

    r, c = 1, 0 #r:行番号 c:列番号
    for num in range(9, -1, -1):
        btn = tk.Button(root,
                        text = f"{num}",
                        width = 4,
                        height = 2,
                        font = ("OPTITimes-Roman,30")
                        )

        btn.bind("<1>",num_button_click)

        btn.grid(row = r,
                column = c)
        c += 1
        if (num-1)%3 == 0:
            r += 1
            c = 0

    root.mainloop()
