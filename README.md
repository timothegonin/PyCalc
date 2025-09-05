# PyCalc - Python Calculator

## Desktop Calculator with CustomTkinte

PyCalc is a lightweight desktop calculator built with Python and CustomTkinter to provide a modern and elegant UI.
It features a grid layout with custom button handling (0 spanning two columns, . isolated, and = highlighted).

![Python](https://img.shields.io/badge/Language-Python-3776AB)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FFCC00)
![CustomTkinter](https://img.shields.io/badge/Framework-CustomTkinter-00A36C)
![Pytest](https://img.shields.io/badge/Tests-Pytest-0A9EDC)


## Features

- **Basic Calculator**: Perform addition, subtraction, multiplication, division, square, and square root.
- **Modern UI**: Styled with CustomTkinter, with distinct colors for operators, functions, and special buttons.
- **Responsive Layout:**: Grid-based, with special treatment for the 0, ., and = buttons.
---

## Prerequisites

Make sure you have installed:

- **Python**: v3.10 or later
- **pip** (comes with Python)
- **Tkinter** (included with Python on Windows/macOS, install python3-tk on Linux if missing)
---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/timothegonin/PyCalc
cd PyCalc
```

### 2. Create Virtual Environment & Install Dependencies


```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Application


```bash
python src/main.py   # or the main file inside src/
```
