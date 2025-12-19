# 📚 Book Inventory Management System

## 📌 Overview
The **Book Inventory Management System** is a Python & MySQL-based application that allows users to manage book records efficiently.  
It provides essential CRUD operations (Create, Read, Update, Delete) and helps maintain a structured inventory of books.

---

## 🚀 Features
- **Create Books Table** — Automatically creates the table if it doesn’t exist.
- **Add Books** — Insert new books into the inventory.
- **Search Books** — Search by Title, Author, or ISBN.
- **Update Quantity** — Modify stock levels of existing books.
- **View Inventory** — Display all books stored in the database.
- **User-Friendly Menu** — Simple command-line interface for easy navigation.

---

## 🛠️ Technologies Used
- **Python**
  - MySQL Connector
  - Exception Handling
- **MySQL**
  - Database storage
  - Structured querying

---

## 📦 Prerequisites
- Python 3+
- MySQL Server installed & running
- Required Python package:
  ```bash
  pip install mysql-connector-python
  ```

---

## 🗄️ Database Setup
### 1️⃣ Create the database in MySQL:
```sql
CREATE DATABASE book_inventory;
```

### 2️⃣ Update credentials inside `book_inventory.py`:
```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="book_inventory"
)
```

---

## ▶️ Running the Project
1. Make sure MySQL Server is running.
2. Execute the Python script:
   ```bash
   python book_inventory.py
   ```
3. Follow on-screen menu options to add, search, update, or view books.

---

## 📘 Usage Instructions
- **Add a Book:** Input `Title, Author, ISBN, Quantity`
- **Search a Book:** Enter the title, author, or ISBN  
- **Update Quantity:** Enter `Book ID` and the new quantity  
- **View Inventory:** Shows all stored books  
- **Exit:** Press option `5`  

---

## 🔧 Future Enhancements
- GUI-based interface  
- User authentication system  
- Report generation for stock analysis  
- Export data to CSV or Excel  

---

## 📄 License
This project is **open-source** and completely free to use.

---

## ✍️ Author
**Gourang Dhote**  
📧 *gourang6102003@gmail.com*

Feel free to contribute, suggest improvements, or report issues!
