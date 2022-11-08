from explorer import *
from setting import *
from time import sleep
from os import system

# TODO
# 도착 안됨 버그 수정
# 도착시 해당 유닛의 이동경로


def getFormatedMap(explorer: Explorer):
    _map = MAP
    _pos = explorer.pos
    _map[_pos[1]][_pos[0]] = 2
    result = "|| "
    for y in MAP:
        for x in y:
            if x == 0:
                result += "  "
            elif x == 1:
                result += "□"
            else:
                result += "■"
        result += " ||\n|| "
    return result


isArrived = False
Winner = None
Died_Runners = []
Runners.append(Explorer())

display_map = ""
while not isArrived:
    deleted_index = []
    for i in range(len(Runners)):
        display_map = getFormatedMap(Runners[i])
        if not Runners[i].Move():
            if Runners[i].pos == ARRIVAL_POINT:
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
