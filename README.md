# 🖱️ Mouse Bot - Python Automation

![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)
![PyAutoGUI](https://img.shields.io/badge/Library-PyAutoGUI-green?style=for-the-badge)

A simple Python-based automation tool designed to simulate random mouse movements and clicks. It includes a safety fail-safe and an acoustic alarm when the execution is interrupted.

## 📋 Summary
- [Technologies](#-technologies)
- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [What I learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)
- [How to Run](#-how-to-run)

---

## 🛠 Technologies
- **Python 3.x**: Core logic and execution.
- **PyAutoGUI**: For controlling mouse movement and click events.
- **Playsound3**: To trigger audio alerts.
- **Built-in Libraries**: `os` for path handling, `time` for execution delays, and `random` for coordinate generation.

## ✨ Features
- **Random Movement:** Generates random coordinates within a specific range (X: 200-1200, Y: 200-650) to keep the cursor active.
- **Interactive Input:** Prompts the user in the terminal to choose whether the bot should perform clicks (`Y/N`) before starting.
- **Fail-Safe System:** Uses PyAutoGUI's built-in fail-safe. Moving the mouse to any corner of the screen safely stops the script.
- **Audio Alert:** Automatically plays an `alarm.mp3` file when the `FailSafeException` is triggered.

## 📂 Project Architecture
The project is organized into specific archives:
* `mouse_bot.py`: The main entry point containing the automation loop, coordinate logic, and exception handling.
* `alarm.mp3`: The audio file required in the same directory to be played upon script termination.

## 📚 What I Learned
* **Automation Basics:** Handling mouse events and movements programmatically.
* **Exception Handling:** Using `try/except` blocks to manage graceful exits (catching `pyautogui.FailSafeException`).
* **Path Management:** Dynamically resolving absolute file paths using the `os` module to ensure the alarm plays regardless of where the script is called from.

## 🔮 Future Improvements
- [ ] GUI for setting coordinate boundaries and sleep timers.
- [ ] Support for multiple monitor setups.
- [ ] Add customized movement patterns (e.g., circles or squares).

## 🚀 How to Run

**Install dependencies:**
   This project requires `pyautogui` and `playsound3`. Install them via pip:
   ```bash
   pip install pyautogui playsound3
