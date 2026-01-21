> [!NOTE]
> The material was created with the help of ChatGPT and Copilot.

# ⚡Task F - Three Weeks of Electricity Consumption and Production (kWh) to a File

## 🎯 Goal

The goal of this task is to extend Task D by:

* reading data from **multiple CSV files**
* computing **daily summaries for multiple weeks**
* converting energy units (**Wh → kWh**)
* formatting values using **Finnish conventions**
* writing a **clear, user-friendly report to a text file**

---

## 📄 Description

Your task is to create a Python program that:

1. **Reads data from the files** `week41.csv`, `week42.csv`, and `week43.csv`
2. **Calculates daily summaries** (Mon–Sun) for each week, similar to Task A:

   * electricity **consumption** by phase (1–3) in **kWh**
   * electricity **production** by phase (1–3) in **kWh**
3. **Writes all summaries to the file `summary.txt`** as a clear, well-structured report
   (not raw data output).

The files contain **hourly measurements** for weeks 41, 42, and 43:

* timestamp (date and time)
* consumption split into three phases (Wh)
* production split into three phases (Wh)

Your task is to **convert Wh → kWh** and present the results with **two decimal places**, using a **comma as the decimal separator** in the report.

---

## ⚖️ Unit Conversion: Wh → kWh

All values in the CSV files are in **Wh**.
In the report file (`summary.txt`), all energy values must be presented in **kWh**.

---

## 1️⃣ Program Functionality

Your program must:

1. **Read all three CSV files**:
   `week41.csv`, `week42.csv`, `week43.csv`
2. **Calculate daily totals for each week** (41, 42, 43), including:

   * weekday name in Finnish (monday, tuesday, …)
   * date in format **dd.mm.yyyy** (e.g., `13.10.2025`)
   * consumption by phase 1–3 (kWh, two decimals, comma decimal separator)
   * production by phase 1–3 (kWh, two decimals, comma decimal separator)
3. **Write the summaries to `summary.txt`** following these principles:

* Each week must have a **clear heading**, for example:

```text
Week 41 electricity consumption and production (kWh, by phase)
Day         Date        Consumption [kWh]            Production [kWh]
                         v1      v2      v3          v1      v2      v3
---------------------------------------------------------------------------
monday   06.10.2025  12,35   1,56    2,78         0,01   0,39    0,52
tuesday     07.10.2025  ...
...
sunday   12.10.2025  ...
```

* Use the **same structure for weeks 42 and 43** within the same report.
* At the end of the report, you **may** include a **short summary of all weeks combined**
  (total consumption and production), if it simplifies your program design
  or if you implement it as a bonus feature ⭐.

The exact wording is not fixed, but the report must be:

* **easy to read**
* **logical**
* **clearly structured** (headings, table-like rows, separate sections per week)

---

## 2️⃣ Use of Functions (Mandatory)

The program must be built around **functions**, not written entirely at the top level.

Include at least:

* a function to read a CSV file, for example:

```python
def read_data(filename: str) -> list:
    """Reads a CSV file and returns the rows in a suitable structure."""
    ...
```

* a function that calculates **daily summaries** for one week
* a function that **formats report rows** as strings
* a function that **writes the report** to `summary.txt`

Also include a **main function**, for example:

```python
def main() -> None:
    """Main function: reads data, computes weekly summaries, and writes the report to a file."""
    ...
```

And at the end:

```python
if __name__ == "__main__":
    main()
```

---

### 📚 Docstring Requirement

Every function must include a **docstring** that briefly and clearly explains what the function does.

```python
def example(value: int) -> float:
    """Converts an integer to a float and returns the value multiplied by ten."""
    ...
```

---

### 🔤 Type Hints (Required)

All functions must use **type hints**:

* parameter types
* return type

Example:

```python
from datetime import datetime
from typing import List, Dict

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
If you use conditionals (`if`) or comparisons involving dates or times, **do not compare raw strings**.
Use proper data types such as `datetime` and `date`.

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

## 5️⃣ Finnish Formatting Conventions 🇫🇮

In the report file (`summary.txt`):

### 1. Date format

* Format: **dd.mm.yyyy**
* Example: `13.10.2025`

```python
date_str = f"{day.day}.{day.month}.{day.year}"
```

### 2. Decimal numbers (kWh values)

* Use a **comma** as the decimal separator
* Round to **two decimal places**

```python
value_kwh = 1.2345
value_str = f"{value_kwh:.2f}"          # "1.23"
value_str = value_str.replace(".", ",") # "1,23"
```

---

## 6️⃣ Basic Programming Structures (Mandatory)

Your program must include at least:

* **variables** (e.g. daily totals, weekly totals)
* **lists or other data structures** (e.g. lists of weekdays)
* **loops** (`for`) to iterate over rows and days
* **conditionals** (`if`), especially for:

  * grouping or selecting days
  * **optionally** identifying the “best / worst” day
* **functions** that include:

  * docstrings
  * type hints

Additionally, you must use:

* **file writing** with a `with` statement, for example:

```python
with open("summary.txt", "w", encoding="utf-8") as file:
    ...
```

This ensures the file is **always properly closed**.

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
   ├─ 🐍 task_e.py
   ├─ 📄 week41.csv
   ├─ 📄 week42.csv
   └─ 📄 week43.csv

```

Also include a short note:

> What was the most memorable thing about this task?