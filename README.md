# 🏦 Python Console Banking System

A fully functional console-based banking system built using Python.
This project simulates how basic banking operations work including account creation, login, secure PIN verification, and transaction tracking.

---

## 🚀 Features

* Create new user account with:

  * Username
  * Strong password validation
  * 4-digit secure PIN
* Login system with password verification
* Deposit money with PIN authentication
* Withdraw money with balance check and PIN authentication
* Transfer money between users
* Transaction history for every user
* Logout system that safely returns to main menu
* Modular code structure using multiple files
* Input validation and error handling
* Soon add file handling so to avoid data loss after program exits  (adding this 10 days after i upload this on 5th Feb 2026)
---

## 🧠 Concepts Used

* Dictionaries inside dictionaries
* Modular programming (main.py, bank.py, data.py)
* Loops and input validation
* Function-based structure
* State management using `current_user`
* Basic security logic (password + pin)
* Transaction logging system
*file handling and json (soon)
---

## 📂 Project Structure

```
main.py   → Controls user flow and menu
bank.py   → All banking operations (deposit, withdraw, transfer, login)
data.py   → In-memory data storage for users and transactions
```

---

## ▶️ How to Run

Run the project using:

```
python main.py
```

---

## 📌 Note

Currently, data is stored in memory using dictionaries.
In future versions, this can be replaced with file storage or a database.

---

## 💡 Future Improvements

* File/database storage
* GUI version
* Admin panel
* Interest calculation
* Account number generation

---

## 👨‍💻 Author

Arpit Raj
Beginner Python Developer building real-world logic step by step.
