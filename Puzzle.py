import math
import copy

class EightPuzzle:
	def __init__(self, initial_state=None):
		self.state = initial_state
		self.h=0
		self.g=0
		self.f=0
		self.parent = None
		self.action = None
	#Function to generate actions from the current state 
	def generateNeighbors(self,state):
		possibleMoves = []		
		for i in range (0,3):
			for j in range (0,3):
				if state[i][j] == 0:
					row,col = i,j
		
		if row > 0:
			node = copy.deepcopy(state)
			row1 = row - 1
			node[row][col] = node[row1][col]
			node[row1][col] = 0
			possibleMoves.append((node,'up'))
		if col > 0:
			node = copy.deepcopy(state)
			col1 = col - 1
			node[row][col] = node[row][col1]
			node[row][col1] = 0
			possibleMoves.append((node,'left'))
		if row < 2:
			node = copy.deepcopy(state)
			row1 = row + 1
			node[row][col] = node[row1][col]
			node[row1][col] = 0 
			possibleMoves.append((node,'down'))	
		if col < 2:
			node = copy.deepcopy(state)
			col1 = col + 1
			node[row][col] = node[row][col1]
			node[row][col1] = 0
			possibleMoves.append((node,'right'))		
		return possibleMoves
	#Function to display path from start to goal state, actions, and path cost considering 1 per action
	def printPath(self,node):
		actions = []
		path = []
		pathCost = node.g
		while node:
			path.append(node.state)
			actions.append(node.action)
			node=node.parent		
		actions.remove(None)
		print('Solution path from initial state to goal state is: ')	
		for node in reversed(path):
			printState(node)
		print('Actions from initial state to reach goal state are: ')
		actions = reversed(actions)
		actionsSequence = ", ".join(actions)
		print(actionsSequence)
		print('Path cost is: ',pathCost)
			
	#Function to calculate solution using A* algorithm
	def solve(self,initial,goal,func='Manhattan'):
		generated_nodes_count = 0
		expanded_nodes_count = 0
		fringe = []
		expanded = []
		if initial.state == goal.state:
			print("Solution Found.")
			self.printPath(initial)
			print("Generated nodes count: ",generated_nodes_count)
			print("Expanded nodes count: ", expanded_nodes_count)
			return
		if func == 'misplacedTiles':
			print(2)
			initial.h = calculateMisplacedTilesHeuristics(initial.state, goal.state)
		else: 
			initial.h = calculateManhattanHeuristics(initial.state, goal.state)
		initial.f = initial.g + initial.h
		initial.parent = None
		initial.action = None
		fringe.append(initial)
		while fringe:
			curr = fringe.pop(0)
			neighbors = self.generateNeighbors(curr.state)
			expanded.append(curr)
			expanded_nodes_count += 1
			for neighbor in neighbors:
				child = EightPuzzle()
				child.state = neighbor[0]
				child.action = neighbor[1]
				child.g = curr.g + 1
				if func == 'misplacedTiles':
					child.h = calculateMisplacedTilesHeuristics(child.state, goal.state)
				else:
					child.h = calculateManhattanHeuristics(child.state, goal.state)
				child.f = child.g + child.h
				child.parent = curr
				generated_nodes_count += 1
				if(child.state == goal.state):
					print("Solution Found.")
					self.printPath(child)
					print("Generated nodes count: ",generated_nodes_count)
					print("Expanded nodes count: ", expanded_nodes_count)
					return
				
				#check whether child state is present in expanded, if yes then don't add it in fringe 
				isExpanded = False
				try:
					expanded.index(child.state, )
				except ValueError:
					isExpanded = False
				
				#check whether child node is already in fringe and if yes, update its f value if child.f is lesser.
				if not isExpanded:				
					found = False
					k=0
					for item in fringe:
						if item.state == child.state:
							found = True
							if child.f < item.f:
								item.f = child.f
								fringe[k] = item
								break
						k += 1
					if not found:
						fringe.append(child)
				
				fringe=sorted(fringe, key=lambda x :x.f)
		print('No Solution')
		return
	
#Function to calculate Heuristics using Manhattan distance
def calculateManhattanHeuristics(state1,state2):
	arr = []
	manh_dist = 0
	for i in range (0,3):
		for j in range (0,3):
			arr.append(state2[i][j])
	
		
	for i in range (0,3,1):
		for j in range (0,3,1):
			current_ij = state1[i][j]
			i_current = i
			j_current = j
			index = arr.index(current_ij)
			i_goal, j_goal = index//3,index%3
			if current_ij != 0:
				manh_dist += (math.fabs(i_goal - i_current) + math.fabs(j_goal - j_current))
	return manh_dist

#Function to calculate Heuristics using Misplaced Tiles technique
def calculateMisplacedTilesHeuristics(state1,state2):
	h = 0	
	for i in range (0,3,1):
		for j in range (0,3,1):
			if state1[i][j] != state2[i][j] and state1[i][j] != 0:
				h += 1
	return h

#Function to print a state in 3X3 maMtrix form
def printState(state):
		for i in range(3):
			result = ""
			for j in range(3):
				result += str(state[i][j])+" "
			print(result)
		print("")
		
#Function to accept initial state and goal state of the problem
def acceptInput():
	print("Enter the initial state") #Input an array and convert it to 2D matrix
	input_arr = []
	goal_arr = []
	element = input().split(" ")
	k = 0
	try:
		for i in range(0,3):
			input_arr += [0]
		for i in range (0,3):
			input_arr[i] = [0]*3
		for i in range (0,3):
			for j in range (0,3):
				input_arr[i][j] = int(element[k])
				k+=1
	except (ValueError, IndexError):
		print("Please input the values using space separation")
		return [],[]
		
	print("Enter the goal state")
	element = input().split(" ")
	k=0
	try:
		for i in range(0,3):
			goal_arr += [0]
		for i in range (0,3):
			goal_arr[i] = [0]*3
		for i in range (0,3):
			for j in range (0,3):
				goal_arr[i][j] = int(element[k])
				k += 1	
	except (ValueError, IndexError):
		print("Please input the values using space separation")
		return input_arr,[]
	return input_arr, goal_arr

#main function driving A* algorithm for 8-puzzle problem
def main():
	input_arr, goal_arr = acceptInput()
	if  input_arr and goal_arr:
		print('Initial state is')
		printState(input_arr)
		print('Goal state is')
		printState(goal_arr)
		initial = EightPuzzle(input_arr)
		goal = EightPuzzle(goal_arr)
		print("*** A* Search for 8-puzzle using Manhattan Distance Heuristic Function ***")
		initial.solve(initial,goal)
		print("\n*** A* Search for 8-puzzle using Misplaced Tiles Heuristic Function ***")
		initial.solve(initial,goal,'misplacedTiles')
	
main()	