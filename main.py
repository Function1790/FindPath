from explorer import *
from setting import *
from time import sleep
from os import system

def getFormatedMap(explorer:Explorer):
    _map=MAP
    _pos=explorer.pos
    _map[_pos[1]][_pos[0]]=2
    result=""
    for y in MAP:
        for x in y:
            if x==0:
                result+="  "
            elif x==1:
                result+="□"
            else:
                result+="■"
        result+="\n"
    return result

sleep(2)
player=Explorer()
while True:
    system("cls")
    print(getFormatedMap(player))
    print(player.pos)
    if not player.Move():
        print("\n도착!\n\n")
        break
    sleep(0.3)