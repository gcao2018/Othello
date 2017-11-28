#!/usr/bin/env python
from src.BoardListener import *


# controls that board
class BoardController:

    # construct BoardController
    def __init__(self, board):
        self.__board = board
        # controller feeds listener all relevant information
        self.__board_listener = BoardListener(board)
    
    # control the board when a key is pressed
    def key_pressed_wrapper(self, event):
        self.__board_listener.key_pressed(event)
        # delete image and redraw
        self.__board.get_canvas().delete("all")
        self.__board.draw()

# for testing
# if __name__ == "__main__":
#     root = Tk()
#     world = Canvas(root, width=450, height=450)
#     world.pack()
#     board_model = BoardModel(world)
#     board_model.draw()
#     board_controller = BoardController(board_model)
#     root.bind("<Key>", lambda event: board_controller.key_pressed_wrapper(event))
#     root.mainloop()
