import sqlite3


with sqlite3.connect("roster.db") as conn:
    cursor = conn.cursor()
    
    cursor.execute('''
    DROP TABLE IF EXISTS Roster;
    
    CREATE TABLE Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    );
    ''')
    
    roster_data = [
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys', 'Bajoran', 29)
    ]
    
    cursor.executemany("INSERT INTO Roster VALUES (?, ?, ?)", roster_data)
    
    print("Initial Roster:")
    cursor.execute("SELECT * FROM Roster")
    for row in cursor.fetchall():
        print(row)
    
    cursor.execute('''
    UPDATE Roster
    SET Name = 'Ezri Dax'
    WHERE Name = 'Jadzia Dax'
    ''')
    
    print("\nAfter updating Jadzia to Ezri:")
    cursor.execute("SELECT * FROM Roster")
    for row in cursor.fetchall():
        print(row)
    
    print("\Benjamin characters (Name and Age):")
    cursor.execute('''
    SELECT Name, Age FROM Roster
    WHERE Species = 'Benjamin'
    ''')
    for row in cursor.fetchall():
        print(row)
    
    cursor.execute('''
    DELETE FROM Roster
    WHERE Age > 100
    ''')
    
    print("\nAfter removing characters over 100 years old:")
    cursor.execute("SELECT * FROM Roster")
    for row in cursor.fetchall():
        print(row)
    
    cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
    
    rank_updates = [
        ('Captain', 'Benjamin Sisko'),
        ('Lieutenant', 'Ezri Dax'),
        ('Major', 'Kira Nerys')
    ]
    
    for rank, name in rank_updates:
        cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", (rank, name))
    
    print("\nAfter adding Rank column:")
    cursor.execute("SELECT * FROM Roster")
    for row in cursor.fetchall():
        print(row)
    
    print("\nCharacters sorted by age (descending):")
    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
    for row in cursor.fetchall():
        print(row)

print("\n\nTASK 2: LIBRARY DATABASE\n" + "-"*30)