# Nand2Tetris Capstone Project

This repository contains my Nand2Tetris Capstone Project for the course **ETCCNT301**.

The project focuses on building the Hack computer, developing a Python assembler, and writing an assembly program that draws a box on the screen.

## Project Details

- **Student:** Sushant
- **Roll Number:** 2501350065
- **Course:** Nand2Tetris-I
- **K Value:** 65

## Project Structure

```text
Nand2Tetris/
│
├── Capstone/
│   ├── CPU.hdl
│   ├── Memory.hdl
│   ├── Computer.hdl
│   ├── assembler.py
│   ├── Box.asm
│   ├── Box.hack
│   ├── Add.asm
│   ├── Add.hack
│   ├── Max.asm
│   ├── Max.hack
│   ├── Rect.asm
│   ├── Rect.hack
│   ├── Pong.asm
│   ├── Pong.hack
│   └── Memory.tst
│
└── README.md
```

## Part A: Hardware Implementation

Implemented the following Hack computer chips:

- CPU
- Memory
- Computer

Tested the hardware using the Nand2Tetris Hardware Simulator.

## Part B: Python Assembler

Developed a Python-based Hack assembler that:

- Reads `.asm` assembly files.
- Performs two-pass assembly.
- Handles labels and variables.
- Converts instructions into 16-bit binary machine code.
- Displays warnings for duplicate labels.

Test programs include Add, Max, Rect and Pong.

## Part C: Draw a Box

Created `Box.asm` to draw a black box when a keyboard key is pressed and erase it when the key is released.

**Box specifications:**

- Starting row: 65
- Height: 20 rows
- Width: 32 pixels
- Starting position: Left edge of the screen

The assembly program was converted into `Box.hack` using my Python assembler and tested in the CPU Emulator.

## Technologies Used

- Hack Assembly Language
- HDL (Hardware Description Language)
- Python
- Nand2Tetris Hardware Simulator
- Nand2Tetris CPU Emulator
- Git and GitHub

## How to Run the Assembler

Run the following command from the `Capstone` directory:

```bash
python assembler.py Box.asm
```

This generates the corresponding `Box.hack` file.

## Learning Outcomes

Through this project, I learned about computer architecture, CPU and memory implementation, assembly language, machine-code translation, and the working of the Hack computer.

---

**Project completed as part of the Nand2Tetris Capstone Assignment.**
