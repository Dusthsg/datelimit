from datetime import datetime
import sys
from pathlib import Path

# Garante que o Python encontre os módulos na pasta raiz
PASTA_PROJETO = Path(__file__).resolve().parent.parent
if str(PASTA_PROJETO) not in sys.path:
    sys.path.append(str(PASTA_PROJETO))

# Importa o cursor compartilhado e o orquestrador
from database import cursor


def executar_consulta(query_onde="", params=None):
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
    
    query_final = query_base + query_onde + " ORDER BY l.date_valid ASC, p.name ASC;"
    cursor.execute(query_final, params)

    colunas = ["Lote ID", "Produto", "Produto ID", "Quantidade", "Preço", "Validade"]
    dados_exportar = []

    resultados = cursor.fetchall()
    for lin in resultados:
        lot_id, product_name, product_id, quant, price, date_valid = lin
        data_obj = datetime.strptime(date_valid, "%Y-%m-%d").date()
        beat_dt = data_obj.strftime("%d/%m/%Y")
        
        print(f"Lote: {lot_id:<6} | {product_name:<50} |Id: {product_id:<6} | Qtd: {quant:<5} | Validade: {beat_dt:<10}")
        dados_exportar.append([lot_id, product_name, product_id, quant, price, beat_dt])

    # Envia os dados para o orquestrador
    return colunas, dados_exportar
