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
    explored = set([])
    fringe = util.Stack()
    
    # Push a plan with the initial state
    for successor in problem.getSuccessors(problem.getStartState()):
        fringe.push([successor])
    while(not fringe.isEmpty()):
        plan = fringe.pop()
        state = plan[len(plan)-1][0] # read last state in this plan
        explored.add(state)
        if problem.isGoalState(state):
            for i in range(len(plan)):
                plan[i] = plan[i][1]
            return plan
        for successor in problem.getSuccessors(state):
            if successor[0] not in explored: # state not in explored
                fringe.push(plan + [successor])

    print("Failed! depthFirstSearch")
    return [] # Fail

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue() # FIFO
    explored = set([])
    # Initial State of the search problem
    initialState = problem.getStartState()
    fringe.push((initialState, '', 0)) # A tuple as (successor, actions, backwardCost)

    while(not fringe.isEmpty()):
        state, actions, g = fringe.pop() # tuple(successor, actions, backwardCost)

        if problem.isGoalState(state):
            # Convert 'actions' string to an array
            actions = actions.strip().split()
            print('actions: ', actions)
            return actions

        explored.add(state)
        
        for successorState, action, stepCost in problem.getSuccessors(state):
            if successorState not in explored:
                fringe.push((successorState, actions + action + ' ', 1))

    print("Failed! breadthFirstSearch")
    return ['Stop'] # Fail

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue() # FIFO
    explored = set([])
    # Initial State of the search problem
    initialState = problem.getStartState()
    fringe.push((initialState, '', 0), 0) # A tuple as (successor, actions, backwardCost)

    while(not fringe.isEmpty()):
        state, actions, g = fringe.pop() # tuple(successor, actions, backwardCost)
        
        if problem.isGoalState(state):
            # Convert 'actions' string to an array
            actions = actions.strip().split()
            print('actions: ', actions)
            print ('Commulative Cost: '+ str(g) +'=='+ str(problem.getCostOfActions(actions)), g == problem.getCostOfActions(actions))
            return actions

        explored.add(state)
        
        for successorState, action, stepCost in problem.getSuccessors(state):
            if successorState not in explored:
                fringe.push((successorState, actions + action + ' ', g + stepCost), g + stepCost)

    print("Failed! uniformCostSearch")
    return [''] # Fail

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
    explored = set([])
    # Initial State of the search problem
    initialState = problem.getStartState()
    h = heuristic(initialState, problem)
    fringe.push((initialState, '', 0), h) # A tuple as (successor, actions, backwardCost)

    while(not fringe.isEmpty()):
        state, actions, g = fringe.pop() # tuple(successor, actions, backwardCost)
        
        if problem.isGoalState(state):
            # Convert 'actions' string to an array
            actions = actions.strip().split()
            print('actions: ', actions)
            print ('Commulative Cost: '+ str(g) +'=='+ str(problem.getCostOfActions(actions)), g == problem.getCostOfActions(actions))
            return actions

        explored.add(state)
        
        for successorState, action, stepCost in problem.getSuccessors(state):
            if successorState not in explored:
                h = heuristic(state, problem)
                fringe.push((successorState, actions + action + ' ', g + stepCost), g + stepCost + h)

    print("Failed! A*")
    return [''] # Fail


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
