import os
import time
from collections import defaultdict
from life import load_pattern, random_state
import msvcrt

os.system("cls")

pattern = load_pattern("patterns/gosper_glider_gun.txt")
board = random_state(30,30)

NEIGHBORS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

# Convert pattern → set
alive = {
    (x, y)
    for y, row in enumerate(pattern)
    for x, cell in enumerate(row)
    if cell == 1
}

def step(alive):
    neighbor_count = defaultdict(int)

    for (x, y) in alive:
        for dx, dy in NEIGHBORS:
            neighbor_count[(x + dx, y + dy)] += 1

    new_alive = set()
    for cell, count in neighbor_count.items():
        if cell in alive and count in (2, 3):
            new_alive.add(cell)
        elif cell not in alive and count == 3:
            new_alive.add(cell)

    return new_alive

def render(alive):
    if not alive:
        print("(empty)")
        return

    xs = [x for x, y in alive]
    ys = [y for x, y in alive]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    for y in range(min_y, max_y + 1):
        row = ""
        for x in range(min_x, max_x + 1):
            row += "#" if (x, y) in alive else " "
        print(row)

while True:
    os.system("cls")
    render(alive)
    alive = step(alive)
    time.sleep(0.1)
    if msvcrt.kbhit():
                    key = msvcrt.getch()
                    if key == b' ':
                        print("Loop is stopped")
                        break
