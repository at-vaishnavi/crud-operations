import sqlite3
from tabulate import tabulate  # Used to display data in a table format

# Connect to SQLite database (or create it if it doesn't exist)
connect = sqlite3.connect('library.sqlite')
lib_cursor = connect.cursor()
print("Connected to the library database successfully.")

# Create the 'books' table if it doesn't already exist
# This is a Python comment, it won't interfere with SQL execution
lib_cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre TEXT CHECK(genre IN ('Mythology', 'Psychology')),
    title TEXT,
    author TEXT,
    available_copies INTEGER
)''')  # Make sure this SQL statement is correct and doesn't contain Python-style comments inside the SQL.

# Commit the changes (apply table creation)
connect.commit()
print("Table created successfully.")

# List of books to insert into the 'books' table
books_to_insert = [
    ('Mythology', 'RAMAYANA', 'VALMIKI', 10),
    ('Psychology', 'Story of a Human Mind', 'Paul Bloom', 5),
    ('Mythology', 'MAHABHARATA', 'VED VYASA', 8),
    ('Psychology', 'Thinking, Fast and Slow', 'Daniel Kahneman', 7),
    ('Mythology', 'BHAGAVATHA', 'VYASA', 15),
    ('Psychology', 'The Man Who Mistook His Wife for a Hat', 'Oliver Sacks', 6)
]

# Insert the list of books into the 'books' table
lib_cursor.executemany('''
    INSERT INTO books (genre, title, author, available_copies)
    VALUES (?, ?, ?, ?)''', books_to_insert)

# Commit the changes (apply the inserts)
connect.commit()
print("Books inserted successfully.")

# Fetch all books from the 'books' table
lib_cursor.execute('SELECT * FROM books')
books = lib_cursor.fetchall()

# Define headers for the table display
headers = ['ID', 'Genre', 'Title', 'Author', 'Available Copies']

# Display all books in a formatted table
print("\nBooks in the Library:")
print(tabulate(books, headers=headers, tablefmt='pretty'))

# Fetch all books in the 'Mythology' genre
lib_cursor.execute("SELECT * FROM books WHERE genre = 'Mythology'")
mythology_books = lib_cursor.fetchall()

# Display the books in the 'Mythology' genre
print("\nBooks in the Mythology Genre:")
print(tabulate(mythology_books, headers=headers, tablefmt='pretty'))

# Fetch all books in the 'Psychology' genre
lib_cursor.execute("SELECT * FROM books WHERE genre = 'Psychology'")
psychology_books = lib_cursor.fetchall()

# Display the books in the 'Psychology' genre
print("\nBooks in the Psychology Genre:")
print(tabulate(psychology_books, headers=headers, tablefmt='pretty'))

# Fetch the details of the book titled 'RAMAYANA'
lib_cursor.execute("SELECT * FROM books WHERE title = 'RAMAYANA'")
before_update = lib_cursor.fetchall()

# Check if 'RAMAYANA' exists in the table
if before_update:
    print("Before Update:")
    # Display the current details of 'RAMAYANA'
    print(tabulate(before_update, headers=['ID', 'Genre', 'Title', 'Author', 'Available Copies'], tablefmt='pretty'))
    
    # Update the number of available copies of 'RAMAYANA' to 25
    lib_cursor.execute("UPDATE books SET available_copies = 25 WHERE title = 'RAMAYANA'")
