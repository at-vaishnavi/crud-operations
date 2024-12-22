import sqlite3
from tabulate import tabulate  
connect = sqlite3.connect('library.sqlite')
lib_cursor = connect.cursor()
print("Connected to the library database successfully.")
lib_cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre TEXT CHECK(genre IN ('Mythology', 'Psychology')),
    title TEXT,
    author TEXT,
    available_copies INTEGER)''')
connect.commit()
print("Table created successfully.")
books_to_insert = [
    ('Mythology', 'RAMAYANA', 'VALMIKI', 10),
    ('Psychology', 'Story of a Human Mind', 'Paul Bloom', 5),
    ('Mythology', 'MAHABHARATA', 'VED VYASA', 8),
    ('Psychology', 'Thinking, Fast and Slow', 'Daniel Kahneman', 7),
    ('Mythology', 'BHAGAVATHA', 'VYASA', 15),
    ('Psychology', 'The Man Who Mistook His Wife for a Hat', 'Oliver Sacks', 6)]
lib_cursor.executemany('''
    INSERT INTO books (genre, title, author, available_copies)
    VALUES (?, ?, ?, ?)''', books_to_insert)
connect.commit()
print("Books inserted successfully.")
lib_cursor.execute('SELECT * FROM books')
books = lib_cursor.fetchall()
headers = ['ID', 'Genre', 'Title', 'Author', 'Available Copies']
print("\nBooks in the Library:")
print(tabulate(books, headers=headers, tablefmt='pretty'))
lib_cursor.execute("SELECT * FROM books WHERE genre = 'Mythology'")
mythology_books = lib_cursor.fetchall()
print("\nBooks in the Mythology Genre:")
print(tabulate(mythology_books, headers=headers, tablefmt='pretty'))
lib_cursor.execute("SELECT * FROM books WHERE genre = 'Psychology'")
psychology_books = lib_cursor.fetchall()
print("\nBooks in the Psychology Genre:")
print(tabulate(psychology_books, headers=headers, tablefmt='pretty'))
lib_cursor.execute("SELECT * FROM books WHERE title = 'RAMAYANA'")
before_update = lib_cursor.fetchall()
if before_update:
    print("Before Update:")
    print(tabulate(before_update, headers=['ID', 'Genre', 'Title', 'Author', 'Available Copies'], tablefmt='pretty'))
    lib_cursor.execute("UPDATE books SET available_copies = 25 WHERE title = 'RAMAYANA'")
    connect.commit()
    lib_cursor.execute("SELECT * FROM books WHERE title = 'RAMAYANA'")
    after_update = lib_cursor.fetchall()
    print("\nAfter Update:")
    print(tabulate(after_update, headers=['ID', 'Genre', 'Title', 'Author', 'Available Copies'], tablefmt='pretty'))
else:
    print("No book found with the title 'RAMAYANA'.")
lib_cursor.execute("SELECT * FROM books WHERE title = 'The Man Who Mistook His Wife for a Hat'")
before_delete = lib_cursor.fetchall()
if before_delete:
    print("Before Delete:")
    print(tabulate(before_delete, headers=['ID', 'Genre', 'Title', 'Author', 'Available Copies'], tablefmt='pretty'))
    lib_cursor.execute("DELETE FROM books WHERE title = 'The Man Who Mistook His Wife for a Hat'")
    connect.commit()
    lib_cursor.execute("SELECT * FROM books WHERE title = 'The Man Who Mistook His Wife for a Hat'")
    after_delete = lib_cursor.fetchall()
    print("\nAfter Delete:")
    if after_delete:
        print(tabulate(after_delete, headers=['ID', 'Genre', 'Title', 'Author', 'Available Copies'], tablefmt='pretty'))
    else:
        print("No record found for the title 'The Man Who Mistook His Wife for a Hat' (it has been deleted).")
else:
    print("No book found with the title 'The Man Who Mistook His Wife for a Hat'.")
connect.close()
