> [!NOTE]
> This material has been created with the assistance of ChatGPT and Copilot.

# 🐍 Task G - Refactoring Data Structures → From Lists to Dictionaries **and** Objects

## 🎯 Goal

The goal of this task is to practice:

* refactoring a list-based data structure into:

  * a **dictionary (`dict`)**
  * an **object (`class`)**
* improving **code readability and maintainability**
* refactoring **without changing program behavior**
* eliminating “magic indices” such as `reservation[8]`

> [!IMPORTANT]
> **In this assignment, you must implement BOTH approaches.**
>
> * One version using **dictionaries**
> * One version using **classes (objects)**
>
> Each implementation must be in a **separate Python file**.

> [!TIP]
> Using AI tools as a coding companion is **strongly encouraged** — this reflects real-world professional practice.

---

---

## 📄 Description

You are provided with:

* a text file **`reservations.txt`**, where each line contains one reservation
* a Python script **`read_reservations.py`**, which:

  * reads `reservations.txt`
  * splits each line into a list using `split('|')`
  * processes reservations using **fixed list indices** such as `reservation[1]`, `reservation[8]`, etc.

Example of the current implementation:

```python
if reservation[8]:
    print(f"- {reservation[1]}, {reservation[9]}, {reservation[4].strftime('%d.%m.%Y')} at {reservation[5].strftime('%H.%M')}")
```

At the moment, **each reservation is represented as a list**, where fields depend on **hard-coded index positions**.

---

**Refactor the program so that:**

* **each reservation is represented in two different ways**:

  1. as a **dictionary**
  2. as an **object (class instance)**
* the rest of the code uses:

  * **dictionary keys** instead of indices
  * **object attributes and methods** instead of indices
* program output and logic remain **identical** to the original version


---

## 🔧 Data Structures

### ✅ Dictionary-Based Implementation (`task_g_dict.py`)

Each reservation must be stored as a dictionary:

```python
reservation = {
    "id": 123,
    "name": "Anna Virtanen",
    "email": "anna.virtanen@example.com",
    "phone": "0401234567",
    "date": datetime.date(...),
    "time": datetime.time(...),
    "duration": 2,
    "price": 19.95,
    "confirmed": True,
    "resource": "Conference Room A",
    "created": datetime.datetime(...),
}
```

**Usage example:**

```python
if reservation["confirmed"]:
    print(f"- {reservation['name']}, {reservation['resource']}, {reservation['date'].strftime('%d.%m.%Y')}")
```

---

## 🚀 Object-Oriented Implementation (`task_g_class.py`)

Create a class `Reservation`:

```python
class Reservation:
    def __init__(self, reservation_id, name, email, phone,
                 date, time, duration, price,
                 confirmed, resource, created):
        self.reservation_id = reservation_id
        self.name = name
        self.email = email
        self.phone = phone
        self.date = date
        self.time = time
        self.duration = duration
        self.price = price
        self.confirmed = confirmed
        self.resource = resource
        self.created = created

    def is_confirmed(self):
        return self.confirmed

    def is_long(self):
        return self.duration >= 3

    def total_price(self):
        return self.duration * self.price
```

**Usage example:**

```python
if reservation.is_confirmed():
    print(f"- {reservation.name}, {reservation.resource}, {reservation.date.strftime('%d.%m.%Y')}")
```

---

## ✅ Step-by-Step Instructions

1. Create a folder **`TaskG`** in your Git repository.
2. Copy `reservations.txt` and the original `read_reservations.py` into the folder.
3. Run the original program once and verify it works.
4. Create **two new files**:

   * `task_g_dict.py`
   * `task_g_class.py`
5. In **both files**, locate the line where a row is split into a list:

   ```python
   reservation = reservation.split('|')
   ```
6. Create a **conversion function**:

   * dictionary version:

     ```python
     def convert_reservation(data: list[str]) -> dict:
         return {
             "id": int(data[0]),
             "name": data[1],
             ...
         }
     ```
   * class version:

     ```python
     def convert_reservation(data: list[str]) -> Reservation:
         return Reservation(
             reservation_id=int(data[0]),
             name=data[1],
             ...
         )
     ```
7. Modify `fetch_reservations` so that it:

   * returns `list[dict]` in the dictionary version
   * returns `list[Reservation]` in the class version
   * does **not** include the header row
8. Replace all index-based access:

   * `reservation[1]` → `reservation["name"]` **or** `reservation.name`
   * `reservation[8]` → `reservation["confirmed"]` **or** `reservation.confirmed`
   * `reservation[6] * reservation[7]` → `reservation["duration"] * reservation["price"]`
     or `reservation.total_price()`
9. Verify that **both programs**:

   * print confirmed reservations
   * print long reservations
   * calculate total revenue (depending on base code)
10. At the **top of each file**, add a comment explaining:

    * which approach the file uses
    * why this approach is clearer than list-based indexing

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
|  ├─ 🐍 task_f.py
|  └─ 📄 2025.csv
├─ 📁 TaskG/
   ├─ 🐍 task_g_dict.py
   ├─ 🐍 task_g_class.py
   └─ 📄 reservations.txt

```

Also include a short note:

> What was the most memorable thing about this task?
