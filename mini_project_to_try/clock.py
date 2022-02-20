import tkinter as tk
from time import strftime

root=tk.Tk()
root.title("Clock")

timing=tk.Label(root,font=("arial",100),bg="black",fg="white")
timing.pack()

def clock():
    clock_time=strftime('%X %p')
    timing.config(text=clock_time)
    timing.after(1000,clock)

clock()

root.mainloop()