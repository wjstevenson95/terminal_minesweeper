import random
import sys
import os



class Cell:
	def __init__(self, state, hidden, value, x, y):
		self.is_numbered = state #Boolean
		self.hidden = hidden # Boolean
		self.value = value
		self.x = x
		self.y = y

	def cell_to_string(self):
		if self.hidden:
			return "-"
		else:
			return str(self.value)

class Minesweeper:
	def __init__(self, width, height):
		self.width = int(width)
		self.height = int(height)
		self.is_game_over = False
		self.adjacents = [(-1,1),(0,1),(1,1),
						(-1,0),			(1,0),
						(-1,-1),(0,-1),(1,-1)]

		self.board = [[Cell(True, False, 0, x, y) for x in range(width)] for y in range(self.height)]

		self.__randomize_mines((self.width*self.height)//4)
		self.print_board()


	def __randomize_mines(self, mines):
		mines_left = mines

		while(mines_left > 0):
			x = random.choice(range(self.width))
			y = random.choice(range(self.height))

			if self.board[x][y].is_numbered:
				self.board[x][y].is_numbered = False # Now a mine
				self.board[x][y].value = -1
				mines_left -= 1
			else:
				continue

	def __calculate_numbers(self):
		pass

	def reveal_cell(self, x, y):
		pass

	def __uncover_blanks(self, x, y):
		pass

	def print_board(self):
		for y in range(self.height):
			row_string = " "
			print(row_string.join([self.board[x][y].cell_to_string() for x in range(self.width)]))


if __name__ == "__main__":

	board = Minesweeper(4,4)



