try:
    # for Python2
    import Tkinter
except ImportError:
    # for Python3
    import tkinter as Tkinter
import time

import game

def create_grid(grid):
    root = Tkinter.Tk()

    root.wm_title("Conway\'s game of Life")
    w = Tkinter.Canvas(root, width=600, height=600)
    w.pack()
    while 1:
        grid = game.set_will_die(grid)
        grid = game.update(grid)
        update(grid, w)
        root.update()
        time.sleep(0.5)

def update(grid, canvas):
    try:
        canvas.delete("all")
    except:
        pass

    for r in range(20):
        for c in range(20):
            if grid.get((c, r), (False, False))[0]:
                color = "blue"
            else:
                color = "white"

            try:
                canvas.create_rectangle(c * 30, r * 30, (c + 1) * 30, (r + 1) * 30,
                                    fill=color, outline='black')
            except:
                pass


create_grid(game.toad)


