# Quantum-Measurement-Simulation
This Python program simulates the process of measuring the "color" (black or white) and "hardness" (hard or soft) properties of electrons. The program demonstrates the non-deterministic nature of quantum measurements.
## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Example Output](#example-output)
- [License](#license)

## Introduction

In quantum mechanics, measuring certain properties of particles like electrons can alter their state. This program simulates such a process where:

1. The color of an electron is measured first.
2. The hardness of the electron is measured next, introducing randomness.
3. The color is measured again to observe any changes.

## Installation

To run this program, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

## Usage

1. Clone or download this repository.
2. Navigate to the directory containing the script.
3. Run the script using Python.

```sh
python quantum_measurement.py
```
### Functions
The program includes the following functions:

measure_color(electron)
Input: A single electron represented by 'B' (black) or 'W' (white).
Output: Returns the color of the electron.
measure_hardness(electron)
Input: A single electron represented by 'B' (black) or 'W' (white).
Output: Randomly returns 'H' (hard) or 'S' (soft) for the electron, simulating the quantum measurement.
demonstrate_measurement_process(electrons)
Input: A list of electrons represented by 'B' or 'W'.
Output: Returns a list of tuples showing the measurement process: (color, hardness, color after hardness).
print_results(results)
Input: A list of tuples showing the measurement process.
Output: Prints the results in a readable format.

## Example Output
When you run the program, it will simulate the process for a list of input electrons (e.g., ['B', 'W', 'B', 'W']) and print the results of each measurement step.

Color -> Hardness -> Color After Hardness
B -> H -> B
W -> S -> W
B -> S -> B
W -> H -> W

i Just created this programme for fun after Superposition Lecture Of MIT Spring 2024 I to explain the concept and developing a python programme for that. :)
