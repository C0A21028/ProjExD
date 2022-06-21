from pip import main


if __name__ == main:
    from cProfile import label
    import tkinter as tk

    root = tk.Tk()

    root.title("calc")
    root.geometry("300x500")

    root.mainloop()


