
import numpy as np
from tkinter import *

def color_change(self,x,y):
    self.btn[x][y].config(bg="red")
    print (x,y)


#User Input
# level = int(input("Enter the level to play[0-5]:"))
level=0
# size = int(input("Enter the size of layout [4x4->4,9x9->9,etc..]:"))
size=9


#Initialization
layout=np.random.randint(2, size=10)
layout[layout<0.5]=0
layout[layout>0.5]=1
#Fix Level of toughness
layout[(layout!=0)%(2+level)==0] = 1

#GUI


root = Tk()
frame = Frame(root,text="Minesweeper")
frame.grid(row=0, column=0)

btn = [[0 for x in range(size)] for x in range(size)]
for x in range(size):
   for y in range(size):
      btn[x][y] = Button(frame, command=lambda x1=x, y1=y: self.color_change(x1, y1))
      btn[x][y].grid(column=x, row=y)

root.mainloop()