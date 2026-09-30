from database import conn as default_conn
from datetime import datetime

class LotRepository:
    def __init__(self, connection=None):
       self.conn = connection or default_conn
       self.cursor = self.conn.cursor()

    def create(self, product_id: int, quant: int, price: float, date_valid: str):
        self.cursor.execute("""
                    INSERT INTO product_lots (product_id, quant, price, date_valid) 
                    VALUES (?, ?, ?, ?)
                """, (product_id, quant, price, date_valid))
        self.conn.commit()
        lot_id = self.cursor.lastrowid
        return lot_id

    def delete(self, lot_id: int):
        self.cursor.execute("DELETE FROM product_lots WHERE id = ?", (lot_id,))
        self.conn.commit()

    def update(self, lot_id: int, quant: int = None, price: float = None, date_valid: str = None):
        fields = []
        params = []

        if quant is not None:
            fields.append("quant = ?")
            params.append(quant)

        if price is not None:
            fields.append("price = ?")
            params.append(price)

        if date_valid is not None:
            fields.append("date_valid = ?")
            params.append(date_valid)

        if not fields:
            return

        params.append(lot_id)   
        sql = f"UPDATE product_lots SET {', '.join(fields)} WHERE id = ?"
        
        self.cursor.execute(sql, tuple(params))
        self.conn.commit()

    def read(self, query_search="", params=None):
        if params is None:
           params = []

        query_base = """
     SELECT 
        l.id AS lot_id,
        p.name AS product_name,
        p.id AS product_id,
        l.quant,
        l.price,
        l.date_valid
    FROM product_lots l
    INNER JOIN products p ON p.id = l.product_id
    WHERE 1=1
    """
        query_final = query_base + query_search + " ORDER BY l.date_valid ASC, p.name ASC;"
        self.cursor.execute(query_final, params)
        return self.cursor.fetchall()