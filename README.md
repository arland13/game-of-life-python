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

## 🗂️ Project Structure

