#!/usr/bin/env python
from tkinter import *
from src.Cell import *


# an othello playing piece
class Piece:
    
    # construct Piece
    def __init__(self, cell, color):
        # the Cell this Piece is placed on
        self.__cell = cell
        # default radius size is 20
        self.__radius = 20
        # color must be white or black
        if not color == "white" and not color == "black":
            raise ValueError("othello playing piece must be white or black")
        else:
            self.__color = color
        # the order matters here
        # a Cell cannot be filled with this Piece until this Piece has been constructed
        # self.__cell is filled instead of cell because cell is to be abandoned
        # self.__cell is the same Cell that was filled with this Piece
        # so maintains consistency that this Piece fills that Cell and that Cell is filled by this Piece
        # if Cell is filled by a different Piece, throw exception since this Piece cannot be constructed
        if cell is not None:
            self.__cell.fill(self)

    # get cell
    def get_cell(self):
        return self.__cell
    
    # remove this piece from that cell
    def remove_piece(self):
        self.__cell = None
    
    # get color
    def get_color(self):
        return self.__color

    # flip this piece over
    def flip(self):
        if self.__color == "white":
            self.__color = "black"
        else:
            self.__color = "white"

    # draw this Piece
    def draw(self):
        self.__cell.get_canvas().create_oval(self.__cell.get_x() - self.__radius,
                                             self.__cell.get_y() - self.__radius,
                                             self.__cell.get_x() + self.__radius,
                                             self.__cell.get_y() + self.__radius,
                                             fill=self.__color, width=1)

# for testing
# if __name__ == "__main__":
#     root1 = Tk()
#     world1 = Canvas(root1, width=55, height=55)
#     world1.pack()
#     cell3 = Cell(world1, 30, 30, 50, "grey")
#     cell3.draw()
#     piece = Piece(cell3, "white")
#     piece.draw()
#     root1.mainloop()
