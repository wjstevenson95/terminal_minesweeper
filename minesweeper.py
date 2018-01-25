import random
import sys
import os



class Cell:
	def __init__(self, state, hidden, value, x, y):
		self.state = state #Boolean
		self.hidden = hidden # Boolean
		self.value
		self.x = x
		self.y = y

class Minesweeper:
	def __init__(self, width, height):
		self.width = int(width)
		self.height = int(height)
		self.is_game_over = False

		self.board = [[Cell(True, True, 0, x, y) for x in range(width)] for y in range(self.height)]

		self.__randomize_mines(self, (self.width*self.height)//4):


	def __randomize_mines(self, mines):

	def __calculate_numbers(self):

	def __uncover_blanks(self, x, y):

	def reveal_cell(self, x, y):

	def print_board(self):


