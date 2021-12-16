

#import operator
import os
from os import write
from tkinter import *
from tkinter import filedialog

from swampy.Gui import *
#import operator
from functools import *
#import random
#from KenKensolver import *
from sol2 import *


FILENAME = "puzzle.txt"

view=Gui()
view.title("Izzy KenKen Solver")
def savetxt():
    # Get text from text widget
    text = mytext.get(0.0, END)
    # Save to output file
    with open(FILENAME, 'w') as file:
        file.write(text)
    
def printit():
    
    if not os.path.exists(FILENAME):
        print("FILE NOT FOUND IN DIRECTORY")

    mycanvas.clear()
    
    # We will list of verbose lines
    error = False
    lines = []
    try:
        lines = solve_puzzle(FILENAME, True)
    except:
        error = True
        
    #non_empty = list(filter(None, [item for sublist in lines for item in sublist]))
    if error:
        mycanvas.create_text(260, 75, fill="darkblue",font="Times 20 italic bold", text="NO SOLUTION")
        return
    
    
    x, y = 220, 45
    for i in range(len(lines)):
        line = lines[i]
        line = "        ".join([str(item) for item in line])
        mycanvas.create_text(x, y + i * 50, fill="darkblue",font="Times 20 italic bold", text=line)
    
def clear():
    mytext.delete(1.0, END)
    mycanvas.clear()
    



label = view.la("Enter the puzzle size, arithmetics and their cages below in the required format")
mytext=view.te(width=200, height=20)

view.row()
mycanvas = view.ca(width=400, height=400, bg='white')
view.col()
view.gr(cols=2)
view.bu(text='Save', command=savetxt)
view.bu(text='Solve', command=printit)

view.bu(text='Clear', command=clear)
view.bu(text='Quit', command=quit)
view.endgr()





view.mainloop()