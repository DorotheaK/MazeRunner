
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
        self.assertTrue(mg.dimCols== 10)

    def test_dimrows(self):
        mg.setDimRows(20)
    
    def test_startrow(self):
        mg.setEndRow(5)
        self.assertTrue(mg.endRow ==5)

    def test_checkMaze(self):
        check = mg.loadMaze("..\\..\\MazeExamples\\maze_fehlerhaft1.txt")
        self.assertFalse(check)
        
       

    

# class FillMazeTest(unittest.TestCase):
#     def test_isingrid(self):
#        self.assertTrue(mg.loadMaze(os.path.realpath(os.path.dirname(
#            __file__))+"/../../../MazeExamples/maze1.txt"))
#        self.assertTrue(mg.isInGrid(0, 0))
