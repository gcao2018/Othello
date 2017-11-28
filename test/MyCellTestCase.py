#!/usr/bin/env python
import unittest
from src.Cell import *
from src.Piece import *


# tester class
class MyTestCase(unittest.TestCase):

    # test get_x
    def test_get_x(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=500, height=500)
        cell0 = Cell(canvas, 200, 300, 50, "grey")
        self.assertEqual(cell0.get_x(), 200)

    # test get_y
    def test_get_y(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=500, height=500)
        cell0 = Cell(canvas, 200, 300, 50, "grey")
        self.assertEqual(cell0.get_y(), 300)

    # test get_canvas
    def test_get_canvas(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=500, height=500)
        cell0 = Cell(canvas, 200, 300, 50, "grey")
        self.assertEqual(cell0.get_canvas(), canvas)

    # test get_color
    def test_get_color(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=500, height=500)
        cell0 = Cell(canvas, 200, 300, 50, "grey")
        self.assertEqual(cell0.get_color(), "grey")

    # test get_is_selected
    def test_get_is_selected(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=500, height=500)
        cell0 = Cell(canvas, 200, 300, 50, "grey")
        self.assertEqual(cell0.get_is_selected(), False)
        cell0.set_is_selected(True)
        self.assertEqual(cell0.get_is_selected(), True)

    # test set_is_selected
    def test_set_is_selected(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=500, height=500)
        cell0 = Cell(canvas, 200, 300, 50, "grey")
        try:
            cell0.set_is_selected("Hello")
        except ValueError:
            self.assertEqual(cell0.get_is_selected(), False)
        cell0.set_is_selected(True)
        self.assertEqual(cell0.get_is_selected(), True)

    # test get_filled_with
    def test_get_filled_with(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=500, height=500)
        cell0 = Cell(canvas, 200, 300, 50, "grey")
        self.assertEqual(None, cell0.get_filled_with())
        piece0 = Piece(cell0, "white")
        self.assertEqual(piece0, cell0.get_filled_with())
    
    # test fill
    def test_fill(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=500, height=500)
        cell0 = Cell(canvas, 200, 300, 50, "grey")
        cell1 = Cell(canvas, 200, 300, 50, "white")
        piece0 = Piece(cell0, "white")
        piece1 = Piece(cell1, "black")
        try:
            piece1 = Piece(cell0, "black")
            print(str(piece1) + " did not throw an exception!")
            self.assertNotEqual(piece1, cell0.get_filled_with())
        except ValueError:
            self.assertEqual(piece0, cell0.get_filled_with())
            self.assertEqual(cell1, piece1.get_cell())
        self.assertEqual(cell0, cell0.get_filled_with().get_cell())

    # test override equals function
    def test_equals(self):
        tkinter = Tk()
        canvas0 = Canvas(tkinter, width=500, height=500)
        canvas1 = Canvas(tkinter, width=500, height=500)
        cell0 = Cell(canvas0, 250, 250, 50, "grey")
        cell1 = Cell(canvas1, 250, 250, 50, "grey")
        cell2 = Cell(canvas0, 250, 250, 50, "grey")
        # difference between == and __eq__(self, other)
        self.assertNotEqual(cell0, cell1)
        self.assertEqual(cell0, cell2)

# run tests
if __name__ == '__main__':
    unittest.main()
