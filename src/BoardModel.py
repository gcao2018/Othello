#!/usr/bin/env python
from src.Cell import *
from src.Piece import *


# a board is made up of Cells
class BoardModel:
    # construct BoardModel
    def __init__(self, canvas):
        # canvas this board is placed on
        self.__canvas = canvas
        # othello is played on an 8 x 8 board
        self.__size = 8
        # internal representation of this board
        self.__board = []
        for x in range(self.__size):
            vertical_strip = []
            for y in range(self.__size):
                if (x + y) % 2 == 0:
                    vertical_strip.append(Cell(canvas, x * 50 + 50, y * 50 + 50, 50, "grey"))
                else:
                    vertical_strip.append(Cell(canvas, x * 50 + 50, y * 50 + 50, 50, "white"))
            self.__board.append(vertical_strip)
        # othello board starts with four pieces in the middle
        Piece(self.__board[int(self.__size / 2)][int(self.__size / 2 - 1)], "black")
        Piece(self.__board[int(self.__size / 2 - 1)][int(self.__size / 2 - 1)], "white")
        Piece(self.__board[int(self.__size / 2 - 1)][int(self.__size / 2)], "black")
        Piece(self.__board[int(self.__size / 2)][int(self.__size / 2)], "white")
        # the first cell to be selected is at coordinates (0, 0)
        self.__cell_selected_coordinates = (0, 0)
        self.__board[self.__cell_selected_coordinates[0]][self.__cell_selected_coordinates[1]].set_is_selected(True)
        # number of turns played so far in game
        self.__turns_played = 0
    
    # get canvas
    def get_canvas(self):
        return self.__canvas
    
    # get size
    def get_size(self):
        return self.__size
    
    # get board
    def get_board(self):
        return self.__board
    
    # get cell_selected
    def get_cell_selected_coordinates(self):
        return self.__cell_selected_coordinates
    
    # select a new Cell
    def select_new_cell(self, new_x, new_y):
        old_x = self.__cell_selected_coordinates[0]
        old_y = self.__cell_selected_coordinates[1]
        if not new_x < 0 and not new_y < 0 and \
                not new_x > self.__size - 1 and not new_y > self.__size - 1:
            self.__board[old_x][old_y].set_is_selected(False)
            self.__board[new_x][new_y].set_is_selected(True)
            self.__cell_selected_coordinates = (new_x, new_y)
    
    # which player is next to play?
    def next_to_play(self):
        # black goes first
        if self.__turns_played % 2 == 0:
            return "black"
        else:
            return "white"
    
    # flip pieces horizontally surrounded by piece played on coordinates (x, y)
    def __flip_horizontal(self, x, y):
        x0 = x - 1
        x1 = x + 1
        any_flipped = False
        while 0 <= x0 < self.__size and \
              self.__board[x0][y].get_filled_with() is not None and \
              self.__board[x0][y].get_filled_with().get_color() != self.__board[x][y].get_filled_with().get_color():
            if self.__horizontally_surrounded(x0, y):
                self.__board[x0][y].get_filled_with().flip()
                any_flipped = True
            x0 = x0 - 1
        while 0 <= x1 < self.__size and \
              self.__board[x1][y].get_filled_with() is not None and \
              self.__board[x1][y].get_filled_with().get_color() != self.__board[x][y].get_filled_with().get_color():
            if self.__horizontally_surrounded(x1, y):
                self.__board[x1][y].get_filled_with().flip()
                any_flipped = True
            x1 = x1 + 1
        return any_flipped
    
    # flip pieces vertically surrounded by piece played on coordinates (x, y)
    def __flip_vertical(self, x, y):
        y0 = y - 1
        y1 = y + 1
        any_flipped = False
        while 0 <= y0 < self.__size and \
              self.__board[x][y0].get_filled_with() is not None and \
              self.__board[x][y0].get_filled_with().get_color() != self.__board[x][y].get_filled_with().get_color():
            if self.__vertically_surrounded(x, y0):
                self.__board[x][y0].get_filled_with().flip()
                any_flipped = True
            y0 = y0 - 1
        while 0 <= y1 < self.__size and \
              self.__board[x][y1].get_filled_with() is not None and \
              self.__board[x][y1].get_filled_with().get_color() != self.__board[x][y].get_filled_with().get_color():
            if self.__vertically_surrounded(x, y1):
                self.__board[x][y1].get_filled_with().flip()
                any_flipped = True
            y1 = y1 + 1
        return any_flipped
    
    # flip pieces surrounded on the upwards sloping diagonal by piece played on coordinates (x, y)
    def __flip_diagonal_up_slope(self, x, y):
        x0 = x - 1
        x1 = x + 1
        y0 = y + 1
        y1 = y - 1
        any_flipped = False
        while 0 <= x0 < self.__size and 0 <= y0 < self.__size and \
              self.__board[x0][y0].get_filled_with() is not None and \
              self.__board[x0][y0].get_filled_with().get_color() != self.__board[x][y].get_filled_with().get_color():
            if self.__diagonally_surrounded_up_slope(x0, y0):
                self.__board[x0][y0].get_filled_with().flip()
                any_flipped = True
            # be very careful here
            x0 = x0 - 1
            y0 = y0 + 1
        while 0 <= x1 < self.__size and 0 <= y1 < self.__size and \
              self.__board[x1][y1].get_filled_with() is not None and \
              self.__board[x1][y1].get_filled_with().get_color() != self.__board[x][y].get_filled_with().get_color():
            if self.__diagonally_surrounded_up_slope(x1, y1):
                self.__board[x1][y1].get_filled_with().flip()
                any_flipped = True
            # be very careful here
            x1 = x1 + 1
            y1 = y1 - 1
        return any_flipped
    
    # flip pieces surrounded on downwards sloping diagonal by piece by played on coordinates (x, y)
    def __flip_diagonal_down_slope(self, x, y):
        x0 = x - 1
        x1 = x + 1
        y0 = y + 1
        y1 = y - 1
        any_flipped = False
        while 0 <= x0 < self.__size and 0 <= y1 < self.__size and \
              self.__board[x0][y1].get_filled_with() is not None and \
              self.__board[x0][y1].get_filled_with().get_color() != self.__board[x][y].get_filled_with().get_color():
            if self.__diagonally_surrounded_down_slope(x0, y1):
                self.__board[x0][y1].get_filled_with().flip()
                any_flipped = True
            # be very careful here
            x0 = x0 - 1
            y1 = y1 - 1
        while 0 <= x1 < self.__size and 0 <= y0 < self.__size and \
              self.__board[x1][y0].get_filled_with() is not None and \
              self.__board[x1][y0].get_filled_with().get_color() != self.__board[x][y].get_filled_with().get_color():
            if self.__diagonally_surrounded_down_slope(x1, y0):
                self.__board[x1][y0].get_filled_with().flip()
                any_flipped = True
            # be very careful here
            x1 = x1 + 1
            y0 = y0 + 1
        return any_flipped
    
    # make a move at coordinates (x, y) if valid; otherwise throw an exception
    def __make_valid_move(self, x, y):
        # flip relevant pieces and check if move is valid afterwards
        is_valid_move = self.__flip_horizontal(x, y)
        is_valid_move = self.__flip_vertical(x, y) or is_valid_move
        is_valid_move = self.__flip_diagonal_up_slope(x, y) or is_valid_move
        is_valid_move = self.__flip_diagonal_down_slope(x, y) or is_valid_move
        # if move is not valid, take piece off the board
        if not is_valid_move:
            self.__board[x][y].empty()
            raise ValueError("invalid move")
    
    # update turns_played and flip othello pieces
    def new_turn(self):
        selected_x = self.__cell_selected_coordinates[0]
        selected_y = self.__cell_selected_coordinates[1]
        self.__make_valid_move(selected_x, selected_y)
        self.__turns_played = self.__turns_played + 1

    # help __horizontally_surrounded
    def __left_bounded(self, x, y):
        if self.__board[x][y].get_filled_with() is None or x == 0 or \
           self.__board[x - 1][y].get_filled_with() is None:
            return False
        elif self.__board[x - 1][y].get_filled_with().get_color() != self.__board[x][y].get_filled_with().get_color():
            return True
        else:
            return self.__left_bounded(x - 1, y)
    
    # help __horizontally_surrounded
    def __right_bounded(self, x, y):
        if self.__board[x][y].get_filled_with() is None or x == self.__size - 1 or \
           self.__board[x + 1][y].get_filled_with() is None:
            return False
        elif self.__board[x + 1][y].get_filled_with().get_color() != self.__board[x][y].get_filled_with().get_color():
            return True
        else:
            return self.__right_bounded(x + 1, y)

    # is there a piece at coordinates (x, y) on this board that is horizontally surrounded?
    def __horizontally_surrounded(self, x, y):
        return self.__right_bounded(x, y) and self.__left_bounded(x, y)
    
    # help __vertically_surrounded
    def __up_bounded(self, x, y):
        if self.__board[x][y].get_filled_with() is None or y == 0 or \
           self.__board[x][y - 1].get_filled_with() is None:
            return False
        elif self.__board[x][y - 1].get_filled_with().get_color() != self.__board[x][y].get_filled_with().get_color():
            return True
        else:
            return self.__up_bounded(x, y - 1)

    # help __vertically_surrounded
    def __down_bounded(self, x, y):
        if self.__board[x][y].get_filled_with() is None or y == self.__size - 1 or \
           self.__board[x][y + 1].get_filled_with() is None:
            return False
        elif self.__board[x][y + 1].get_filled_with().get_color() != self.__board[x][y].get_filled_with().get_color():
            return True
        else:
            return self.__down_bounded(x, y + 1)
    
    # is that piece at coordinates (x, y) vertically surrounded?
    def __vertically_surrounded(self, x, y):
        return self.__up_bounded(x, y) and self.__down_bounded(x, y)
    
    # help __diagonally_surrounded_up_slope
    def __up_right_bounded(self, x, y):
        if self.__board[x][y].get_filled_with() is None or \
           x == self.__size - 1 or y == 0 or \
           self.__board[x + 1][y - 1].get_filled_with() is None:
            return False
        elif self.__board[x + 1][y - 1].get_filled_with().get_color() != \
             self.__board[x][y].get_filled_with().get_color():
            return True
        else:
            return self.__up_right_bounded(x + 1, y - 1)
    
    # help __diagonally_surrounded_up_slope
    def __down_left_bounded(self, x, y):
        if self.__board[x][y].get_filled_with() is None or \
           x == 0 or y == self.__size - 1 or \
           self.__board[x - 1][y + 1].get_filled_with() is None:
            return False
        elif self.__board[x - 1][y + 1].get_filled_with().get_color() != \
             self.__board[x][y].get_filled_with().get_color():
            return True
        else:
            return self.__down_left_bounded(x - 1, y + 1)
    
    # is that piece at coordinates (x, y) diagonally surrounded (upwards sloping diagonal)
    def __diagonally_surrounded_up_slope(self, x, y):
        return self.__up_right_bounded(x, y) and self.__down_left_bounded(x, y)
    
    # help __diagonally_surrounded_down_slope
    def __up_left_bounded(self, x, y):
        if self.__board[x][y].get_filled_with() is None or \
           x == 0 or y == 0 or \
           self.__board[x - 1][y - 1].get_filled_with() is None:
            return False
        elif self.__board[x - 1][y - 1].get_filled_with().get_color() != \
             self.__board[x][y].get_filled_with().get_color():
            return True
        else:
            return self.__up_left_bounded(x - 1, y - 1)

    # help __diagonally_surrounded_down_slope
    def __down_right_bounded(self, x, y):
        if self.__board[x][y].get_filled_with() is None or \
           x == self.__size - 1 or y == self.__size - 1 or \
           self.__board[x + 1][y + 1].get_filled_with() is None:
            return False
        elif self.__board[x + 1][y + 1].get_filled_with().get_color() != \
             self.__board[x][y].get_filled_with().get_color():
            return True
        else:
            return self.__down_right_bounded(x + 1, y + 1)

    # is that piece at coordinates (x, y) diagonally surrounded (downwards sloping diagonal)
    def __diagonally_surrounded_down_slope(self, x, y):
        return self.__up_left_bounded(x, y) and self.__down_right_bounded(x, y)
    
    # draw this board
    def draw(self):
        color = "cyan"
        if self.__turns_played % 2 == 1:
            color = "orange"
        for x in range(self.__size):
            for y in range(self.__size):
                self.__board[x][y].draw(color)

# for testing
# if __name__ == "__main__":
#     root = Tk()
#     world = Canvas(root, width=450, height=450)
#     world.pack()
#     board = BoardModel(world)
#     board.draw()
#     root.mainloop()
