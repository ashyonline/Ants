from Ant import Ant
from AntNorth import AntNorth
from AntSouth import AntSouth
from AntEast import AntEast
from AntWest import AntWest

class AntFactory:
    def __init__(self):
        self._antClassMap = {}
        self._antClassMap["N"] = AntNorth
        self._antClassMap["S"] = AntSouth
        self._antClassMap["E"] = AntEast
        self._antClassMap["W"] = AntWest
        
    def createAnt(self, x, y, direction):
        return apply(self._antClassMap[direction], [x, y])
    
