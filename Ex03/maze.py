import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as maze
import sys
def key_down(event):
    global key,mx,my
    key=event.keysym

def key_up(event):
    global key
    key=""

def main_proc():
    global cy,cx,mx,my,maze_bg
    move=[[0,-1],[0,1],[1,0],[-1,0]]
    key_pressed=["Up","Down","Right","Left"]
    for i,key_info in enumerate(key_pressed):
        if key==key_info:
            if maze_bg[my+move[i][1]][mx+move[i][0]]==0:
                mx+=move[i][0]
                my+=move[i][1]
    cx,cy=mx*50+25,my*50+25
    canvas.coords("tori",cx,cy)
    finished()
    root.after(100,main_proc)

def finished():
    global px,py,mx,my
    if mx==px and my==py:
        label = tk.Label(root,
            text="Game Clear!!",
            font=("Times New Roman",80)
            )
        label.pack()
        maze_bg[py-1][px]=1
        maze_bg[py+1][px]=1
        maze_bg[py][px+1]=1
        maze_bg[py][px-1]=1
        tori=tk.PhotoImage(file="ex03/fig/5.png")
        img = tori.subsample(2)
        canvas.create_image(mx,my,image=img,tag="tori")
        if key=="x":
            sys.exit()

if __name__ == "__main__":
    root=tk.Tk()
    root.title("迷える子羊")
    canvas=tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    maze_bg=maze.make_maze(30,18)
    maze.show_maze(canvas,maze_bg)
    tori=tk.PhotoImage(file="ex03/fig/5.png")
    mx,my=1,1
    cx,cy=mx*100+50,my*100+50
    img = tori.subsample(2)
    canvas.create_image(mx,my,image=img,tag="tori")
    px,py=maze.sarch(maze_bg,canvas)
    key=""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()
