import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "products.db"

def migrate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("Iniciando migração...")

    try:
        # 1. Adiciona a nova coluna no produto (se já não existir)
        cursor.execute("PRAGMA table_info(products);")
        cols = [c[1] for c in cursor.fetchall()]
        if "price" not in cols:
            cursor.execute("ALTER TABLE products ADD COLUMN price REAL DEFAULT 0.0;")
            print("-> Coluna 'price' adicionada à tabela 'products'.")
        else:
            print("-> Coluna 'price' já existia na tabela 'products'.")

        # 2. Copia os preços existentes dos lotes para os produtos
        cursor.execute("""
            UPDATE products
            SET price = COALESCE((
                SELECT l.price 
                FROM product_lots l 
                WHERE l.product_id = products.id AND l.price > 0
                ORDER BY l.id DESC 
                LIMIT 1
            ), 0.0)
            WHERE EXISTS (
                SELECT 1 
                FROM product_lots l 
                WHERE l.product_id = products.id AND l.price > 0
            );
        """)
        updated_count = cursor.rowcount
        print(f"-> Preços sincronizados com sucesso! ({updated_count} produtos atualizados)")

        conn.commit()
        print("\nMigração concluída com êxito!")

    except Exception as e:
        conn.rollback()
        print(f"Erro inesperado na migração: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()
