from setting import MAP

def addVector(pos, deltaX, deltaY) -> list:
    return [pos[0]+deltaX, pos[1]+deltaY]

class Explorer:
    def __init__(self):
        self.last_pos = [-1, -1]
        self.pos = [0, 0]

    def Move(self):
        predtic_pos = [
            addVector(self.pos, 1, 0),
            addVector(self.pos, -1, 0),
            addVector(self.pos, 0, 1),
            addVector(self.pos, 0, -1)
        ]

        possible_pos = []
        for i in predtic_pos:
            if i[0] < 0 or i[1] < 0:
                continue
            if i[0] >= len(MAP[0]) or i[1] >= len(MAP):
                continue
            if i == self.last_pos or MAP[i[1]][i[0]]!=0:
                continue
            possible_pos.append(i)

        if possible_pos == []:
            return False

        self.last_pos=self.pos
        self.pos = possible_pos[0]
        return True