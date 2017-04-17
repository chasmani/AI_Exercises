import math

class State:
	"State of the game at any point"

	def __init__(self, positions, history=[]):
		self.positions = positions
		self.rows = int(math.sqrt(len(positions)))
		self.history = history
		self.zero_pos = self.positions.index(0)

	def __str__(self):
		return "State object. Board: {}. History: {}".format(self.positions, self.history)

	def get_possible_actions(self):
		
		possible_actions = []
		if self.zero_pos >= self.rows:
			possible_actions.append("Up")
		if self.zero_pos < len(self.positions) - self.rows:
			possible_actions.append("Down")
		if (self.zero_pos) % self.rows != 0:
			possible_actions.append("Left")
		if self.zero_pos % self.rows != self.rows-1:
			possible_actions.append("Right")
		return possible_actions

	def get_child(self, action):

		if action == "Up":
			new_zero_position = self.zero_pos - self.rows
		if action == "Down":
			new_zero_position = self.zero_pos + self.rows
		if action == "Left":
			new_zero_position = self.zero_pos - 1
		if action == "Right":
			new_zero_position = self.zero_pos + 1
			
		tile_to_switch = self.positions[new_zero_position]

		child_position = list(self.positions)
		child_position.remove(0)
		child_position.insert(int(new_zero_position), 0)
		child_position.remove(tile_to_switch)
		child_position.insert(int(self.zero_pos), tile_to_switch)
		
		child_history = self.history + [action]
		child = State(child_position, child_history)
		return child

	def get_children(self):

		children = []
		for action in self.get_possible_actions():
			children.append(self.get_child(action))
		return children

	def print_board(self):

		board = ""
		for current_row in range(self.rows):
			board += "\n"
			row_start  = current_row * self.rows
			row_end = (current_row + 1) * self.rows
			row_digits = self.positions[row_start:row_end]
			row_strings = [str(i) for i in row_digits]
			board += ("|" + "|".join(row_strings) + "|")
		return board

	def goal_test(self):
		goal_positions = sorted(self.positions)
		if goal_positions == self.positions:
			return True
		else:
			return False


def breadth_first_search(fringe):
	return fringe[0]

def depth_first_search(fringe):
	return fringe[-1]


def tree_search(problem, strategy):

	initial_state = State(problem)
	fringe = [initial_state]
	while len(fringe)>0:
		node_to_expand = strategy(fringe)
		fringe.remove(node_to_expand)

		if node_to_expand.goal_test():
			return node_to_expand
		else:
			fringe += node_to_expand.get_children()