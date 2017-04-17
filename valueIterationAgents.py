# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """

        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        print "getState:",mdp.getStates()
        #print "possibleActions:", mdp.getPossibleActions(state)
        #print "probs:", mdp.getTransitionStatesAndProbs(state, action)
        #print "reward:", mdp.getReward(state, action, nextState)
        #print "terminal:", mdp.isTerminal(state)
        print "Values:", self.values

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        """for state in self.mdp.getStates():
            self.values[state] = self.mdp.getReward(state,"STOP", state)"""
            #print "value:", self.values[state]
        for i in range(self.iterations):
            tmpValues = self.values.copy()
            for state in self.mdp.getStates():
                if self.mdp.isTerminal(state):
                    tmpValues[state] = 0
                else:
                    maxValue = float('-inf')
                    for action in self.mdp.getPossibleActions(state):
                        maxValue = max(maxValue,self.getQValue(state, action))
                        tmpValues[state] = maxValue

            self.values = tmpValues

            #update Value




    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        Q = 0
        for sPrime, T in self.mdp.getTransitionStatesAndProbs(state, action):
            Q += T*(self.mdp.getReward(state, action, sPrime) + self.discount*(self.getValue(sPrime)))

        return Q



    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        bestAction = None
        Qtmp = 0
        Qmax = float('-inf')
        for action in self.mdp.getPossibleActions(state):
            Qtmp = self.computeQValueFromValues(state, action)
            if Qtmp > Qmax:
                Qmax = Qtmp
                bestAction = action
            #values[state] = Qmax
        return bestAction



    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
