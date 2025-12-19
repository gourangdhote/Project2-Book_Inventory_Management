import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

# Database credentials (replace with your own)
mydb = mysql.connector.connect(
  host=os.getenv('DB_HOST', 'localhost'),
  user=os.getenv('DB_USER', 'root'),
  password=os.getenv('DB_PASSWORD'),
  database=os.getenv('DB_NAME', 'book_inventory')
)


mycursor = mydb.cursor()


def create_table():
    try:
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255),
                isbn VARCHAR(20) UNIQUE,
                quantity INT DEFAULT 0
            )
        """)
        mydb.commit()
        print("Books table created (or already exists).")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")


def add_book(title, author, isbn, quantity):
    try:
        sql = "INSERT INTO books (title, author, isbn, quantity) VALUES (%s, %s, %s, %s)"
        val = (title, author, isbn, quantity)
        mycursor.execute(sql, val)
        mydb.commit()
        print(f"Book '{title}' added successfully.")
    except mysql.connector.Error as err:
        print(f"Error adding book: {err}")


def search_books(query):
    try:
        sql = "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s OR isbn LIKE %s"
        val = (f"%{query}%", f"%{query}%", f"%{query}%")
        mycursor.execute(sql, val)
        results = mycursor.fetchall()
        if results:
            print("Search results:")
            for book in results:
                print(book)
        else:
            print("No books found matching your search.")
    except mysql.connector.Error as err:
        print(f"Error searching books: {err}")


def update_quantity(book_id, new_quantity):
    try:
        sql = "UPDATE books SET quantity = %s WHERE id = %s"
        val = (new_quantity, book_id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(f"Quantity for book ID {book_id} updated to {new_quantity}.")
    except mysql.connector.Error as err:
        print(f"Error updating quantity: {err}")


def view_inventory():
    try:
        mycursor.execute("SELECT * FROM books")
        books = mycursor.fetchall()
        if books:
            print("Book Inventory:")
            for book in books:
                print(book)
        else:
            print("Inventory is empty.")
    except mysql.connector.Error as err:
        print(f"Error viewing inventory: {err}")

def generate_summary_statistics():
    """Generate basic inventory statistics - DATA SCIENCE FEATURE"""
    try:
        # Total books and categories
        mycursor.execute("""
            SELECT 
                COUNT(*) as total_titles,
                SUM(quantity) as total_books,
                COUNT(DISTINCT author) as unique_authors,
                AVG(quantity) as avg_quantity
            FROM books
        """)
        stats = mycursor.fetchone()
        
        # Category breakdown
        mycursor.execute("""
            SELECT author, COUNT(*) as book_count, SUM(quantity) as total_qty
            FROM books 
            GROUP BY author
            ORDER BY book_count DESC
            LIMIT 5
        """)
        top_authors = mycursor.fetchall()
        
        print("\n" + "="*60)
        print("INVENTORY STATISTICS")
        print("="*60)
        print(f"Total Unique Titles: {stats[0]}")
        print(f"Total Books in Stock: {stats[1]}")
        print(f"Unique Authors: {stats[2]}")
        print(f"Average Quantity per Title: {stats[3]:.2f}")
        print("\nTop 5 Authors by Book Count:")
        for author in top_authors:
            print(f"  - {author[0]}: {author[1]} titles, {author[2]} books")
        print("="*60)
        
    except mysql.connector.Error as err:
        print(f"Error generating statistics: {err}")

create_table()
print("WELCOME TO LIBRARY !")

while True:
    print("\nMENU:"
          "\n1 - FOR ADDING A BOOK"
          "\n2 - FOR SEARCHING A BOOK"
          "\n3 - FOR UPDATING QUANTITY OF A BOOK"
          "\n4 - FOR VIEWING THE INVENTORY"
          "\n5 - FOR GENERATING SUMMARY STATISTICS"
          "\n6 - TO EXIT")

    try:
        user_input = input("YOUR CHOICE: ")
        user_input = int(user_input)
        if user_input == 1:
            try:
                title, author, isbn, quantity = map(str, (x.strip() for x in (input("PLEASE ENTER TITLE, AUTHOR, ISBN, QUANTITY - ").split(","))))
                add_book(title, author, isbn, quantity)
            except ValueError:
                print("INVALID INPUT.\nPlease enter title, author, isbn and quantity without quotes and separated by commas.")

        elif user_input == 2:
            query = input("PLEASE ENTER TITLE OR AUTHOR NAME OR ISBN - ")
            search_books(query)

        elif user_input == 3:
            try:
                book_id, new_quantity = map(int, input("PLEASE ENTER BOOK ID, NEW QUANTITY - ").split(","))
                update_quantity(book_id, new_quantity)
            except ValueError or TypeError:
                print("INVALID INPUT.\nPlease enter book ID and new quantity without quotes and separated by commas.")

        elif user_input == 4:
            view_inventory()

        elif user_input == 5:
            generate_summary_statistics()   

        elif user_input == 6:
            break

        else:
            print("PLEASE ENTER A VALID INPUT!")
    except ValueError:
        print("PLEASE ENTER A VALID INPUT!")

print("\n\nTHANKYOU FOR VISITING !")
mydb.close()