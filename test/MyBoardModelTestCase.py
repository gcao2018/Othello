#!/usr/bin/env python
import unittest
from src.BoardModel import *


# tester class
class MyTestCase(unittest.TestCase):

    # test get_canvas
    def test_get_canvas(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=450, height=450)
        canvas.pack()
        board = BoardModel(canvas)
        self.assertEqual(canvas, board.get_canvas())
    
    # test get_size
    def test_get_size(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=450, height=450)
        canvas.pack()
        board = BoardModel(canvas)
        self.assertEqual(8, board.get_size())
        
    # test get_board
    def test_get_board(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=450, height=450)
        canvas.pack()
        board = BoardModel(canvas)
        board_model = []
        for x in range(board.get_size()):
            vertical_strip = []
            for y in range(board.get_size()):
                if (x + y) % 2 == 0:
                    vertical_strip.append(Cell(canvas, x * 50 + 50, y * 50 + 50, 50, "grey"))
                else:
                    vertical_strip.append(Cell(canvas, x * 50 + 50, y * 50 + 50, 50, "white"))
            board_model.append(vertical_strip)
        self.assertEqual(board_model, board.get_board())

    # test get_cell_selected
    def test_get_cell_selected(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=450, height=450)
        canvas.pack()
        board = BoardModel(canvas)
        self.assertEqual((0, 0), board.get_cell_selected_coordinates())
        self.assertEqual(True, board.get_board()[0][0].get_is_selected())
        self.assertEqual(False, board.get_board()[7][7].get_is_selected())

    # test select_new_cell
    def test_select_new_cell(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=450, height=450)
        canvas.pack()
        board = BoardModel(canvas)
        board.select_new_cell(-1, 0)
        self.assertEqual((0, 0), board.get_cell_selected_coordinates())
        self.assertEqual(True, board.get_board()[0][0].get_is_selected())
        self.assertEqual(False, board.get_board()[7][7].get_is_selected())
        board.select_new_cell(0, -1)
        self.assertEqual((0, 0), board.get_cell_selected_coordinates())
        self.assertEqual(True, board.get_board()[0][0].get_is_selected())
        self.assertEqual(False, board.get_board()[7][7].get_is_selected())
        board.select_new_cell(8, 0)
        self.assertEqual((0, 0), board.get_cell_selected_coordinates())
        self.assertEqual(True, board.get_board()[0][0].get_is_selected())
        self.assertEqual(False, board.get_board()[7][7].get_is_selected())
        board.select_new_cell(0, 8)
        self.assertEqual((0, 0), board.get_cell_selected_coordinates())
        self.assertEqual(True, board.get_board()[0][0].get_is_selected())
        self.assertEqual(False, board.get_board()[7][7].get_is_selected())
        board.select_new_cell(7, 7)
        self.assertEqual((7, 7), board.get_cell_selected_coordinates())
        self.assertEqual(False, board.get_board()[0][0].get_is_selected())
        self.assertEqual(True, board.get_board()[7][7].get_is_selected())
    
    # test next_to_play
    def test_get_turns_played(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=450, height=450)
        canvas.pack()
        board = BoardModel(canvas)
        self.assertEqual("black", board.next_to_play())

    # test new_turn
    def test_new_turn(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=450, height=450)
        canvas.pack()
        board = BoardModel(canvas)
        self.assertEqual("black", board.next_to_play())
        board.new_turn()
        self.assertEqual("white", board.next_to_play())
        board.new_turn()
        self.assertEqual("black", board.next_to_play())
        board.new_turn()
        self.assertEqual("white", board.next_to_play())

# run tests
if __name__ == '__main__':
    unittest.main()
