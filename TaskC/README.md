> [!NOTE]
> The material was created with the help of ChatGPT and Copilot.

# 🐍 Task C - Handling Reservation Data

## 🎯 Goal

The goal of this task is to practice:

*   type conversions in Python using a separate function
*   working with lists and structuring reservation data
*   printing reservation data using loops and conditional statements

***

## 📄 Description

You are given:

*   a text file **`reservations.txt`**, where each line contains the details of one reservation.
*   a Python script **`read_reservations.py`**, which includes pre-built functionality for reading reservations (including the function `convert_reservation_data`).

> [!NOTE]
> **You are not allowed to alter the reservations.txt file in this task!**

**Example line from `reservations.txt`:**

    201|Moomin Valley|moomin@whitevalley.org|0509876543|2025-11-12|09:00|2|18.50|True|Forest Area 1|2025-08-12 14:33:20

The line contains the following fields:

| Column                | Description           | Target Data Type    |
| --------------------- | --------------------- | ------------------- |
| 1  `reservationId`    | Reservation number    | `int`               |
| 2  `name`             | Name of reserver      | `str`               |
| 3  `email`            | Email address         | `str`               |
| 4  `phone`            | Phone number          | `str`               |
| 5  `reservationDate`  | Reservation date      | `datetime.date`     |
| 6  `reservationTime`  | Start time            | `datetime.time`     |
| 7  `durationHours`    | Duration in hours     | `int`               |
| 8  `price`            | Hourly price (€)      | `float`             |
| 9  `confirmed`        | Confirmed             | `bool`              |
| 10 `reservedResource` | Reserved resource     | `str`               |
| 11 `createdAt`        | When reservation made | `datetime.datetime` |

***

## 🧠 Part A: Fix `convert_reservation_data`

In this part, focus on converting a single reservation line into the correct data types.

> [!TIP]  
> Unlike previous tasks, here the function performs the conversion immediately after reading, and the program continues with the converted data.

***

### 1️⃣ Preparation

1.  Copy the file **`reservations.txt`** into your own Git repository under the folder `TaskC`.
2.  Copy the Python script **`read_reservations.py`** into the same `TaskC` folder.
3.  Rename the Python script file to **`task_c.py`**
4.  Make sure the program runs with the command → `the program prints reservations and unconverted data types`:

    ```bash
    python task_c.py
    ```

***

### 2️⃣ The `convert_reservation_data` Function

The script contains a function called **`convert_reservation_data`**, which receives as a parameter **a list split from one line**. Example:

```python
["201", "Moomin Valley", "moomin@whitevalley.org", "0509876543", "2025-11-12", "09:00:00", "2", "18.50", "True", "Forest Area 1", "2025-08-12 14:33:20"]
```

**Your task is to modify the function `convert_reservation_data` so that it returns a list where the columns have the following data types:**

```text
reservationId | name | email | phone | reservationDate | reservationTime | durationHours | price | confirmed | reservedResource | createdAt

int | str | str | str | date | time | int | float | bool | str | datetime
```

> [!TIP]  
> Use Python’s `datetime` library:

```python
from datetime import datetime, date, time
```

> [!TIP]  
> Examples of conversions (adapt to your code):

```python
# 1) reservationId: str -> int
reservation_id = int(row[0])

# 5) reservationDate: "2025-11-12" -> datetime.date
reservation_date = datetime.strptime(row[4], "%Y-%m-%d").date()

# 6) reservationTime: "09:00" -> datetime.time
reservation_time = datetime.strptime(row[5], "%H:%M").time()

# 8) price: "18.50" -> float
price = float(row[7])

# 9) confirmed: "True"/"False" -> bool
confirmed = (row[8] == "True")

# 11) createdAt: "2025-08-12 14:33:20" -> datetime.datetime
created_at = datetime.strptime(row[10], "%Y-%m-%d %H:%M:%S")
```

Finally, the function should return a list where all fields are in the correct order and data types.

> [!TIP]  
> Example (you don’t have to use these exact variable names or this approach, but the idea is the same):

```python
return [
    reservation_id, name, email, phone,
    reservation_date, reservation_time,
    duration_hours, price,
    confirmed, reserved_resource,
    created_at
]
```

***

### 3️⃣ Testing

Make sure the program runs with the command → `the program prints reservations and converted data types`:

```bash
python task_c.py
```

***

### 🧩 Tips

*   Make conversions **in small steps**:
    *   first `int` and `float`
    *   then `bool`
    *   finally `datetime.date`, `datetime.time`, and `datetime`
*   If `datetime.strptime` throws an error, check carefully:
    *   what the string looks like in the file
    *   that the format string (`"%Y-%m-%d %H:%M:%S"`) matches exactly
*   You can add temporary `print` statements for debugging (e.g., `print(row[4], type(reservation_date))`).

***

## 🧠 Part B: Processing Reservations with Loops and Conditionals

In this part, build a program that prints **five different summaries** of reservations in one run. All outputs should appear **in the same program execution (i.e., when running `python read_reservations.py`, everything prints in order 1–5)**.

> [!IMPORTANT]  
> Output from Part A is not required for submission. Only the outputs from Part B should be included in the screenshot you submit.

***

### 🧩 Tips

*   Progress in small steps, testing after each change.

***

### 1️⃣ Output: All Confirmed Reservations

Header:

```
1) Confirmed Reservations
```

Each reservation should print in this format:

```
- Name, Reserved Resource, dd.mm.yyyy at hh.mm
```

Example:

```
1) Confirmed Reservations
- Moomin Valley, Forest Area 1, 12.11.2025 at 09.00
- Little My Storm, Red Room, 22.10.2025 at 15.45
```

***

### 2️⃣ Output: Long Reservations (duration ≥ 3 h)

Header:

```
2) Long Reservations (≥ 3 h)
```

Format:

```
- Name, dd.mm.yyyy at hh.mm, duration X h, Reserved Resource
```

***

### 3️⃣ Output: Reservation Confirmation Status

Header:

```
3) Reservation Confirmation Status
```

Format:

```
Name → Confirmed
Name → NOT Confirmed
```

***

### 4️⃣ Output: Summary of Confirmed vs Not Confirmed

Header:

```
4) Confirmation Summary
```

Format:

```
- Confirmed reservations: X pcs
- Not confirmed reservations: Y pcs
```

***

### 5️⃣ Output: Total Revenue from Confirmed Reservations (with comma!)

Header:

```
5) Total Revenue from Confirmed Reservations
```

Format:

```
Total revenue from confirmed reservations: 243,50 €
```

Note the comma in the amount:

```python
amount_str = f"{amount:.2f}".replace(".", ",")
```

***

### 🔍 What the Full Output must Look Like

> This is just an example, not the actual content of the file.

```
1) Confirmed Reservations
- Moomin Valley, Forest Area 1, 12.11.2025 at 09.00
- Hemulen Plant Collector, Botanical Lab, 05.11.2025 at 10.30

2) Long Reservations (≥ 3 h)
- Little My Storm, 22.10.2025 at 15.45, duration 3 h, Red Room
- Sniff Moneywise, 18.09.2025 at 13.00, duration 4 h, Storage Area N

3) Reservation Confirmation Status
Moomin Valley → Confirmed
Snork Maiden → NOT Confirmed
Little My Storm → Confirmed

4) Confirmation Summary
- Confirmed reservations: 1 pcs
- Not confirmed reservations: 2 pcs

5) Total Revenue from Confirmed Reservations
Total revenue from confirmed reservations: 123,50 €
```

***

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
   ├─ 🐍 task_c.py
   └─ 📄 reservations.txt

```


Also include a short note:

> What was the most memorable thing about this task?

---

## 💬 Grading Criteria (points):
* **`0:`** The program does not work and/or its structure has been significantly altered. The file names are incorrect.
* **`1:`** The program works, but the output does not meet the requirements, and the correct data types and/or functions have not been used.
* **`2:`** The program produces the required output and uses the correct data types and functions. The program structure follows the given task.

---

## 💡 Most Common Errors and Solutions

| Error            | Cause                             | Solution                               |
| ---------------- | --------------------------------- | -------------------------------------- |
| “File not found” | Script is run in the wrong folder | Move to the folder where the script is |
| “File not found” | Files haven’t been copied         | Copy the files into your folder        |
| “File not found” | Files are misnamed                | Verify the file names are correct      |

---