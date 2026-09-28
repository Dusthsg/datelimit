from database import conn, cursor

class NewLotItem:
    def __init__(self, name: str, quant: int, price: float, date_valid: str):
        self.name = name.strip()
        self.quant = quant
        self.price = price
        self.date_valid = date_valid

    def save(self) -> tuple[int, int]:
        """
        Salva o produto (se não existir) e registra o novo lote.
        Retorna: (product_id, lot_id)
        """
        cursor.execute("SELECT id FROM products WHERE name = ?", (self.name,))
        row = cursor.fetchone()

        if row:
            product_id = row[0]
        else:
            # Correção: VALUES (?) com parênteses
            cursor.execute("INSERT INTO products (name) VALUES (?)", (self.name,))
            product_id = cursor.lastrowid

        # Correção: nome da tabela 'product_lots'
        cursor.execute("""
            INSERT INTO product_lots (product_id, quant, price, date_valid) 
            VALUES (?, ?, ?, ?)
        """, (product_id, self.quant, self.price, self.date_valid))

        conn.commit()
        lot_id = cursor.lastrowid

        return product_id, lot_id