from re import L
from turtle import right
from pip import main
from cProfile import label
import tkinter as tk
import tkinter.messagebox as tkm


def num_button_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, f"{txt}")
    tkm.showinfo(txt,f"[{txt}]が押されました")

#def plus_button_click(event):
#    plus_button = event.widget
    


if __name__ == "__main__":
    insnum = 0
    root = tk.Tk()
    root.title("calc")
    #root.geometry("310x330")

    entry = tk.Entry(width = 10,
                    justify = "right",
                    font = ("OPTITimes-Roman, 34")
                    )  
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

    plus_button = tk.Button(root,
                            text = "+",
                            width = 4,
                            height = 2,
                            font = ("OPTITimes-Roman,30")
                            )
    plus_button.grid(row=4,
                    column=3
                    )

    minus_button = tk.Button(root,
                            text = "-",
                            width = 4,
                            height = 2,
                            font = ("OPTITimes-Roman,30")
                            )
    minus_button.grid(row=3,
                    column=3
                    )
    
    times_button = tk.Button(root,
                            text = "×",
                            width = 4,
                            height = 2,
                            font = ("OPTITimes-Roman,30")
                            )
    times_button.grid(row=1,
                    column=3
                    )

    divis_button = tk.Button(root,
                            text = "÷",
                            width = 4,
                            height = 2,
                            font = ("OPTITimes-Roman,30")
                            )
    divis_button.grid(row=2,
                    column=3
                    )
           
    eq_button = tk.Button(root,
                            text = "=",
                            width = 4,
                            height = 2,
                            font = ("OPTITimes-Roman,30")
                            )
    eq_button.grid(row=4,
                    column=2
                    )
    dot_button = tk.Button(root,
                            text=".",
                            width=4,
                            height=2,
                            font = ("OPTITimes-Roman,30"),
                            )
    dot_button.grid(row = 4,column= 1)

    
    root.mainloop()
