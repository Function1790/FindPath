import typing as t
from setting import *

Runners = []
CHAR_DIRECTION = "→↓←↑"


class Vector(list):
    def setDirection(self, direction):
        """0 : → | 1 : ↓ | 2 : ← | 3 : ↑"""
        self.direction = direction

    def getDirection(self):
        return self.direction


def DirectionToChar(direction):
    return CHAR_DIRECTION[direction]


def addVector(pos, deltaX, deltaY, direction) -> Vector:
    result = Vector([pos[0]+deltaX, pos[1]+deltaY])
    result.setDirection(direction)
    return result


def SeparateUnit(start_pos: list, speed: Vector, trace_data: str):
    """speed = possible position"""
    _unit = Explorer(start_pos)
    _unit.trace = trace_data
    _unit.recordData(speed.getDirection())
    _unit.pos = speed
    Runners.append(_unit)


class Explorer:
    def __init__(self, start_pos=[0, 0]):
        self.last_pos = [-1, -1]
        self.pos = start_pos
        self.trace = ""
        self.isMoving = True

    def recordData(self, direction):
        self.last_pos = self.pos
        self.trace += DirectionToChar(direction)

    def getWayToGo(self) -> t.List[Vector]:
        predtic_pos = [
            addVector(self.pos, 1, 0, 0),
            addVector(self.pos, -1, 0, 2),
            addVector(self.pos, 0, 1, 1),
            addVector(self.pos, 0, -1, 3)
        ]

        result = []
        for i in predtic_pos:
            if i[0] < 0 or i[1] < 0:
                continue
            if i[0] >= len(MAP[0]) or i[1] >= len(MAP):
                continue
            if i == self.last_pos or MAP[i[1]][i[0]] != 0:
                continue
            result.append(i)

        return result

    def Separate(self, _possible_pos):
        for i in _possible_pos:
            SeparateUnit(self.pos, i, self.trace)

    def Move(self):
        predtic_pos = [
            addVector(self.pos, 1, 0, 0),
            addVector(self.pos, -1, 0, 2),
            addVector(self.pos, 0, 1, 1),
            addVector(self.pos, 0, -1, 3)
        ]

        possible_pos = self.getWayToGo()
        if possible_pos==[]:
            return False

        if len(possible_pos) != 0:
            self.Separate(possible_pos[1:len(possible_pos)])

        self.recordData(possible_pos[0].getDirection())
        self.pos = possible_pos[0]

        return True
