import unittest
from tkinter import *
from src.BoardModel import *
from src.BoardListener import *


# tester class
class MyTestCase(unittest.TestCase):
    
    # test key_pressed
    def test_key_pressed_left(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=450, height=450)
        canvas.pack()
        board_model = BoardModel(canvas)
        board_model.select_new_cell(1, 1)
        board_listener = BoardListener(board_model)
        event = Event()
        event.keysym = "Left"
        board_listener.key_pressed(event)
        self.assertEqual((0, 1), board_model.get_cell_selected_coordinates())
        self.assertEqual(True, board_model.get_board()[0][1].get_is_selected())
        self.assertEqual(False, board_model.get_board()[1][1].get_is_selected())
        board_listener.key_pressed(event)
        self.assertEqual((0, 1), board_model.get_cell_selected_coordinates())
        self.assertEqual(True, board_model.get_board()[0][1].get_is_selected())
        self.assertEqual(False, board_model.get_board()[1][1].get_is_selected())
        
    # test key_pressed
    def test_key_pressed_up(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=450, height=450)
        canvas.pack()
        board_model = BoardModel(canvas)
        board_model.select_new_cell(1, 1)
        board_listener = BoardListener(board_model)
        event = Event()
        event.keysym = "Up"
        board_listener.key_pressed(event)
        self.assertEqual((1, 0), board_model.get_cell_selected_coordinates())
        self.assertEqual(True, board_model.get_board()[1][0].get_is_selected())
        self.assertEqual(False, board_model.get_board()[1][1].get_is_selected())
        board_listener.key_pressed(event)
        self.assertEqual((1, 0), board_model.get_cell_selected_coordinates())
        self.assertEqual(True, board_model.get_board()[1][0].get_is_selected())
        self.assertEqual(False, board_model.get_board()[1][1].get_is_selected())
    
    # test key_pressed
    def test_key_pressed_right(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=450, height=450)
        canvas.pack()
        board_model = BoardModel(canvas)
        board_model.select_new_cell(6, 6)
        board_listener = BoardListener(board_model)
        event = Event()
        event.keysym = "Right"
        board_listener.key_pressed(event)
        self.assertEqual((7, 6), board_model.get_cell_selected_coordinates())
        self.assertEqual(True, board_model.get_board()[7][6].get_is_selected())
        self.assertEqual(False, board_model.get_board()[6][6].get_is_selected())
        board_listener.key_pressed(event)
        self.assertEqual((7, 6), board_model.get_cell_selected_coordinates())
        self.assertEqual(True, board_model.get_board()[7][6].get_is_selected())
        self.assertEqual(False, board_model.get_board()[6][6].get_is_selected())

    # test key_pressed
    def test_key_pressed_down(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=450, height=450)
        canvas.pack()
        board_model = BoardModel(canvas)
        board_model.select_new_cell(6, 6)
        board_listener = BoardListener(board_model)
        event = Event()
        event.keysym = "Down"
        board_listener.key_pressed(event)
        self.assertEqual((6, 7), board_model.get_cell_selected_coordinates())
        self.assertEqual(True, board_model.get_board()[6][7].get_is_selected())
        self.assertEqual(False, board_model.get_board()[6][6].get_is_selected())
        board_listener.key_pressed(event)
        self.assertEqual((6, 7), board_model.get_cell_selected_coordinates())
        self.assertEqual(True, board_model.get_board()[6][7].get_is_selected())
        self.assertEqual(False, board_model.get_board()[6][6].get_is_selected())
        
    # test key_pressed
    def test_key_pressed_return(self):
        tkinter = Tk()
        canvas = Canvas(tkinter, width=450, height=450)
        canvas.pack()
        board_model = BoardModel(canvas)
        board_model.select_new_cell(6, 6)
        board_listener = BoardListener(board_model)
        event = Event()
        event.keysym = "Return"
        self.assertEqual(None, board_model.get_board()[6][6].get_filled_with())
        board_listener.key_pressed(event)
        self.assertNotEqual(None, board_model.get_board()[6][6].get_filled_with())
        self.assertEqual("black", board_model.get_board()[6][6].get_filled_with().get_color())
        board_model.select_new_cell(5, 6)
        self.assertEqual(None, board_model.get_board()[5][6].get_filled_with())
        board_listener.key_pressed(event)
        self.assertNotEqual(None, board_model.get_board()[5][6].get_filled_with())
        self.assertEqual("white", board_model.get_board()[5][6].get_filled_with().get_color())

if __name__ == '__main__':
    unittest.main()
