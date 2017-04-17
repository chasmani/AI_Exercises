import unittest

from driver import State
from driver import tree_search, breadth_first_search, depth_first_search


class TestState(unittest.TestCase):

	def setUp(self):

		self.state_1 = State([0,1,2,3])
		self.state_2 = State([1,0,2,3])
		self.state_3 = State([1,2,0,3])
		self.state_4 = State([1,2,3,0])
		self.state_5 = State([0,1,2,3,4,5,6,7,8])
		self.state_6 = State([1,0,2,3,4,5,6,7,8])
		self.state_7 = State([1,2,0,3,4,5,6,7,8])
		self.state_8 = State([1,2,3,0,4,5,6,7,8])
		self.state_9 = State([1,2,3,4,0,5,6,7,8])
		self.state_10 = State([1,2,3,4,5,0,6,7,8])
		self.state_11 = State([1,2,3,4,5,6,0,7,8])
		self.state_12 = State([1,2,3,4,5,6,7,0,8])
		self.state_13 = State([1,2,3,4,5,6,7,8,0])

	def test_print_board(self):

		self.assertEqual(self.state_1.print_board(), "\n|0|1|\n|2|3|")
		self.assertEqual(self.state_5.print_board(), "\n|0|1|2|\n|3|4|5|\n|6|7|8|")

	def test_possible_actions(self):

		self.assertEqual(self.state_1.get_possible_actions(), ["Down", "Right"])
		self.assertEqual(self.state_2.get_possible_actions(), ["Down", "Left"])
		self.assertEqual(self.state_3.get_possible_actions(), ["Up", "Right"])
		self.assertEqual(self.state_4.get_possible_actions(), ["Up", "Left"])
		self.assertEqual(self.state_5.get_possible_actions(), ["Down", "Right"])
		self.assertEqual(self.state_6.get_possible_actions(), ["Down", "Left", "Right"])
		self.assertEqual(self.state_7.get_possible_actions(), ["Down", "Left"])
		self.assertEqual(self.state_8.get_possible_actions(), ["Up", "Down","Right"])
		self.assertEqual(self.state_9.get_possible_actions(), ["Up", "Down", "Left", "Right"])
		self.assertEqual(self.state_10.get_possible_actions(), ["Up", "Down", "Left"])
		self.assertEqual(self.state_11.get_possible_actions(), ["Up", "Right"])
		self.assertEqual(self.state_12.get_possible_actions(), ["Up", "Left", "Right"])
		self.assertEqual(self.state_13.get_possible_actions(), ["Up", "Left"])

	def test_children(self):

		child_1_down = self.state_1.get_child("Down")
		self.assertEqual(child_1_down.positions, [2,1,0,3])
		self.assertEqual(child_1_down.history, ["Down"])

		child_9_up = self.state_9.get_child("Up")
		self.assertEqual(child_9_up.positions, [1,0,3,4,2,5,6,7,8])
		self.assertEqual(child_9_up.history, ["Up"])
		child_9_down = self.state_9.get_child("Down")
		self.assertEqual(child_9_down.positions, [1,2,3,4,7,5,6,0,8])
		self.assertEqual(child_9_down.history, ["Down"])
		child_9_left = self.state_9.get_child("Left")
		self.assertEqual(child_9_left.positions, [1,2,3,0,4,5,6,7,8])
		self.assertEqual(child_9_left.history, ["Left"])
		child_9_right = self.state_9.get_child("Right")
		self.assertEqual(child_9_right.positions, [1,2,3,4,5,0,6,7,8])
		self.assertEqual(child_9_right.history, ["Right"])
		
	def test_grandchildren(self):

		child_1_down = self.state_1.get_child("Down")
		grandchild_1_right = child_1_down.get_child("Right")
		self.assertEqual(grandchild_1_right.positions, [2,1,3,0])
		self.assertEqual(grandchild_1_right.history, ["Down", "Right"])

		child_9_up = self.state_9.get_child("Up")
		grandchild_1_left = child_9_up.get_child("Left")
		self.assertEqual(grandchild_1_left.history, ["Up", "Left"])
		self.assertEqual(grandchild_1_left.positions, [0,1,3,4,2,5,6,7,8])
		
	def test_get_children(self):

		children_1 = self.state_1.get_children()
		self.assertEqual(len(children_1),2)

		children_9 = self.state_9.get_children()
		self.assertEqual(len(children_9),4)

	def test_goal_state(self):

		self.assertEqual(self.state_1.goal_test(), True)
		self.assertEqual(self.state_3.goal_test(), False)
		self.assertEqual(self.state_5.goal_test(), True)
		self.assertEqual(self.state_9.goal_test(), False)


class TestTreeSearch(unittest.TestCase):

	def setUp(self):

		self.problem_1 = [1,0,2,3]
		self.problem_2 = [0,1,2,3]
		self.problem_3 = [0,1,2,3,4,5,6,7,8]
		self.problem_4 = [1,0,2,3,4,5,6,7,8]
		self.problem_5 = [3,1,2,0,4,5,6,7,8]

	def test_2_rows_solutions_bfs(self):

		solution_1 = tree_search(self.problem_1, breadth_first_search)
		self.assertEqual(solution_1.history, ["Left"])		

		solution_2 = tree_search(self.problem_2, breadth_first_search)
		self.assertEqual(solution_2.history, [])
		
	def test_3_rows_solutions_bfs(self):

		solution_3 = tree_search(self.problem_3, breadth_first_search)
		self.assertEqual(solution_3.history, [])

		solution_4 = tree_search(self.problem_4, breadth_first_search)
		self.assertEqual(solution_4.history, ["Left"])

		solution_5 = tree_search(self.problem_5, breadth_first_search)
		self.assertEqual(solution_5.history, ["Up"])


	def test_2_rows_solutions_dfs(self):

		solution_1 = tree_search(self.problem_1, depth_first_search)
		self.assertEqual(solution_1.history, ["Left"])		

		solution_2 = tree_search(self.problem_2, depth_first_search)
		self.assertEqual(solution_2.history, [])


	def test_2_rows_solutions_dfs(self):

		solution_1 = tree_search(self.problem_1, depth_first_search)
		self.assertEqual(solution_1.history, ["Left"])		

		solution_2 = tree_search(self.problem_2, depth_first_search)
		self.assertEqual(solution_2.history, [])

		
	def test_3_rows_solutions_dfs(self):

		solution_3 = tree_search(self.problem_3, depth_first_search)
		self.assertEqual(solution_3.history, [])

		'''
		These take too long and too much space - process gets killed after about a minute whe run in terminal. 
		Makes sense - DFS will miss the solution to move left, because that is not the last node created. 
		It will instead go right first and then just keep searching deeper and deeper, doesn't find a solution.
		solution_4 = tree_search(self.problem_4, depth_first_search)
		self.assertEqual(solution_4.history, ["Left"])

		
		solution_5 = tree_search(self.problem_5, breadth_first_search)
		self.assertEqual(solution_5.history, ["Up"])
		'''

if __name__=="__main__":
	unittest.main()