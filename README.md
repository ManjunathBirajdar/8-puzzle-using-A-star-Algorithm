# 8-puzzle-using-A-star-Algorithm
8-puzzle using A* Algorithm
The code implements two heuristics Manhattan distance and misplaced tiles. Following
is the program structure.
1. Global Variables

Two variables named expanded and fringe (priority queue) are used in function solve, which is the main function for A* algorithm.

2. Functions & Procedures

generateNeighbors() : Function to generate actions from the current state.
printPath() : Function to display path from start to goal state, actions, and path cost
considering state cost is 1 per action.
solve() : Function to calculate solution using A* algorithm.
calculateManhattanHeuristics() : Function to calculate Heuristics using Manhattan
distance.
calculateMisplacedTilesHeuristics() : Function to calculate Heuristics using
Misplaced Tiles technique
printState() : Function to print a state in 3X3 Matrix form
acceptInput() : Function to accept initial state and goal state of the problem
