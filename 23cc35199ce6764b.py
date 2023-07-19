import sqlite3
import random
import string
import os

conn = sqlite3.connect('BD_New.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Warehous (
    id INTEGER PRIMARY KEY,
    name TEXT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Company (
    id INTEGER PRIMARY KEY,
    name TEXT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Product (
    id INTEGER PRIMARY KEY,
    name TEXT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Sales (
    date DATE,
    sales_sum REAL,
    amount INTEGER,
    product_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES Product(id)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Product_Segmentation (
    product_id INTEGER,
    segment_name TEXT,
    FOREIGN KEY (product_id) REFERENCES Product(id)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Stock (
    date DATE,
    product_id INTEGER,
    value INTEGER,
    warehouse_id INTEGER,
    company_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES Product(id),
    FOREIGN KEY (warehouse_id) REFERENCES Warehous(id),
    FOREIGN KEY (company_id) REFERENCES Company(id)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ProductMovement (
    date DATE,
    product_id INTEGER,
    in_value INTEGER,
    out_value INTEGER,
    type BOOLEAN,
    FOREIGN KEY (product_id) REFERENCES Product(id)
)''')

for i in range(20):
    name = ''.join(random.choices(string.ascii_uppercase, k=5))
    cursor.execute("INSERT INTO Warehous (name) VALUES (?)", (name,))

for i in range(10):
    name = ''.join(random.choices(string.ascii_uppercase, k=5))
    cursor.execute("INSERT INTO Company (name) VALUES (?)", (name,))

for i in range(21):
    name = ''.join(random.choices(string.ascii_uppercase, k=5))
    cursor.execute("INSERT INTO Product (name) VALUES (?)", (name,))

for i in range(100):
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = f"2023-{month:02d}-{day:02d}"
    sales_sum = round(random.uniform(1000, 5000), 2)
    amount = random.randint(1, 100)
    product_id = random.randint(1, 10)
    cursor.execute("INSERT INTO Sales (date, sales_sum, amount, product_id) VALUES (?, ?, ?, ?)", (date, sales_sum, amount, product_id))

for i in range(10):
    product_id = random.randint(1, 10)
    segment_name = ''.join(random.choices(string.ascii_uppercase, k=5))
    cursor.execute("INSERT INTO Product_Segmentation (product_id, segment_name) VALUES (?, ?)", (product_id, segment_name))

for i in range(100):
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = f"2023-{month:02d}-{day:02d}"
    product_id = random.randint(1, 10)
    value = random.randint(1, 100)
    warehouse_id = random.randint(1, 10)
    company_id = random.randint(1, 10)
    cursor.execute("INSERT INTO Stock (date, product_id, value, warehouse_id, company_id) VALUES (?, ?, ?, ?, ?)", (date, product_id, value, warehouse_id, company_id))

for i in range(100):
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = f"2023-{month:02d}-{day:02d}"
    product_id = random.randint(1, 10)
    in_value = random.randint(1, 50)
    out_value = random.randint(1, 50)
    movement_type = random.choice([True, False])
    cursor.execute("INSERT INTO ProductMovement (date, product_id, in_value, out_value, type) VALUES (?, ?, ?, ?, ?)", (date, product_id, in_value, out_value, movement_type))

conn.commit()
conn.close()
os.rename('BD_New.db', 'BD_New.sqlite3')