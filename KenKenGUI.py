from swampy.Gui import *
import random

g=Gui()
g.title("Izzy KenKen Solver")
#class solve(self):
#    """Attributes: board, grid, """
def setup(self):
    label = self.la("Enter the puzzle's arithmetics and their coordinates below in the required format")
    self.row()
    self.te(width=200, height=10)
    self.col()
    self.gr(cols=2)
    self.bu(text='Solve')
    self.bu(text='Quit',command=quit)    




setup(g)
g.mainloop()
