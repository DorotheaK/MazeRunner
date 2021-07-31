
import unittest
import sys
import os
#import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from TeamDDAlgo import TeamDDAlgo

mg = TeamDDAlgo()

class TeamDDTest(unittest.TestCase):
    def test_dimcols(self):
        mg.setDimCols(10)
        self.assertEqual(mg.dimCols, 10)

    def test_dimrows(self):
        mg.setDimRows(20)
        self.assertEqual(mg.dimRows, 20)
    
    def test_startRow(self):
        mg.setStartRow(5)
        self.assertEqual(mg.startRow, 5)

    def test_startColumn(self):
        mg.setStartCol(45)
        self.assertEqual(mg.startCol, 45)

    def test_endRow(self):
        mg.setEndRow(23)
        self.assertEqual(mg.endRow, 23)

    def test_checkMaze(self):
        check = mg.loadMaze("..\\..\\MazeExamples\\maze_fehlerhaft1.txt")
        self.assertFalse(check)

    def test_loadMaze(self):
        check = mg.loadMaze("..\\..\\MazeExamples\\maze1.txt")
        self.assertTrue(check)
        self.assertEqual(mg.grid[1,3], 1)
        self.assertTrue(mg.grid[0,4] == 2)
        self.assertTrue(mg.grid[2,4] == 3)

    def test_isBlocked(self):
        mg.loadMaze("..\\..\\MazeExamples\\maze1.txt")
        result = mg.isBlocked(0,3)
        self.assertFalse(result)
        result = mg.isBlocked(1,3)
        self.assertTrue(result)
        result = mg.isBlocked(0,4)
        self.assertFalse(result)
        result = mg.isBlocked(2,4)
        self.assertFalse(result)
        result = mg.isBlocked(-2,4)
        self.assertTrue(result)
        result = mg.isBlocked(2,-1)
        self.assertTrue(result)
        result = mg.isBlocked(6,2)
        self.assertTrue(result)
        result = mg.isBlocked(2,6)
        self.assertTrue(result)

    def test_getNeighbours(self):
        mg.loadMaze("..\\..\\MazeExamples\\maze1.txt")
        result = mg.getNeighbours((0,3))
        self.assertEqual(result, [[0,2], [0,4]])

    # debugging test  can be eliminated when everything works fine 
    #   make sure every testcase is covered by test_getNeighbours
    def test_findValidNeighbours(self):
        mg.loadMaze("..\\..\\MazeExamples\\maze1.txt")
        result = mg.findValidNeighbours([[-1, 3], [0, 2], [0, 4], [1, 3]])
        self.assertEqual(result, [[0,2], [0,4]])


    

# class FillMazeTest(unittest.TestCase):
#     def test_isingrid(self):
#        self.assertTrue(mg.loadMaze(os.path.realpath(os.path.dirname(
#            __file__))+"/../../../MazeExamples/maze1.txt"))
#        self.assertTrue(mg.isInGrid(0, 0))
