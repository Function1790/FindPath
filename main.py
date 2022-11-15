from explorer import *
from setting import *
from time import sleep
from os import system

# TODO
# 도착시 해당 유닛의 이동경로


def getFormatedMap(explorer: Explorer):
    _map = MAP
    _pos = explorer.pos
    _map[_pos[1]][_pos[0]] = 2
    result = "|| "
    for y in _map:
        for x in y:
            if x == 0:   # Path
                result += "  "
            elif x == 1: # Wall
                result += "□"
            else:        # Explorer
                result += "■"
        result += " ||\n|| "
    return result


isArrived = False
Winner = None
Died_Runners = []
Runners.append(Explorer())

sleep(6)
display_map = ""
while not isArrived:
    deleted_index = []
    for i in range(len(Runners)):
        display_map = getFormatedMap(Runners[i])
        if not Runners[i].Move(): # Cant Move
            if Runners[i].pos == ARRIVAL_POINT: # isArrive?
                Winner = Runners[i]
                isArrived = True
                break
            Died_Runners.append(Runners[i])
            deleted_index.append(i)
            break

    for i in deleted_index:
        del (Runners[i])

    system("cls")
    print(display_map)
    print(f"Runners Count : {len(Runners)}")
    sleep(0.05)

print("\nArrive!!")
print(Winner.trace)
