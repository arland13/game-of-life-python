import random
import os
import time
import msvcrt
import copy
os.system("cls")

def dead_state(width, height):
    board_state = [[0 for _ in range(width)] for _ in range(height)]
    return board_state

def random_state(width, height):
    state = dead_state(width, height)
    for y in range(height):
        for x in range(width):
            state[y][x] = random.choice([0,1])
    return state

def render(board_state):
    print("\n    " + " ".join(f"{i:0}" for i in range(len(board_state[0]))))
    print("   " + "--" * len(board_state[0]))
    for r, row in enumerate(board_state):
        line = f"{r:0}|"
        for col in row:
            if col == 0:
                col = " "
            if col == 1:
                col = "#"
            line += col
        print(" ".join(line) + "|" )
    print("   " + "--" * len(board_state[0]))

def next_board_state(init_state):
    old_state = copy.deepcopy(init_state)
    for r, row in enumerate(old_state, 1):
        height = r
        width = len(row)
    
    for y in range(height):
        for x in range(width):

            if y == 0 and x == 0 :
                neighbors = [
                    old_state[y][x+1],
                    old_state[y+1][x],
                    old_state[y+1][x+1]
                ]
                 #rules logic
                if old_state[y][x] == 1 and neighbors.count(1) < 2:
                    init_state[y][x] = 0
                elif old_state[y][x] == 1 and  2 <= neighbors.count(1) <= 3:
                    init_state[y][x] = 1
                elif old_state[y][x] == 1 and neighbors.count(1) > 3:
                    init_state[y][x] = 0
                elif old_state[y][x] == 0 and neighbors.count(1) == 3:
                    init_state[y][x] = 1

            elif y == 0 and x == width-1:
                neighbors = [
                    old_state[y][x-1],
                    old_state[y+1][x],
                    old_state[y+1][x-1]
                ]
                 #rules logic
                if old_state[y][x] == 1 and neighbors.count(1) < 2:
                    init_state[y][x] = 0
                elif old_state[y][x] == 1 and  2 <= neighbors.count(1) <= 3:
                    init_state[y][x] = 1
                elif old_state[y][x] == 1 and neighbors.count(1) > 3:
                    init_state[y][x] = 0
                elif old_state[y][x] == 0 and neighbors.count(1) == 3:
                    init_state[y][x] = 1

            elif y == height-1 and x == 0:
                neighbors = [
                    old_state[height-1][x-1],
                    old_state[height-2][x],
                    old_state[height-2][x-1]
                ]
                #rules logic
                if old_state[y][x] == 1 and neighbors.count(1) < 2:
                    init_state[y][x] = 0
                elif old_state[y][x] == 1 and  2 <= neighbors.count(1) <= 3:
                    init_state[y][x] = 1
                elif old_state[y][x] == 1 and neighbors.count(1) > 3:
                    init_state[y][x] = 0
                elif old_state[y][x] == 0 and neighbors.count(1) == 3:
                    init_state[y][x] = 1

            elif y == height-1 and x == width-1:
                neighbors = [
                    old_state[height-1][width-2],
                    old_state[height-2][width-1],
                    old_state[height-2][width-2]
                ]
                 #rules logic
                if old_state[y][x] == 1 and neighbors.count(1) < 2:
                    init_state[y][x] = 0
                elif old_state[y][x] == 1 and  2 <= neighbors.count(1) <= 3:
                    init_state[y][x] = 1
                elif old_state[y][x] == 1 and neighbors.count(1) > 3:
                    init_state[y][x] = 0
                elif old_state[y][x] == 0 and neighbors.count(1) == 3:
                    init_state[y][x] = 1

            elif y == 0 and 0 < x < width-1 :  
                neighbors = [
                    old_state[y][x+1],
                    old_state[y][x-1],
                    old_state[y+1][x],
                    old_state[y+1][x-1],
                    old_state[y+1][x+1]
                ]
                 #rules logic
                if old_state[y][x] == 1 and neighbors.count(1) < 2:
                    init_state[y][x] = 0
                elif old_state[y][x] == 1 and  2 <= neighbors.count(1) <= 3:
                    init_state[y][x] = 1
                elif old_state[y][x] == 1 and neighbors.count(1) > 3:
                    init_state[y][x] = 0
                elif old_state[y][x] == 0 and neighbors.count(1) == 3:
                    init_state[y][x] = 1

            elif y == height-1 and 0 < x < width-1:
                neighbors = [
                    old_state[y][x+1],
                    old_state[y][x-1],
                    old_state[y-1][x],
                    old_state[y-1][x-1],
                    old_state[y-1][x+1]
                ]
                #rules logic
                if old_state[y][x] == 1 and neighbors.count(1) < 2:
                    init_state[y][x] = 0
                elif old_state[y][x] == 1 and  2 <= neighbors.count(1) <= 3:
                    init_state[y][x] = 1
                elif old_state[y][x] == 1 and neighbors.count(1) > 3:
                    init_state[y][x] = 0
                elif old_state[y][x] == 0 and neighbors.count(1) == 3:
                    init_state[y][x] = 1

            elif 0 < y < height-1 and x == 0:
                neighbors = [
                    old_state[y][x+1],
                    old_state[y-1][x],
                    old_state[y+1][x],
                    old_state[y-1][x+1],
                    old_state[y+1][x+1]
                ]
                #rules logic
                if old_state[y][x] == 1 and neighbors.count(1) < 2:
                    init_state[y][x] = 0
                elif old_state[y][x] == 1 and  2 <= neighbors.count(1) <= 3:
                    init_state[y][x] = 1
                elif old_state[y][x] == 1 and neighbors.count(1) > 3:
                    init_state[y][x] = 0
                elif old_state[y][x] == 0 and neighbors.count(1) == 3:
                    init_state[y][x] = 1

            elif 0 < y < height-1 and x == width-1:
                neighbors = [
                    old_state[y-1][x],
                    old_state[y+1][x],
                    old_state[y][x-1],
                    old_state[y-1][x-1],
                    old_state[y+1][x-1]
                ]
                #rules logic
                if old_state[y][x] == 1 and neighbors.count(1) < 2:
                    init_state[y][x] = 0
                elif old_state[y][x] == 1 and  2 <= neighbors.count(1) <= 3:
                    init_state[y][x] = 1
                elif old_state[y][x] == 1 and neighbors.count(1) > 3:
                    init_state[y][x] = 0
                elif old_state[y][x] == 0 and neighbors.count(1) == 3:
                    init_state[y][x] = 1

            else:
                neighbors = [
                    old_state[y+1][x],
                    old_state[y+1][x+1],
                    old_state[y+1][x-1],
                    old_state[y][x+1],
                    old_state[y][x-1],
                    old_state[y-1][x],
                    old_state[y-1][x+1],
                    old_state[y-1][x-1]
                ]
                #rules logic
                if old_state[y][x] == 1 and neighbors.count(1) < 2:
                    init_state[y][x] = 0
                elif old_state[y][x] == 1 and  2 <= neighbors.count(1) <= 3:
                    init_state[y][x] = 1
                elif old_state[y][x] == 1 and neighbors.count(1) > 3:
                    init_state[y][x] = 0
                elif old_state[y][x] == 0 and neighbors.count(1) == 3:
                    init_state[y][x] = 1
                    
    return init_state


if __name__ == "__main__":
    while True:
        os.system("cls")
        x = random_state(8, 8)
        y=next_board_state(x)
        render(y)
        time.sleep(1)
        

        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'q':
                print("Goodbye 🖐🏾")
                break
                    
        
        
        
