from ast import Num
import tkinter as tk
import tkinter.messagebox as tkm
from turtle import right

def button_click(event):
    btn=event.widget
    num=btn["text"]
    if num=="=":
        res=eval(entry1.get())
        entry1.delete(0,tk.END)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    elif num=="C":
        entry.delete(0,tk.END)
        entry1.delete(0,tk.END)
    elif num=="上C":
        entry1.delete(0,tk.END)
    elif num=="下C":
        entry.delete(0,tk.END)
    elif num=="×":
        num="*"
        entry1.insert(tk.END,num)
    elif num=="+":
        num="+"
        entry1.insert(tk.END,num)
    else:
        entry1.insert(tk.END,num)

if __name__ == "__main__":

    root=tk.Tk()
    root.title("電卓")

    entry1=tk.Entry(root,justify="right",width=20,font=("Times New Roman",20))
    entry1.grid(row=0,column=1,columnspan=10)

    entry=tk.Entry(root,justify="right",width=10,font=("Times New Roman",40))
    entry.grid(row=1,column=1,columnspan=10)

    
    for l,i in enumerate(["C","上C","下C","",9,8,7,"+",6,5,4,"-",3,2,1,"×",0,"="]):
        button=tk.Button(root,text=f"{i}",
                        font=("Helvetica",30),
                        width=4,height=1,
                        command=button_click)
        button.bind("<1>",button_click)
        k=l%4+1
        j=l//4+2
        button.grid(row=j,column=k)

    root.mainloop()
