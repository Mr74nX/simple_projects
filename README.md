<div align="center">

# 🐍 Simple Python Projects

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg?style=for-the-badge)](https://www.gnu.org/licenses/gpl-2.0.html)
[![GitHub stars](https://img.shields.io/github/stars/Mr74nX/simple_projects?style=for-the-badge)](https://github.com/Mr74nX/simple_projects/stargazers)

*A collection of beginner-friendly, clean, and useful Python scripts designed for learning and quick reference.*

</div>

---

## 📌 About The Repository

This repository contains various small Python utility scripts including calculators, digital clocks, calendar utilities, and timers. It is created to help beginners understand practical implementations of built-in Python modules like `calendar`, `datetime`, `time`, and more.

---

## 🛠️ Included Projects & Features

| File Name | Description | Key Modules |
| :--- | :--- | :--- |
| `calendar.py` | Full year/month calendar viewer & day-of-week finder | `calendar`, `datetime` |
| `python_clock.py` | Real-time digital clock application | `time` / `tkinter` |
| `simple_calculator.py` | Basic arithmetic calculator for quick calculations | Standard Operators |
| `timer.py` | Countdown timer script with customizable limits | `time` |
| `voice_timer.py` | Voice-assisted timer with audio notifications | `pyttsx3` / `gTTS` |

---

## 🚀 How to Run

### Prerequisites
Make sure you have **Python 3.x** installed on your system. You can check your version using:
```bash
python --version
```

### Installation & Execution

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Mr74nX/simple_projects.git
   ```

2. **Navigate into the directory:**
   ```bash
   cd simple_projects
   ```

3. **Run any script (e.g., Calendar Script):**
   ```bash
   python calendar.py
   ```

---

## 📂 Featured Script Spotlight: Calendar & Day Finder

Here is a quick look at how the calendar utility works:

```python
import calendar
import datetime

# 1. View Full Year Calendar
year = int(input("Enter Year: "))
print("\n", calendar.calendar(year))

# 2. View Specific Month
month = int(input("Enter Month: "))
print("\n", calendar.month(year, month))

# 3. Find Day of the Week
day = int(input("Enter Day: "))
date_obj = datetime.date(year, month, day)
print("\nDay:", date_obj.strftime("%A"))
```

---

## 🤝 Contributing

Contributions are always welcome! If you have a simple Python script to add:

1. Fork the Repository
2. Create your Feature Branch (`git checkout -b feature/NewScript`)
3. Commit your Changes (`git commit -m 'Add some NewScript'`)
4. Push to the Branch (`git push origin feature/NewScript`)
5. Open a Pull Request

---

## 📜 License

Distributed under the **GPL-2.0 License**. See `LICENSE` for more information.

<div align="center">

Developed with ❤️ by **[Mr74nX](https://github.com/Mr74nX)**

</div>
