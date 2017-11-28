#!/usr/bin/env python
import unittest
from src.Piece import *


# tester class
class MyTestCase(unittest.TestCase):
    
    # test Piece constructor
    def test_piece_constructor(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=500, height=500)
        cell0 = Cell(canvas, 200, 300, 50, "grey")
        cell1 = Cell(canvas, 200, 300, 50, "white")
        piece0 = Piece(cell0, "white")
        piece1 = Piece(cell1, "black")
        self.assertEqual(cell0, piece0.get_cell())
        self.assertEqual(cell1, piece1.get_cell())
        try:
            piece1 = Piece(cell0, "black")
            print(str(piece1) + " did not throw an exception!")
            self.assertNotEqual(piece1, cell0.get_filled_with())
        except ValueError:
            self.assertEqual(piece0, cell0.get_filled_with())
            self.assertEqual(cell0, piece0.get_cell())
            self.assertEqual(cell1, piece1.get_cell())
        self.assertEqual(piece0, piece0.get_cell().get_filled_with())

    # test Piece constructor
    def test_piece_constructor2(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=500, height=500)
        cell0 = Cell(canvas, 200, 300, 50, "grey")
        try:
            piece0 = Piece(cell0, "green")
            print(str(piece0) + " did not throw an exception!")
        except ValueError:
            self.assertEqual(None, cell0.get_filled_with())
        
    # test get_cell
    def test_get_cell(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=500, height=500)
        cell0 = Cell(canvas, 200, 300, 50, "grey")
        piece0 = Piece(cell0, "white")
        self.assertEqual(cell0, piece0.get_cell())
        
    # test get_color
    def test_get_color(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=500, height=500)
        cell0 = Cell(canvas, 200, 300, 50, "grey")
        piece0 = Piece(cell0, "white")
        self.assertEqual("white", piece0.get_color())

# run tests
if __name__ == '__main__':
    unittest.main()
