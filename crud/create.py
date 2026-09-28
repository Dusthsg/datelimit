from datetime import datetime
from models import NewLotItem


def add_product():
    print("\n--- Novo Cadastro de Lote ---")
    name = input("Nome do Produto: ").strip()
    if not name:
        print("-> Erro: O nome do produto não pode ficar vazio.")
        return

    try:
        quant = int(input("Quantidade: "))
        price = float(input("Preço unitário: ").replace(",", "."))
    except ValueError:
        print("-> Erro: Quantidade deve ser um número inteiro e Preço deve ser numérico.")
        return

    # Entrada e validação explícita da data (aceita com barra ou hífen)
    input_date = input("Validade (DD/MM/AAAA ou DD-MM-AAAA): ").strip()
    try:
        # Converte para data real e padroniza para ISO (YYYY-MM-DD) para o SQLite
        date_obj = datetime.strptime(input_date.replace("/", "-"), "%d-%m-%Y")
        date_valid = date_obj.strftime("%Y-%m-%d")
    except ValueError:
        print("-> Erro: Data inválida! Use o formato DD/MM/AAAA.")
        return

    # Persistência via Active Record
    product = NewLotItem(name, quant, price, date_valid)
    prod_id, lot_id = product.save()

    print(f"\n[OK] Lote #{lot_id} cadastrado com sucesso para o produto '{name}' (ID: {prod_id})!")