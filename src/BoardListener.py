#!/usr/bin/env python
from src.BoardController import *
from src.Piece import *


# listener of that Board
class BoardListener:

    # construct BoardListener
    def __init__(self, board_model):
        # all relevant information is fed to this BoardListener by that BoardController
        self.__board_model = board_model

    # key listener
    def key_pressed(self, event):
        new_x = self.__board_model.get_cell_selected_coordinates()[0]
        new_y = self.__board_model.get_cell_selected_coordinates()[1]
        if event.keysym == "Left":
            new_x = new_x - 1
        if event.keysym == "Right":
            new_x = new_x + 1
        if event.keysym == "Up":
            new_y = new_y - 1
        if event.keysym == "Down":
            new_y = new_y + 1
        self.__board_model.select_new_cell(new_x, new_y)
        if event.keysym == "Return":
            x = self.__board_model.get_cell_selected_coordinates()[0]
            y = self.__board_model.get_cell_selected_coordinates()[1]
            Piece(self.__board_model.get_board()[x][y], self.__board_model.next_to_play())
            self.__board_model.new_turn()
