
"""
This class is the template class for the Maze solver
"""

import os.path
import queue
# import sys
# from math import sqrt
# from _typeshed import Self
# from sys import float_repr_style

import numpy


class TeamDDAlgo:

    EMPTY = 0       # empty cell
    OBSTACLE = 1    # cell with obstacle / blocked cell
    START = 2       # the start position of the maze (red color)
    TARGET = 3      # the target/end position of the maze (green color)

    def __init__(self):
        # TODO: this is you job now :-)
        self.master = 0
        self.dimCols = 0
        self.dimRows = 0
        self.startCol = 0
        self.startRow = 0
        self.endCol = 0
        self.endRow = 0
        self.grid = [[]]
        self.cameFrom = dict()
        self.costSoFar = dict()
        print("\n[TeamDDAlgo]: Constructor TeamDDAlgo successfully executed.")

    # Setter method for the maze dimension of the rows
    def setDimRows(self, rows):
        self.dimRows = rows

    # Setter method for the maze dimension of the columns
    def setDimCols(self, cols):
        self.dimCols = cols

    # Setter method for the column of the start position
    def setStartCol(self, col):
        self.startCol = col

    # Setter method for the row of the start position
    def setStartRow(self, row):
        self.startRow = row

    # Setter method for the column of the end position
    def setEndCol(self, col):
        self.endCol = col

    # Setter method for the row of the end position
    def setEndRow(self, row):
        self.endRow = row

    # Setter method for blocked grid elements
    def setBlocked(self, row, col):
        # TODO: this is you job now :-)
        pass

    # Start to build up a new maze
    # HINT: don't forget to initialize all member variables of this class (grid, start position, end position, dimension,...)
    def startMaze(self, columns=0, rows=0):
        # TODO: this is you job now :-)
        pass

    # Start to build up a new maze
    # HINT: don't forget to initialize all member variables of this class (grid, start position, end position, dimension,...)

    # Define what shall happen after the full information of a maze has been received
    def endMaze(self):
        # TODO: this is you job now :-)
        # HINT: did you set start position and end position correctly?
        pass

    # just prints a maze on the command line
    def printMaze(self):
        # for
        pass

    # loads a maze from a file pathToConfigFile
    def loadMaze(self, pathToConfigFile):
        # check whether a function numpy.loadtxt() could be useful
        # https://numpy.org/doc/1.20/reference/generated/numpy.loadtxt.html
        # TODO: this is you job now :-)
        exists = os.path.exists(pathToConfigFile)

        if exists:
            self.grid = numpy.loadtxt(pathToConfigFile, int, delimiter=',')
            if self.checkGrid() is False:
                print("Maze is not valid")
                return False
            else:
                gridSize = numpy.shape(self.grid)
                self.setDimRows(gridSize[0])
                self.setDimCols(gridSize[1])
                startpoint = self.searchNumber(self.START)
                self.setStartRow(startpoint[0])
                self.setStartCol(startpoint[1])
                endpoint = self.searchNumber(self.TARGET)
                self.setEndRow(endpoint[0])
                self.setEndCol(endpoint[1])
                print("[TeamDDAlgo]: SUCCESS loading file: ", pathToConfigFile)
                return True
        else:
            print("[TeamDDAlgo]: ERROR loading file ", pathToConfigFile)
            return False

    # check grid for corectness
    def checkGrid(self):
        if len(self.grid) == 0:
            return False
        elif self.countNumber(self.START) != 1:
            return False
        elif self.countNumber(self.TARGET) != 1:
            return False
        else:
            for nr in range(4, 9):
                if self.countNumber(nr) != 0:
                    return False
            return True

    # searches for specific number
    def searchNumber(self, number):
        for row in range(0, self.dimRows):
            for column in range(0, self.dimCols):
                if self.grid[row, column] == number:
                    ret = (row, column)
                    return ret

    # searches for specific number
    def countNumber(self, number):
        counter = 0
        for row in range(0, numpy.shape(self.grid)[0]):
            for column in range(0, numpy.shape(self.grid)[1]):
                if self.grid[row, column] == number:
                    counter = counter+1
        return counter

    # clears the complete maze
    def clearMaze(self):
        # TODO: this is you job now :-)
        pass

    # Decides whether a certain row,column grid element is inside the maze or outside
    def isInGrid(self, row, column):
        return (row >= 0 and row < self.dimRows) and (column >= 0 and column < self.dimCols)

    def isBlocked(self, row, column):
        if not self.isInGrid(row, column):
            return True
        return self.grid[row, column] == self.OBSTACLE

    # Returns a list of all grid elements neighboured to the grid element row,column
    def getNeighbours(self, cell):
        row = cell[0]
        column = cell[1]
        potentialNeighbours = self.getAllNeighbours(row, column)
        result = self.findValidNeighbours(potentialNeighbours)
        return result

    def getAllNeighbours(self, row, column):
        upper = [row - 1, column]
        left = [row, column - 1]
        right = [row, column + 1]
        lower = [row + 1, column]
        return [upper, left, right, lower]

    def findValidNeighbours(self, allNeighbours):
        validNeighbours = []
        for neighbour in allNeighbours:
            if self.isInGrid(neighbour[0], neighbour[1]) and not self.isBlocked(neighbour[0], neighbour[1]):
                validNeighbours.append(neighbour)
        return validNeighbours

    # Gives a grid element as string, the result should be a string row,column
    def gridElementToString(self, row, col):
        return str(row) + '#' + str(col)

    # check whether two different grid elements are identical
    # aGrid and bGrid are both elements [row,column]
    def isSameGridElement(self, aGrid, bGrid):
        pass

    # Defines a heuristic method used for A* algorithm
    # aGrid and bGrid are both elements [row,column]

    def heuristic(self, aGrid, bGrid):
        # using Manhattan distance
        return abs(aGrid[0] - bGrid[0]) + abs(aGrid[1] - bGrid[1])

    # # Generates the resulting path as string from the came_from list
    # def generateResultPath(self):
    #     currentstr = self.gridElementToString(self.endRow, self.endCol)
    #     current = (self.endRow, self.endCol)
    #     path = []
    #     path.append(current)
    #     while currentstr != self.gridElementToString(self.startRow,self.startCol):
    #        current = self.cameFrom[currentstr]
    #        path.append (current)
    #        currentstr = self.gridElementToString(current[0], current[1])
    #     path.append([self.startRow,self.startCol])
    #     path.reverse()
    #     return path

    def getResultPath(self):
        currentstr = self.gridElementToString(self.endRow, self.endCol)
        current = (self.endRow, self.endCol)
        path = []
        path.append(current)
        while currentstr != self.gridElementToString(self.startRow, self.startCol):
            current = self.cameFrom[currentstr]
            path.append(current)
            currentstr = self.gridElementToString(current[0], current[1])
        path.append([self.startRow, self.startCol])
        path.reverse()
        return path

    #############################
    # Definition of Maze solver algorithm
    #
    # implementation taken from https://www.redblobgames.com/pathfinding/a-star/introduction.html
    #############################
    def myMazeSolver(self):
        frontier = queue.PriorityQueue()
        frontier.put((0, [self.startRow, self.startCol]))
        self.cameFrom[self.gridElementToString(self.startRow, self.startCol)] = None
        self.costSoFar[self.gridElementToString(self.startRow, self.startCol)] = 0

        while not frontier.empty():
            current = frontier.get()[1]

            if current == [self.endRow, self.endCol]:
                break

            for next in self.getNeighbours(current):
                nextstr = self.gridElementToString(next[0], next[1])
                newCost = self.costSoFar[self.gridElementToString(current[0], current[1])] + 1  # self.cost(current, next)
                if nextstr not in self.costSoFar or newCost < self.costSoFar[nextstr]:
                    self.costSoFar[nextstr] = newCost
                    priority = newCost + self.heuristic((self.endRow, self.endCol), next)
                    frontier.put((priority, next))
                    self.cameFrom[nextstr] = current
        path = self.getResultPath()
        # print(path)
        return path

    # Command for starting the solving procedure
    def solveMaze(self):
        print("[TeamDDAlgo]: start solving maze... ")
        return self.myMazeSolver()


if __name__ == '__main__':
    mg = TeamDDAlgo()

    # HINT: in case you want to develop the solver without MQTT messages and without always
    #       loading new different mazes --> just load any maze you would like from a file

    mg.loadMaze("..\\..\\MazeExamples\\spiral1.txt")
    print("[TeamDDAlgo]: loaded maze", mg.grid)

    # solve the maze
    # HINT: this command shall be received from MQTT client in run_all mode
    solutionString = mg.solveMaze()
    print("[TeamDDAlgo]: Result of solving maze: ", solutionString)
