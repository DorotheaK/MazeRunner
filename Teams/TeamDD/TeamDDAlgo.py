
"""
This class is the template class for the Maze solver
"""

# import sys
# from math import sqrt
# import queue
import numpy
import os.path


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
        self.came_from = []
        print("\n[TeamDDAlgo]: Constructor TeamDDAlgo successfully executed.")

    # Setter method for the maze dimension of the rows
    def setDimRows(self, rows):
        self.dimRows = rows
        pass

    # Setter method for the maze dimension of the columns
    def setDimCols(self, cols):
        self.dimCols = cols
        pass

    # Setter method for the column of the start position
    def setStartCol(self, col):
        self.startCol = col
        pass

    # Setter method for the row of the start position
    def setStartRow(self, row):
        self.startRow = row
        pass

    # Setter method for the column of the end position
    def setEndCol(self, col):
        self.endCol = col
        pass

    # Setter method for the row of the end position
    def setEndRow(self, row):
        self.endRow = row
        pass

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
            gridSize = numpy.shape(self.grid)
            self.setDimRows(gridSize[0])
            self.setDimCols(gridSize[1])
            startpoint = self.searchNumber(self.START)
            self.setStartRow = startpoint[0]
            self.setStartCol = startpoint[1]
            endpoint = self.searchNumber(self.TARGET)
            self.setEndRow = endpoint[0]
            self.setEndCol = endpoint[1]
            print(self.endRow)
            print("[TeamDDAlgo]: SUCCESS loading file: ", pathToConfigFile)
        else:
            print("[TeamDDAlgo]: ERROR loading file ", pathToConfigFile)

        return True
    
    # searches for specific number
    def searchNumber(self, number):
        for row in (0, self.dimRows-1):
            for column in (0, self.dimCols -1):
                if self.grid[row, column] == number:
                    return [row, column]

    # clears the complete maze
    def clearMaze(self):
        # TODO: this is you job now :-)
        pass

    # Decides whether a certain row,column grid element is inside the maze or outside
    def isInGrid(self, row, column):
        # TODO: this is you job now :-)
        pass

    # Returns a list of all grid elements neighboured to the grid element row,column
    def getNeighbours(self, row, column):
        # TODO: this is you job now :-)
        # TODO: Add a Unit Test Case --> Very good example for boundary tests and condition coverage
        pass

    # Gives a grid element as string, the result should be a string row,column
    def gridElementToString(self, row, col):
        return row + '#' + col

    # check whether two different grid elements are identical
    # aGrid and bGrid are both elements [row,column]
    def isSameGridElement(self, aGrid, bGrid):
        # TODO: this is you job now :-)
        pass

    # Defines a heuristic method used for A* algorithm
    # aGrid and bGrid are both elements [row,column]

    def heuristic(self, aGrid, bGrid):
        # TODO: this is you job now :-)
        # HINT: a good heuristic could be the distance between to grid elements aGrid and bGrid
        pass

    # Generates the resulting path as string from the came_from list
    def generateResultPath(self, came_from):
        # TODO: this is you job now :-)
        # HINT: this method is a bit tricky as you have to invert the came_from list (follow the path from end to start)
        pass

    def getResultPath(self):
        # TODO: this is you job now :-)
        pass

    #############################
    # Definition of Maze solver algorithm
    #
    # implementation taken from https://www.redblobgames.com/pathfinding/a-star/introduction.html
    #############################
    def myMazeSolver(self):
        # TODO: this is you job now :-)
        pass

    # Command for starting the solving procedure
    def solveMaze(self):
        print("[TeamDDAlgo]: start solving maze... ")
        return self.myMazeSolver()


if __name__ == '__main__':
    mg = TeamDDAlgo()

    # HINT: in case you want to develop the solver without MQTT messages and without always
    #       loading new different mazes --> just load any maze you would like from a file

    mg.loadMaze("..\\..\\MazeExamples\\maze1.txt")
    print("[TeamDDAlgo]: loaded maze", mg.grid)

    # solve the maze
    # HINT: this command shall be received from MQTT client in run_all mode
    solutionString = mg.solveMaze()
    print("[TeamDDAlgo]: Result of solving maze: ", solutionString)
