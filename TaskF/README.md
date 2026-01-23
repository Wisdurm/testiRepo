> [!NOTE]
> The material was created with the help of ChatGPT and Copilot.

# ⚡ Task F -  Annual Electricity Consumption Reporting

## 🎯 Goal

The goal of this task is to build an **interactive report generator** in Python that:

* reads a full year of hourly measurement data from a CSV file
* uses **input-driven menus** so the user can choose different report types
* calculates summaries on daily, monthly, or yearly level
* prints the report in a clear format in the console
* optionally writes the report to a file (`report.txt`) based on the user’s choice

---

## 📄 Task Description

Create a Python program that:

1. **Reads data from the file `2025.csv`**
2. Provides the user with a **menu using input commands**, where the user can select different reports
3. **Calculates the selected report type**
   (e.g., date-range daily summary, monthly summary, full-year summary)
4. **Prints the report to the console** as clear text
5. After printing a report, asks the user:

   * `1) Write the report to the file report.txt`
   * `2) Create a new report`
   * `3) Exit`

   and behaves according to the choice
6. Writes the report to the file **`report.txt`** if the user chooses option 1

   * the filename is **always the same** (`report.txt`)
   * a new report **overwrites** the old one

The file `2025.csv` contains hourly measurements for the year 2025:

* timestamp (date and time)
* consumption (net) in kWh
* production (net) in kWh
* daily average temperature

The goal is to build an **interactive tool-like program** that feels more like a real utility than a one-off script.

---

## ⚖️ Units and Formatting Rules

Values in the file are already in **kWh**. In your report you must ensure:

* **Decimal values** are shown with **two decimal places**, using a **comma** as the decimal separator
* **Dates** are shown in format **dd.mm.yyyy** (e.g., `13.10.2025`)
* The report uses **clear headings and table-like formatting** so the content is easy to understand

---

## 1️⃣ Program Functionality

Your program must:

1. **Read the CSV file** `2025.csv`.
2. Convert rows into a structure that makes it easy to compute summaries on:

   * daily level
   * monthly level
   * yearly level
     (for example: lists, dictionaries, etc.)
3. Show the user a **main menu**, for example:

```text
Choose a report type:
1) Daily summary for a date range
2) Monthly summary for one month
3) Full year 2025 summary
4) Exit the program
```

4. Ask for any required extra inputs based on the selection (see below).
5. Calculate and print the **report to the console**.
6. After printing, show a **second menu**:

```text
What would you like to do next?
1) Write the report to the file report.txt
2) Create a new report
3) Exit
```

* If the user selects **1**, write the **just-created report** to `report.txt`.
* If the user selects **2**, return to the main report menu.
* If the user selects **3**, exit the program.

The program runs in a **loop** until the user decides to stop. 🔁

---

## 📅 Report 1: Daily Summary for a Date Range

Ask the user:

* **Start date**: `Enter start date (dd.mm.yyyy):`
* **End date**: `Enter end date (dd.mm.yyyy):`

The report must include:

* the date range (dd.mm.yyyy–dd.mm.yyyy)
* total consumption for the range (kWh, two decimals, comma decimal separator)
* total production for the range (kWh, two decimals, comma decimal separator)
* average temperature for the range
  (for example: average of all hourly temperature values)

---

## 📆 Report 2: Monthly Summary

Ask the user:

* **Month number** (1–12), for example: `Enter month number (1–12):`

The report must include:

* the month
* total consumption for the month (kWh)
* total production for the month (kWh)
* average daily temperature for the month

---

## 📊 Report 3: Full Year 2025 Summary

The report must include:

* total consumption for 2025 (kWh)
* total production for 2025 (kWh)
* average temperature for the year

---

## 2️⃣ Use of Functions (Mandatory)

The program must be built around **functions**, not written entirely at the top level.

You may use functions like these:

```python
def read_data(filename: str) -> list:
    """Reads a CSV file and returns the rows in a suitable structure."""
    ...

def show_main_menu() -> str:
    """Prints the main menu and returns the user selection as a string."""
    ...

def create_daily_report(data: list) -> list[str]:
    """Builds a daily report for a selected date range."""
    ...

def create_monthly_report(data: list) -> list[str]:
    """Builds a monthly summary report for a selected month."""
    ...

def create_yearly_report(data: list) -> list[str]:
    """Builds a full-year summary report."""
    ...

def print_report_to_console(lines: list[str]) -> None:
    """Prints report lines to the console."""
    ...

def write_report_to_file(lines: list[str]) -> None:
    """Writes report lines to the file report.txt."""
    ...
```

Also include a **main function**, for example:

```python
def main() -> None:
    """Main function: reads data, shows menus, and controls report generation."""
    ...
```

And at the end:

```python
if __name__ == "__main__":
    main()
```

---

### 📚 Docstring Requirement

Every function must include a **docstring** that clearly describes what the function does.

---

### 🧾 Type Hints (Required)

All functions must include **type hints**:

* parameter types
* return type

Example:

```python
from datetime import datetime, date
from typing import List

def convert_time(time_str: str) -> datetime:
    """Converts an ISO-formatted timestamp string into a datetime object."""
    ...
```

---

## 3️⃣ MIT Copyright Header

At the top of the Python file, include:

```python
# Copyright (c) 2025 Your Name
# License: MIT
```

---

## 4️⃣ Dates and Times – Use Data Types, Not Strings

**Important principle:**
When using conditionals (`if`) or comparisons with dates/times, **do not compare raw strings**.
Use correct data types (`datetime`, `date`).

❌ Bad example (string comparison):

```python
if time_str[:10] == "2025-10-13":
    ...
```

✅ Better example:

```python
from datetime import datetime, date

dt = datetime.fromisoformat(time_str)  # e.g. "2025-10-13T00:00:00"
day = dt.date()

if day == date(2025, 10, 13):
    ...
```

---

## 5️⃣ Finnish Formatting Emphasis 🇫🇮

In the report (`report.txt`) and in the console:

### 1. Date format

* Format: **dd.mm.yyyy**
* Example: `13.10.2025`

```python
date_str = f"{day.day}.{day.month}.{day.year}"
```

### 2. Decimal values (kWh)

* Use a **comma**, not a dot
* Round to **two decimals**

```python
value_kwh = 1.2345
value_str = f"{value_kwh:.2f}"          # "1.23"
value_str = value_str.replace(".", ",") # "1,23"
```

---

## 6️⃣ Basic Programming Structures (Mandatory)

Your program must include at least:

* **variables** (e.g., daily totals, monthly totals)
* **lists or other data structures** (e.g., list of measurements, list of report lines)
* **loops** (`for`, and if needed `while`) to iterate through rows, days, and months
* **conditionals** (`if`), especially for:

  * handling menu and input selections
  * selecting dates and months
* **functions** with:

  * docstrings
  * type hints

Additionally required:

* **file writing** using `with`, for example:

```python
with open("report.txt", "w", encoding="utf-8") as file:
    ...
```

* **inputs** that allow the user to control the program (menus, dates, months)

---

## 📤 Submission Instructions to Itslearning

Submit a **link to your GitHub repo** and a **screenshot of the console** showing the program execution and output.

The folder structure of the Github repo must be as follows:

```
📁 Github Repo/
├─ 📁 TaskA/
|  ├─ 🐍 task_a.py
|  └─ 📄 reservations.txt
├─ 📁 TaskB/
|  ├─ 🐍 task_b.py
|  └─ 📄 reservations.txt
├─ 📁 TaskC/
|  ├─ 🐍 task_c.py
|  └─ 📄 reservations.txt
├─ 📁 TaskD/
|  ├─ 🐍 task_d.py
|  └─ 📄 week42.csv
├─ 📁 TaskE/
|  ├─ 🐍 task_e.py
|  ├─ 📄 week41.csv
|  ├─ 📄 week42.csv
|  └─ 📄 week43.csv
├─ 📁 TaskF/
   ├─ 🐍 task_f.py
   └─ 📄 2025.csv

```

Also include a short note:

> What was the most memorable thing about this task?
