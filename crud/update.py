from datetime import datetime
from database import conn, cursor

from repositories.lot_repository import LotRepository
from repositories.product_repository import ProductRepository

product_repo = ProductRepository()
lot_repo = LotRepository()


def update_product(entity):
    lot_id, nome, prod_id, quant, price, validade = entity
    print(f"\nEntidade Selecionada: Lote #{lot_id:<7} | {nome:<50} | Qtd: {quant:<4} | Preço: R$ {price:<7} | Val: {validade}")

    print("\n" + "=" * 55)
    print(f"{'Selecione o que deseja editar':^50}")
    print("=" * 55)
    print("[1] Nome do Produto")
    print("[2] Quantidade")
    print("[3] Preço")
    print("[4] Data de Validade")
    print("[0] Sair / Cancelar")
    print("=" * 55)

    while True:
        try:
            input_query = input("Insira as opções separadas por vírgula (ex: 2, 3): ")
            args = [int(x.strip()) for x in input_query.split(",") if x.strip().isdigit()]

            if 0 in args or not args:
                print("Operação cancelada.")
                return

            processing_update(args, entity)
            return

        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")


def processing_update(args, entity):
    lot_id, nome, prod_id, quant, price, validade = entity

    # 1. Se escolheu alterar o Nome (Tabela 'products')
    if 1 in args:
        new_name = input(f"Digite um novo nome para [{nome}]: ")
        if new_name:
            product_repo.update_name(prod_id, new_name)
            print("-> Nome atualizado com sucesso!")

    set_clauses = []
    params = []

    if 2 in args:
        try:
           new_quant = int(input(f"Digite uma nova quantidade para [{quant}]: "))
        except ValueError:
         print("Quantidade inválida! Campo ignorado.")

    if 3 in args:
        try:
           new_price = float(input(f"Digite um novo preço para [{price:.2f}]: "))
        except ValueError:
            print("Preço inválido! Campo ignorado.")

    if 4 in args:
        try:
           raw_date = input("Digite a nova data em formato (22/12/2028 ou 22-12/2028): ")
           new_date = datetime.strptime(raw_date.replace("/", "-"), "%d-%m-%Y").strftime("%Y-%m-%d")
        except ValueError:
            print("Data inválida! Campo ignorado.")

    if any(param is not None for param in (new_quant, new_price, new_date)):
      lot_repo.update(lot_id, quant=new_quant, price=new_price, date_valid=new_date)
      print("\n[OK] Alterações do lote salvas!")
   