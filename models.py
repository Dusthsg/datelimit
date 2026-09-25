from datetime import datetime
from database import conn, cursor

class NewLotItem:
    def __init__(self, name: str, quant: int, price: float, date_valid: str):
        self.name = name
        self.quant = quant
        self.price = price
        self.date_valid = date_valid

    def save(self):
         cursor.execute("SELECT id from products WHERE name = ?", (self.name,))
         row = cursor.fetchone()
         

         if row:
             product_id = row[0]
         else:
            cursor.execute("INSERT INTO products (name) VALUES (?)",(self.name,))
            product_id = cursor.lastrowid
            print(f"O produto foi criado com ID: {product_id}")

         cursor.execute("INSERT INTO products_lots (product_id, quant, price, date_valid) VALUES (?, ?, ?, ?)", (product_id, self.quant, self.price, self.date_valid))

         conn.commit()
         return cursor.lastrowid