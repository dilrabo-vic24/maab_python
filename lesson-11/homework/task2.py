import sqlite3

with sqlite3.connect("library.db") as conn:
    cursor = conn.cursor()
    
    cursor.execute('''
    DROP TABLE IF EXISTS Books;
    
    CREATE TABLE Books (
        Title TEXT,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT
    );
    ''')
    
    books_data = [
        ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
        ('1984', 'George Orwell', 1949, 'Dystopian'),
        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
    ]
    
    cursor.executemany("INSERT INTO Books VALUES (?, ?, ?, ?)", books_data)
    
    print("Initial Books:")
    cursor.execute("SELECT * FROM Books")
    for row in cursor.fetchall():
        print(row)
    
    cursor.execute('''
    UPDATE Books
    SET Year_Published = 1950
    WHERE Title = '1984'
    ''')
    
    print("\nAfter updating 1984's publication year:")
    cursor.execute("SELECT * FROM Books")
    for row in cursor.fetchall():
        print(row)
    
    print("\nDystopian books (Title and Author):")
    cursor.execute('''
    SELECT Title, Author FROM Books
    WHERE Genre = 'Dystopian'
    ''')
    for row in cursor.fetchall():
        print(row)
    
    cursor.execute('''
    DELETE FROM Books
    WHERE Year_Published < 1950
    ''')
    
    print("\nAfter removing books published before 1950:")
    cursor.execute("SELECT * FROM Books")
    for row in cursor.fetchall():
        print(row)
    
    cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
    
    rating_updates = [
        (4.8, 'To Kill a Mockingbird'),
        (4.7, '1984'),
        (4.5, 'The Great Gatsby')
    ]
    
    for rating, title in rating_updates:
        cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rating, title))
    
    print("\nAfter adding Rating column:")
    cursor.execute("SELECT * FROM Books")
    for row in cursor.fetchall():
        print(row)
    
    print("\nBooks sorted by publication year (ascending):")
    cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
    for row in cursor.fetchall():
        print(row)