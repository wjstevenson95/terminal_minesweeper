import random
import sys
import os



class Cell:
	def __init__(self, state, hidden, value, x, y):
		self.is_numbered = state #Boolean
		self.is_flag = False
		self.hidden = hidden # Boolean
		self.value = value
		self.x = x
		self.y = y

	def cell_to_string(self):
		if self.hidden:
			return "-"
		else:
			if self.is_flag:
				return "F"

			if self.is_numbered:
				return str(self.value)
			else:
				return "M"

class Minesweeper:
	def __init__(self, width, height, flags):
		self.width = int(width)
		self.height = int(height)
		self.is_game_over = False
		self.flags = flags
		self.adjacents = [(-1,-1),(0,-1),(1,-1),
						(-1,0),			(1,0),
						(-1,1),(0,1),(1,1)]

		self.board = [[Cell(True, True, 0, x, y) for x in range(width)] for y in range(self.height)]

	def __in_board_range(self, x, y):
		return x >= 0 and x < self.width and y >= 0 and y < self.height


	def __randomize_mines(self, first_x, first_y, mines):
		mines_left = mines

		while(mines_left > 0):
			x = random.choice(range(self.width))
			y = random.choice(range(self.height))

			if x == first_x or y == first_y:
				# Can't have the first one be a mine
				continue

			if self.board[x][y].is_numbered:
				self.board[x][y].is_numbered = False # Now a mine
				self.board[x][y].value = -1
				mines_left -= 1
			else:
				continue


	def __calculate_numbers(self):
		for y in range(self.height):
			for x in range(self.width):
				if self.board[x][y].is_numbered:
					# If not a mine, go through adjacents
					for tuple in self.adjacents:
						if self.__in_board_range(x + tuple[0],y + tuple[1]):
							if not self.board[x + tuple[0]][y + tuple[1]].is_numbered:
								self.board[x][y].value += 1

	def reveal_cell(self, x, y, first=False):
		if first:
			self.__randomize_mines(x,y,(self.width*self.height)//16)
			self.__calculate_numbers()

		if self.__in_board_range(x,y):
			if not self.board[x][y].hidden:
				print("---> Coordinate already uncovered, please choose another <---")
			else:
				if not self.board[x][y].is_numbered:
					self.is_game_over = True
					self.board[x][y].hidden = False
				else:
					if not self.board[x][y].value > 0:
						self.__uncover_blanks(x,y)
					else:
						self.board[x][y].hidden = False
		else:
			print("---> Please choose a coordinate pair within the board range! <---")

	def place_flag(self, x, y):
		if self.__in_board_range(x,y):
			self.board[x][y].hidden = False
			self.board[x][y].is_flag = True
			self.flags -= 1
		else:
			print("---> Please choose a coordinate pair within the board range! <---")



	def __uncover_blanks(self, x, y):
		if self.board[x][y].hidden:
			self.board[x][y].hidden = False
			for tuple in self.adjacents:
				dx = tuple[0]
				dy = tuple[1]
				if self.__in_board_range(x + dx, y + dy):
					if self.board[x + dx][y + dy].is_numbered:
						if self.board[x + dx][y + dy].value == 0:
							self.__uncover_blanks(x + dx, y + dy)
						else:
							self.board[x + dx][y + dy].hidden = False



	def game_over(self):
		return self.is_game_over

	def print_board(self):
		print("  ".join([str(x) for x in range(10)]) + "  " + " ".join([str(x) for x in range(10,self.width,1)]))
		print(" ".join(["--" for x in range(self.width)]))
		for y in range(self.height):
			row_string = "  "
			print(row_string.join([self.board[x][y].cell_to_string() for x in range(self.width)]))

		print("\n ###########################")
		print("Flags Left: %d" % self.flags)

if __name__ == "__main__":

	print("---> WELCOME TO MINESWEEPER! <---")
	print("---> please choose the width and height of your board (up to 20) <---")
	print("--> then choose the number of flags you have")
	width = raw_input("width: ")
	height = raw_input("height: ")
	flags = raw_input("flags: ")
	if width > 20 or height > 20:
		
	board = Minesweeper(int(width),int(height),int(flags))

	print("To start, choose an initial coordinate...")
	first_x = raw_input("first x: ")
	first_y = raw_input("first y: ")
	board.reveal_cell(int(first_x),int(first_y),True)
	board.print_board()

	while True:
		print("---> CHOICES <---")
		print("--> reveal")
		print("--> flag")
		choice = raw_input("?: ")

		if choice == "reveal":
			x = raw_input("x: ")
			y = raw_input("y: ")
			board.reveal_cell(int(x),int(y))
		elif choice == "flag":
			flag_x = raw_input("flag_x: ")
			flag_y = raw_input("flag_y: ")
			board.place_flag(int(flag_x),int(flag_y))
		else:
			print("Invalid choice...")
			continue
		
		board.print_board()

		if board.game_over():
			print("---> GAME OVER <---")
			break



