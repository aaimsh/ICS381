# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util
from game import Grid
from game import Agent
foodList = []
class ReflexAgent(Agent):
    foodList = []
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """
    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        foodList = []
        currentFood = gameState.getFood()
        legalMoves = gameState.getLegalActions()
        #print directions
        """for x in range(0,5):
            for y in range(0, 10):
                if currentFood[x][y] == True:
                    foodPosition = (x,y)
                    print "food Position:", foodPosition
                    foodList.append(foodPosition)"""

        #print foodList
        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        #print "bestIndices:", bestIndices
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best
        #print "best Index:", chosenIndex
        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        ghostPosition = successorGameState.getGhostPositions()
        """print "new Position:", newPos
        print "new Food:", newFood
        print "new Ghost States:", newGhostStates
        print "new Scared Times:", newScaredTimes
        print "ghost Position:", ghostPosition
        #print "food Position:", foodList"""
        "*** YOUR CODE HERE ***"
        #print "+++++++++++++++++++++++++++++"
        #print foodList
        currentGameState.getScore()
        #print "Score:", currentGameState.getScore()
        #print "To Food:", manhattanDistance(newPos,foodList[0])
        #print "To Ghost:", manhattanDistance(newPos,ghostPosition[0])
        #print foodList
        foodList = currentGameState.getFood().asList()
        if len(foodList) != 0:
            maxScore = - 2.5 * manhattanDistance(newPos,foodList[0]) +  2 * manhattanDistance(newPos,ghostPosition[0]) + 1.5 * manhattanDistance(foodList[0],ghostPosition[0])
            for i in range(1,len(foodList)):
                tmpScore = - 2.5 * manhattanDistance(newPos,foodList[i]) + 2 * manhattanDistance(newPos,ghostPosition[0]) + 1.5 * manhattanDistance(foodList[i],ghostPosition[0])
                #print "tmp:", tmpScore
                if tmpScore > maxScore:
                    maxScore = tmpScore
        else:
            print "I am in the else part"
            maxScore = currentGameState.getScore()
        #foodList = []
        return maxScore

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        #self.depth = self.depth + 1
        print self.depth
        #v = float("-inf")
        action = "null"
        action = self.miniMaxPlayer(0,gameState,self.depth * gameState.getNumAgents(),"STOP")[1]
        if action != "null":
            print "inside if"
            return action

    def maxAgent(self,agentIndex, gameState, previousAction):
        v = float("-inf")
        legalMaxMoves = gameState.getLegalActions(agentIndex)
        #if len(legalMaxMoves) != 0:
        if gameState.isWin() or gameState.isLose() or depth == 0 :
            evaluation =  self.evaluationFunction(gameState)
            print "Evaluation:", evaluation
            return (evaluation, action)
        else:
            for action in legalMaxMoves:
                successorState = gameState.generateSuccessor(agentIndex, action)
                value = self.minAgent(1, successorState,depth -1,action)
                if  value > v:
                    v = value
                    previousAction = action
        return (v,previousAction)

    """def maxAgent(self,agentIndex, gameState, depth):
        #print "agent Index:", agentIndex
        v = float("-inf")
        legalMaxMoves = gameState.getLegalActions(agentIndex)
        if len(legalMaxMoves) != 0:
            if gameState.isWin() or gameState.isLose() or depth == 1 :
                for action in legalMaxMoves:
                    successorState = gameState.generateSuccessor(agentIndex, action)
                    v = max(v,self.evaluationFunction(successorState))
            else:
                for action in legalMaxMoves:
                    successorState = gameState.generateSuccessor(agentIndex, action)
                    v = max(v,self.minAgent( 1, successorState,depth -1))
        return v"""

    def minAgent(self,agentIndex, gameState,depth,action):
        v = float("inf")
        legalMoves = gameState.getLegalActions(agentIndex)
        if agentIndex == gameState.getNumAgents() - 1:
            if gameState.isWin() or gameState.isLose() or depth == 0:
                """for action in legalMoves:
                    successorState = gameState.generateSuccessor(agentIndex, action)
                    v = min(v,self.evaluationFunction(successorState))"""
                evaluation = self.evaluationFunction(gameState)
                print "Evaluation:", evaluation
                return (evaluation, action)
            else:
                for action in legalMoves:
                    successorState = gameState.generateSuccessor(agentIndex, action)
                    v = min(v,self.firstMaxAgent(0, successorState,depth -1,action))
        else:
            if gameState.isWin() or gameState.isLose() or depth == 0 :
                """for action in legalMoves:
                    successorState = gameState.generateSuccessor(agentIndex, action)
                    v = min(v,self.evaluationFunction(successorState))"""
                evaluation =  self.evaluationFunction(gameState)
                print "Evaluation:", evaluation
                return (evaluation,action)
            else:
                for action in legalMoves:
                    successorState = gameState.generateSuccessor(agentIndex, action)
                    v = min(v,self.minAgent(agentIndex + 1, successorState,depth - 1,action))
        return v

    def miniMaxPlayer(self,agentIndex,gameState,depth,action):
        previousAction = "STOP"
        if gameState.isWin() or gameState.isLose() or depth == 0:
            evaluation = self.evaluationFunction(gameState)
            #print "Evaluation:", evaluation
            return (evaluation, action)
        agentIndex = agentIndex % gameState.getNumAgents()
        legalMoves = gameState.getLegalActions(agentIndex)
        if agentIndex == 0:
            v = float("-inf")
            for action in legalMoves:
                successorState = gameState.generateSuccessor(agentIndex, action)
                value = self.miniMaxPlayer(agentIndex + 1, successorState,(depth - 1),action)[0]
                if  value > v:
                    v = value
                    previousAction = action
            #print "Maximum Value:", v
            return (v,previousAction)

        else:
            vr = float ("inf")
            for action in legalMoves:
                successorState = gameState.generateSuccessor(agentIndex, action)
                value = self.miniMaxPlayer(agentIndex + 1, successorState,depth -1,action)[0]
                #print "THIS IS THE VALUE:", value
                if  value < vr:
                    vr = value
                    previousAction = action
            #print "Minimum Value:", vr
            return (vr,previousAction)
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        return self.alphaBetaPlayer(0,gameState,self.depth * gameState.getNumAgents(),"STOP",float("-inf"),float("inf"))[1]
        util.raiseNotDefined()
    def alphaBetaPlayer(self,agentIndex,gameState,depth,action,alpha,beta):
        previousAction = "STOP"
        if gameState.isWin() or gameState.isLose() or depth == 0:
            evaluation = self.evaluationFunction(gameState)
            #print "Evaluation:", evaluation
            return (evaluation, action)
        agentIndex = agentIndex % gameState.getNumAgents()
        legalMoves = gameState.getLegalActions(agentIndex)
        if agentIndex == 0:
            v = float("-inf")
            for action in legalMoves:
                successorState = gameState.generateSuccessor(agentIndex, action)
                value = self.alphaBetaPlayer(agentIndex + 1, successorState,(depth - 1),action,alpha,beta)[0]
                if value > beta:
                    return (value,previousAction)

                if  value > v:
                    alpha = max(alpha,value)
                    v = value
                    previousAction = action
            #print "Maximum Value:", v
            return (v,previousAction)

        else:
            vr = float ("inf")
            for action in legalMoves:
                successorState = gameState.generateSuccessor(agentIndex, action)
                value = self.alphaBetaPlayer(agentIndex + 1, successorState,depth -1,action,alpha,beta)[0]
                #print "THIS IS THE VALUE:", value
                if value < alpha:
                    return (value,previousAction)
                if  value < vr:
                    beta = min(beta,value)
                    vr = value
                    previousAction = action
            #print "Minimum Value:", vr
            return (vr,previousAction)
class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.

        """
        "*** YOUR CODE HERE ***"
        return self.expectimaxPlayer(0,gameState,self.depth * gameState.getNumAgents(),"STOP")[1]

    def expectimaxPlayer(self,agentIndex,gameState,depth,action):
        previousAction = "STOP"
        if gameState.isWin() or gameState.isLose() or depth == 0:
            evaluation = self.evaluationFunction(gameState)
            #print "Evaluation:", evaluation
            return (evaluation, action)
        agentIndex = agentIndex % gameState.getNumAgents()
        legalMoves = gameState.getLegalActions(agentIndex)
        if agentIndex == 0:
            v = float("-inf")
            for action in legalMoves:
                successorState = gameState.generateSuccessor(agentIndex, action)
                value = self.expectimaxPlayer(agentIndex + 1, successorState,(depth - 1),action)[0]
                #if value > beta:
                    #return (value,previousAction)

                if  value > v:
                    #alpha = max(alpha,value)
                    v = value
                    previousAction = action
            #print "Maximum Value:", v
            return (v,previousAction)

        else:
            vr = 0
            for action in legalMoves:
                successorState = gameState.generateSuccessor(agentIndex, action)
                value = self.expectimaxPlayer(agentIndex + 1, successorState,depth -1,action)[0]
                #print "THIS IS THE VALUE:", value
                #if value < alpha:
                    #return (value,previousAction)
                #if  value < vr:
                    #beta = min(beta,value)
                vr = vr + (value/len(legalMoves))
                previousAction = action
            #print "Minimum Value:", vr
            return (vr,previousAction)
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
