> [!NOTE]
> The material was created with the help of ChatGPT and Copilot. 

# ⚡ Task D - Weekly Electricity Consumption and Production (kWh) in the Console

## 🎯 Goal

The goal of this task is to practice:

* reading CSV data from a file
* converting units (**Wh → kWh**)
* grouping data by day (Mon–Sun)
* using functions with **docstrings** and **type hints**
* printing a clear, user-friendly table in the console

---

## 📄 Description

You are given:

* a CSV file **`week42.csv`** that contains **hourly measurements** for **week 42** (Mon–Sun)
* each row includes:

  * timestamp (date + time)
  * electricity **consumption** in three phases (Wh)
  * electricity **production** in three phases (Wh)

Your task is to:

1. **Read the data from `week42.csv`.** using script **`task_d.py`**
2. **Calculate daily totals** (Mon–Sun) for:

   * consumption phase 1–3 (**kWh**)
   * production phase 1–3 (**kWh**)
3. **Print the results to the console as a clear table.**

> [!NOTE]
> **You are not allowed to alter the week42.csv file in this task!**

---

## ⚖️ Unit Conversion: Wh → kWh

The file values are in **Wh**. In your output, all energy values must be shown in **kWh**.

* Conversion: `kWh = Wh / 1000`
* Print using **two decimals**
* Use a **comma as the decimal separator** in the output (Finnish formatting)

---

## ✅ Program Requirements

### 1️⃣ Console Output (Required)

Your program must print a **user-friendly table** that shows:

* weekday name **in Finnish** (monday, tuesday, …)
* date in format **dd.mm.yyyy** (e.g., `13.10.2025`)
* consumption phases v1–v3 in **kWh** (two decimals, comma decimal separator)
* production phases v1–v3 in **kWh** (two decimals, comma decimal separator)

Example structure (you may adjust formatting, but keep it readable):

```text
Week 42 electricity consumption and production (kWh, by phase)

Day          Date        Consumption [kWh]               Production [kWh]
            (dd.mm.yyyy)  v1      v2      v3             v1     v2     v3
---------------------------------------------------------------------------
monday       13.10.2025   12,35   1,56    2,78           0,01   0,39   0,52
tuesday      14.10.2025   ...     ...     ...            ...    ...    ...
...
sunday       19.10.2025   ...     ...     ...            ...    ...    ...
```

---

### 2️⃣ Functions Only (Required)

Your program must be built around **functions** (not “everything at the top level”).

Include at least:

* a function that reads the CSV data, for example:

```python
def read_data(filename: str) -> list:
    """Reads the CSV file and returns the rows in a suitable structure."""
    ...
```

* a `main()` function, for example:

```python
def main() -> None:
    """Main function: reads data, computes daily totals, and prints the report."""
    ...
```

* and at the end:

```python
if __name__ == "__main__":
    main()
```

### 📚 Docstring Requirement

Every function must have a **docstring** that clearly explains what the function does.

### 🔤 Type Hints (Required)

All functions must include **type hints** for:

* parameter types
* return type

---

### 3️⃣ MIT Copyright Header (Required)

At the top of your Python file, include:

```python
# Copyright (c) 2025 Your Name
# License: MIT
```

---

### 4️⃣ Dates and Times as Data Types (Required)

If you use conditions (`if`) or comparisons involving dates/times:

* **Do not** compare raw strings
* Use real data types: `datetime`, `date`

❌ Bad example (string comparison):

```python
if time_str[:10] == "2025-10-13":
    ...
```

✅ Better example:

```python
from datetime import datetime, date

dt = datetime.fromisoformat(time_str)  # e.g., "2025-10-13T00:00:00"
d = dt.date()

if d == date(2025, 10, 13):
    ...
```

---

### 5️⃣ Finnish Formatting Emphasis 🇫🇮

#### Date format

* Output date must be: `dd.mm.yyyy`
  Example: `13.10.2025`

#### Decimal comma

* Output decimals must use a **comma**, not a dot:

```python
value_str = f"{value_kwh:.2f}".replace(".", ",")
```

---

### 6️⃣ Basic Programming Structures (Required)

Your solution must include at least:

* variables (e.g., daily totals)
* lists or other data structures
* loops (`for`) to process rows and days
* conditionals (`if`) for grouping and/or selecting data
* functions with docstrings and type hints

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
   ├─ 🐍 task_d.py
   └─ 📄 week42.csv

```

Also include a short note:

> What was the most memorable thing about this task?

---

## 💬 Grading Criteria (0–2 points)

* **`0:`** The program does not work. File names are incorrect.
* **`1:`** The program runs, but the output does not meet the requirements and/or required data types/functions are missing.
* **`2:`** The program produces the required output and uses correct data types and functions. The program structure follows the given task. 

---
