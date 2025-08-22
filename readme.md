# **Banking System with Thread Safety in Python**

This project implements a **multi-threaded banking system** in Python, featuring account management, secure transactions, and data persistence using JSON. It adheres to **OOP principles** with layered architecture, including validation, user management, and data access modules.

---

## **Features**

* ✅ **Object-Oriented Design** using abstract base classes.
* ✅ **Account Management**:

  * Add and delete users.
  * Login and logout functionality.
* ✅ **Banking Operations**:

  * Deposit and withdraw funds.
  * Transfer funds between accounts (PIN verification).
* ✅ **Data Persistence**:

  * Store users and bank metadata in JSON files.
* ✅ **Validation**:

  * Validates name, email, phone number, IBAN, and PIN formats using regex.
* ✅ **Thread Safety**:

  * Supports concurrent operations using **threading** with locks.
* ✅ **Menu-Driven CLI**:

  * Interactive console for performing banking operations.

---

## **Project Structure**

```
src/
├── people/
│   ├── person.py       # Abstract base class for Person
│   └── user.py         # User class (inherits Person)
├── server/
│   ├── bank.py         # Bank class handling operations
│   └── data_access.py  # Handles JSON file storage
├── data/
│   ├── user_data.json  # Stores user details
│   └── bank_data.json  # Stores last account number
└── main.py             # CLI menu to interact with the system
```

---

## **Prerequisites**

* No external dependencies (uses only standard library).

---

## **How It Works**

### **1. User Validation**

* **Name**: Alphabets and spaces only.
* **Email**: Standard email format (`abc@xyz.com`).
* **Phone Number**: Format `+923XXXXXXXXX`.
* **IBAN**: Starts with `PKABCC` followed by 16 digits.
* **PIN**: 4 digits.

---

### **2. Data Persistence**

* Users are stored in `user_data.json` as:

```json
[
    {
        "name": "Ali Khan",
        "email": "ali.khan@example.com",
        "ph_num": "+923001234567",
        "IBAN": "PKABCC10000000000001",
        "PIN": "1234",
        "Balance": 50000
    }
]
```

* Bank metadata (`bank_data.json`):

```json
{
    "last_account_number": 10000000000001
}
```

---

### **3. Supported Operations**

* **Add User**: Creates an account with IBAN and initial balance.
* **Delete User**: Removes an account.
* **Login/Logout**: Authenticates users for secure transactions.
* **Deposit/Withdraw**: Updates account balance.
* **Transfer**: Transfers funds between accounts after PIN verification.
* **View Details**: Displays account info (only if logged in).

---

## **Run the Application**

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd <project-folder>
   ```

2. Ensure file paths for `user_data.json` and `bank_data.json` exist:

   ```
   D:/Task 2/src/server/data/
   ```

3. Run the program:

   ```bash
   python main.py
   ```

---

## **Threading**

* Each user operation is handled using `threading.Thread` to simulate real-world concurrent banking transactions.
* Critical sections (modifying shared state) are protected using `threading.Lock`.

---

## **Future Enhancements**

* ✅ Add **unit tests** using `unittest` or `pytest`.
* ✅ Replace JSON with a **database** (SQLite/PostgreSQL).
* ✅ Add **Flask API** for web-based banking.
* ✅ Implement **encryption** for storing PIN securely.

---

### **Author**

Developed by **Inam Ullah Shaikh**