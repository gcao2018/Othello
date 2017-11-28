#!/usr/bin/env python
from tkinter import *


# a square unit of a Board
class Cell:

    # construct Cell
    def __init__(self, canvas, x, y, size, color):
        # canvas this Cell is placed on
        self.__canvas = canvas
        # horizontal position of this Cell
        self.__x = x
        # vertical position of this Cell
        self.__y = y
        # length of one side of this Cell
        self.__size = size
        # color of this cell
        self.__color = color
        # is this Cell selected or not?
        self.__is_selected = False
        # initially, this Cell has no piece placed on it and is thus empty
        # cannot be filled unless a piece is constructed
        self.__filled_with = None

    # draw this Cell
    def draw(self, selected_color):
        if self.__is_selected:
            self.__canvas.create_rectangle(self.__x - self.__size / 2,
                                           self.__y + self.__size / 2,
                                           self.__x + self.__size / 2,
                                           self.__y - self.__size / 2,
                                           fill=selected_color, width=1)
        else:
            self.__canvas.create_rectangle(self.__x - self.__size / 2,
                                           self.__y + self.__size / 2,
                                           self.__x + self.__size / 2,
                                           self.__y - self.__size / 2,
                                           fill=self.__color, width=1)
        if self.__filled_with is not None:
            self.__filled_with.draw()
    
    # get canvas of this cell
    def get_canvas(self):
        return self.__canvas
    
    # get horizontal position of this cell
    def get_x(self):
        return self.__x
    
    # get vertical position of this cell
    def get_y(self):
        return self.__y
    
    # get color of this cell
    def get_color(self):
        return self.__color
    
    # is this Cell selected or not?
    def get_is_selected(self):
        return self.__is_selected
    
    # set is_selected
    def set_is_selected(self, boolean):
        if isinstance(boolean, bool):
            self.__is_selected = boolean
        else:
            raise ValueError("argument must be a boolean")

    # get filled_with
    def get_filled_with(self):
        return self.__filled_with
    
    # empty this Cell
    def empty(self):
        if self.__filled_with is not None:
            self.__filled_with.remove_piece()
            self.__filled_with = None
    
    # fill this Cell
    def fill(self, piece):
        if piece.get_cell() == self and self.__filled_with is None:
            self.__filled_with = piece
        else:
            raise ValueError("piece says it fills a different cell")

    # override equals function
    def __eq__(self, other):
        return type(other) is type(self) and \
               self.__canvas == other.get_canvas() and \
               self.__x == other.get_x() and \
               self.__y == other.get_y() and \
               self.__color == other.get_color()

# for testing
# if __name__ == "__main__":
#     root = Tk()
#     world = Canvas(root, width=55, height=55)
#     world.pack()
#     cell = Cell(world, 30, 30, 50, "grey")
#     cell.draw()
#     root.mainloop()
