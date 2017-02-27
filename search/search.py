# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    explored = set()
    fringe = util.Stack()
    
    # Initial State of the search problem
    root = (problem.getStartState(), [], 0) # A tuple as (successor, actions, backwardCost)
    fringe.push(root)

    while not fringe.isEmpty():
        state, actions, g = fringe.pop() # tuple(successor, actions, backwardCost)

        if problem.isGoalState(state):
            # print ('Commulative Cost: '+ str(g) +'=='+ str(problem.getCostOfActions(actions)), g == problem.getCostOfActions(actions))
            # print('actions: ', actions)
            return actions

        explored.add(state)
        
        for successorState, action, stepCost in problem.getSuccessors(state):
            if successorState not in explored:
                successorNode = (successorState, actions+[action], 1)
                fringe.push(successorNode)

    print("dfs Failed!")
    return ['Stop'] # Fail

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue() # FIFO
    explored = set()
    # Initial State of the search problem
    root = (problem.getStartState(), [], 0) # A tuple as (successor, actions, backwardCost)
    fringe.push(root)

    while not fringe.isEmpty():
        state, actions, g = fringe.pop() # tuple(successor, actions, backwardCost)

        if problem.isGoalState(state):
            # print ('Commulative Cost: '+ str(g) +'=='+ str(problem.getCostOfActions(actions)), g == problem.getCostOfActions(actions))
            # print('actions: ', actions)
            return actions

        explored.add(state)
        
        for successorState, action, stepCost in problem.getSuccessors(state):
            if successorState not in explored and successorState not in [x[0] for x in fringe.list]:
                successorNode = (successorState, actions+[action], 1)
                fringe.push(successorNode)

    print("bfs Failed!")
    return ['Stop'] # Fail

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue() # FIFO
    explored = set()
    # Initial State of the search problem
    root = (problem.getStartState(), [], 0) # A tuple as (successor, actions, backwardCost)
    fringe.push(root, 0)

    while not fringe.isEmpty():
        state, actions, g = fringe.pop() # tuple(successor, actions, backwardCost)
        
        if problem.isGoalState(state):
            # print ('Commulative Cost: '+ str(g) +'=='+ str(problem.getCostOfActions(actions)), g == problem.getCostOfActions(actions))
            # print('actions: ', actions)
            return actions

        explored.add(state)
        
        for successorState, action, stepCost in problem.getSuccessors(state):
            successorNode = (successorState, actions+[action], g + stepCost)
            if successorState not in explored and successorState not in [x[0] for x in fringe.heap]:
                fringe.push(successorNode, g + stepCost)
                # print("IF")
            else:
                sharedState = [x for x in fringe.heap if x[0] == successorState]
                print("ELSE", sharedState)
                if len(sharedState) != 0 and sharedState[0][2] > g + stepCost:
                    print("ELSE IF", sharedState)
                    fringe.heap.pop(sharedState[0])
                    fringe.push(successorNode, g + stepCost)

            # elif successorState in [x[0] for x in fringe.heap] and fringe.heap.index([x[0] for x in fringe.heap].index(successorState))[2] > g + stepCost:
                # TODO: delete the node and replace it

                



            

    print("ucs Failed!")
    return ['Stop'] # Fail

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue() # FIFO
    explored = set()
    # Initial State of the search problem
    initialState = problem.getStartState()
    root = (initialState, [], 0) # A tuple as (successor, actions, backwardCost)
    h = heuristic(initialState, problem)
    fringe.push(root, h) # A tuple as (successor, actions, backwardCost)

    while not fringe.isEmpty():
        state, actions, g = fringe.pop() # tuple(successor, actions, backwardCost)
        
        if problem.isGoalState(state):
            # print ('Commulative Cost: '+ str(g) +'=='+ str(problem.getCostOfActions(actions)), g == problem.getCostOfActions(actions))
            # print('actions: ', actions)
            return actions

        explored.add(state)
        
        for successorState, action, stepCost in problem.getSuccessors(state):
            if successorState not in explored and successorState not in [x[0] for x in fringe.heap]:
                successorNode = (successorState, actions+[action], g + stepCost)
                h = heuristic(state, problem)
                fringe.push(successorNode, h + g + stepCost)

    print("A* Failed!")
    return ['Stop'] # Fail


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
