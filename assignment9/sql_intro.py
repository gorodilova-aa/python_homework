import sqlite3


# ------------------------------------------------------------------------------------
# Task 3: Function to insert data into the tables

# Function to add a publisher
def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")
    except sqlite3.Error as e:
        print(f"Database error while adding publisher '{name}': {e}")

# Function to add a magazine
def add_magazine(cursor, name, publisher_name):
    try:
        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
        row = cursor.fetchone()
        if not row:
            print(f"Publisher '{publisher_name}' not found. Cannot add magazine '{name}'.")
            return
        publisher_id = row[0]
    
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"Magazine '{name}' already exists.")
    except sqlite3.Error as e:
        print(f"Database error while adding magazine '{name}': {e}")


# Function to add a subscriber
def add_subscriber(cursor, name, address):
    try:
        # check that you don't already have an entry where both the name and the address are the same
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?", (name, address))
        if cursor.fetchone():
            print(f"Subscriber '{name}' at '{address}' already exists.")
            return
        
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
    except sqlite3.IntegrityError:
        print(f"Subscriber '{name}' at '{address}' already exists.")
    except sqlite3.Error as e:
            print(f"Database error while adding subscriber '{name}': {e}")


# Function to add a subscription
def add_subscription(cursor, subscriber_name, subscriber_address, magazine_name, expiration_date):
    try:
        # 1. Find subscriber_id
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?", (subscriber_name, subscriber_address))
        row_subscriber = cursor.fetchone()
        if not row_subscriber:
            print(f"Subscriber '{subscriber_name}' not found.")
            return
        subscriber_id = row_subscriber[0]

        # 2. Find magazine_id
        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
        row_magazine = cursor.fetchone()
        if not row_magazine:
            print(f"Magazine '{magazine_name}' not found.")
            return
        magazine_id = row_magazine[0]

        # 3. Check for existing subscription
        cursor.execute("""
            SELECT subscription_id FROM subscriptions 
            WHERE subscriber_id = ? AND magazine_id = ?
        """, (subscriber_id, magazine_id))
        if cursor.fetchone():
            print(f"Subscription for '{subscriber_name}' to '{magazine_name}' already exists.")
            return

        cursor.execute("""
            INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) 
            VALUES (?, ?, ?)
        """, (subscriber_id, magazine_id, expiration_date))

    except sqlite3.IntegrityError:
        print(f"Subscription for '{subscriber_name}' to '{magazine_name}' already exists.")
    except sqlite3.Error as e:
        print(f"Database error while adding subscription: {e}")

# ------------------------------------------------------------------------------------



# Task 1: Create a New SQLite Database
try:
    # Connect to a new SQLite database
    with  sqlite3.connect("../db/magazines.db") as conn:  
        print("Database created and connected successfully.")

        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()


# ------------------------------------------------------------------------------------
# Task 2: Define Database Structure

        # 1. publishers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)

        # 2. magazines table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
        )
        """)

        # 3. subscribers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            UNIQUE (name, address)
        )
        """)

        # 4. subscriptions table (join table)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
        )
        """)

        conn.commit()
        print("Tables created successfully.")

# ------------------------------------------------------------------------------------
        # Task 3: Insert Data into the Tables

        # 1. Publishers
        add_publisher(cursor, "Nature Group")
        add_publisher(cursor, "Sport Group")
        add_publisher(cursor, "Media Group")

        # 2. Magazines
        add_magazine(cursor, "Wild Life", "Nature Group")
        add_magazine(cursor, "Siberia nature", "Nature Group")
        add_magazine(cursor, "Sports Weekly", "Sport Group")
        add_magazine(cursor, "Winter Sports", "Sport Group")
        add_magazine(cursor, "Films new releases", "Media Group")
        add_magazine(cursor, "Cartoons", "Media Group")

        # 3. Subscribers
        add_subscriber(cursor, "Maksim", "16 Swim Drive")
        add_subscriber(cursor, "Katya", "19 Gymnastic Street")
        add_subscriber(cursor, "Dima", "22 PawPatrol Avenue")

        # 4. Subscriptions
        add_subscription(cursor, "Maksim", "16 Swim Drive", "Films new releases", "2026-01-10")
        add_subscription(cursor, "Maksim", "16 Swim Drive", "Wild Life", "2025-11-15")
        add_subscription(cursor, "Katya", "19 Gymnastic Street", "Siberia nature", "2026-01-17")
        add_subscription(cursor, "Katya", "19 Gymnastic Street", "Sports Weekly", "2026-03-18")    
        add_subscription(cursor, "Dima", "22 PawPatrol Avenue", "Cartoons", "2026-07-05")
      

        # Commit the changes to the database
        conn.commit()
        print("Data inserted and committed successfully.")


# ------------------------------------------------------------------------------------
        #Task 4: Write SQL Queries
        
        # Write a query to retrieve all information from the subscribers table.
        print("\n--- All Subscribers ---")
        cursor.execute("SELECT * FROM subscribers")
        subscribers = cursor.fetchall()
        for subscriber in subscribers:
            print(subscriber)

        # Write a query to retrieve all magazines sorted by name.
        print("\n--- All Magazines (Sorted by Name) ---")
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        magazines = cursor.fetchall()
        for magazine in magazines:
            print(magazine)

        # Write a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN.
        particular_publisher = "Nature Group"
        print(f"\n--- Magazines for Publisher: {particular_publisher} ---")
        cursor.execute("""
            SELECT m.magazine_id, m.name 
            FROM magazines m
            JOIN publishers p ON m.publisher_id = p.publisher_id
            WHERE p.name = ?
        """, (particular_publisher,))

        magazines = cursor.fetchall()
        for magazine in magazines:
            print(magazine)
       

except sqlite3.Error as e:
    print(f"Database error: {e}")

# close the connection
conn.close()