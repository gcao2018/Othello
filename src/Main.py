#!/usr/bin/env python
from src.BoardModel import *
from src.BoardController import *

# run othello program
if __name__ == "__main__":
    root = Tk()
    world = Canvas(root, width=450, height=450)
    world.pack()
    board_model = BoardModel(world)
    board_model.draw()
    board_controller = BoardController(board_model)
    root.bind("<Key>", lambda event: board_controller.key_pressed_wrapper(event))
    root.mainloop()
