# Import sqlite3 so Python can create and query a SQLite database.
import sqlite3

# Create a connection to library.db in this same folder.
# If the file does not exist yet, SQLite creates it automatically.
connection = sqlite3.connect("library.db")

# Create a cursor object used to execute SQL commands.
cursor = connection.cursor()

# Drop the books table if it already exists so reruns start clean.
cursor.execute("DROP TABLE IF EXISTS books;")

# Create the books table with the required columns and data types.
cursor.execute(
    """
    CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT
    );
    """
)

# Insert the required book rows into the books table.
cursor.executemany(
    """
    INSERT INTO books (title, author, publication_year, genre)
    VALUES (?, ?, ?, ?);
    """,
    [
        ("The Great Gatsby", "F Scott Fitzgerald", 1925, "Fiction"),
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian Fiction"),
        ("The Lord of the Rings", "J.R.R. Tolkien", 1954, "Fantasy"),
        ("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction"),
        ("One Hundred Years of Solitude", "Gabriel Garcia Marquez", 1967, "Magical Realism"),
        ("The Hitchhikers Guide to the Galaxy", "Douglas Adams", 1979, "Science Fiction"),
        ("The Handmaids Tale", "Margaret Atwood", 1985, "Dystopian Fiction"),
        ("War and Peace", "Leo Tolstoy", 1869, "Fiction"),
        ("Ulysses", "James Joyce", 1922, "Fiction"),
    ],
)

# Select all rows to verify data can be fetched from the table.
all_books = cursor.execute("SELECT * FROM books;").fetchall()

# Store every row whose genre is exactly "Fiction".
fiction = cursor.execute("SELECT * FROM books WHERE genre = 'Fiction';").fetchall()

# Update The Handmaids Tale publication year to 1985.
cursor.execute(
    """
    UPDATE books
    SET publication_year = 1985
    WHERE title = 'The Handmaids Tale';
    """
)

# Delete the book titled 1984 from the table.
cursor.execute("DELETE FROM books WHERE title = '1984';")

# Save all create/insert/update/delete changes to library.db.
connection.commit()
