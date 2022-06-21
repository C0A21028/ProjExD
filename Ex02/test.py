from cProfile import label
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]を押しちゃったね")

root = tk.Tk()

root.title("おためし")
root.geometry("500x200")

label = tk.Label(root,
                text="テスト",
                font=("ＤＦＰ勘亭流", 36))
label.pack()

button1 = tk.Button(root,
                    text="押すなよ…絶対におすなよ",
                    font=("ＤＦＰ勘亭流", 14)
                     )
button1.bind("<1>",button_click)
button1.pack()




root.mainloop()
