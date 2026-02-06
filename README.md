# 🧬 Conway’s Game of Life (Python)

A terminal-based implementation of **Conway’s Game of Life**, written in Python.  
This project focuses on grid-based state management, neighbor evaluation logic, and basic testing.

---

## 📌 Project Overview

Conway’s Game of Life is a cellular automaton where cells evolve over time based on simple rules and their neighboring cells.

This project demonstrates:
- 2D grid data structures
- Rule-based state transitions
- Defensive copying to avoid mutation bugs
- Terminal rendering
- Basic automated testing

---

## ⚙️ Rules of the Game

Each cell is either **alive (1)** or **dead (0)**:

- Any live cell with fewer than 2 live neighbors dies (underpopulation)
- Any live cell with 2 or 3 live neighbors survives
- Any live cell with more than 3 live neighbors dies (overpopulation)
- Any dead cell with exactly 3 live neighbors becomes alive (reproduction)

---

## ▶️ How to Run

### Run the simulation:
```bash
python life.py 
``` 
- The board updates every second
- Press q to quit the simulation

### Run test
python test.py

### 🧪 Tests Included

Current tests cover:
- Dead cells remaining dead with no neighbors
- Dead cells becoming alive with exactly three neighbors
- Tests ensure that the game rules are applied correctly.

---

## 📝 Project Notes & Learning Context

This project was inspired by the **Project-Based Learning** repository curated by the open-source community:  
https://github.com/practical-tutorials/project-based-learning

The goal was to practice implementing a well-known problem independently while applying core programming concepts such as grid-based logic, state transitions, and testing.

Additionally, prior experience designing **grid-based game logic** (inspired by tactical games like *Fire Emblem*)
-https://github.com/arland13/turn-based-tactical-rpg/blob/main/core/maps/grid.py-
helped significantly in understanding and structuring this simulation.