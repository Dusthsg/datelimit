from database.database import conn as default_conn

class ProductRepository:
   def __init__(self, connection=None):
      self.conn = connection or default_conn
      self.cursor = self.conn.cursor()

   def get_by_name(self, name: str):
      self.cursor.execute("SELECT id FROM products WHERE name = ?", (name,))
      return self.cursor.fetchone()
   
   def search_by_name(self, name: str) -> int:
      self.cursor.execute("SELECT id FROM products WHERE name LIKE ?", (name,))
      return self.cursor.fetchone()

   def delete(self, product_id) -> None:
      self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
      self.conn.commit()

   def update(self, prod_id, fields: dict) -> bool:
      if not fields:
         return False

      if isinstance(prod_id, (tuple, list)):
         prod_id = prod_id[0]

      set_clauses = ", ".join([f"{col} = ?" for col in fields.keys()])
      sql = f"UPDATE products SET {set_clauses} WHERE id = ?"

      params = list(fields.values()) + [prod_id]

      self.cursor.execute(sql, tuple(params))
      self.conn.commit()
      
      return self.cursor.rowcount > 0


   def create(self, name: str, price: float) -> int:
      self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
      self.conn.commit()

      return self.cursor.lastrowid