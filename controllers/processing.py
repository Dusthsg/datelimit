from datetime import datetime
from repositories.lot_repository import LotRepository
from repositories.product_repository import ProductRepository

prod_repo = ProductRepository()
lot_repo = LotRepository()


def processing_update(args, entity):
    lot_id, nome, prod_id, quant, price, validade = entity[:6]

    prod_fields = {}

    # 1. Se escolheu alterar o Nome (Tabela 'products')
    if 1 in args:
        new_name = input(f"Digite um novo nome para [{nome}]: ").strip()
        if new_name:
            prod_fields["name"] = new_name

    if 3 in args:
        try:
          raw_price = input(f"Digite um novo preço para [{price:.2f}]: ").replace(",", ".")
          prod_fields["price"] = float(raw_price)
        except ValueError:
            
            print("Preço inválido! Campo ignorado.")
    if prod_fields:
      sucesso = prod_repo.update(prod_id, prod_fields)
      if sucesso:
            print(f"\n[OK] Produto #{prod_id} atualizado com sucesso!")
      else:
            print("\n[!] Falha ao atualizar o lote.")

    # 2. Dicionário de campos dinâmicos para a tabela 'product_lots'
    lot_fields = {}

    if 2 in args:
        try:
            new_quant = int(input(f"Digite uma nova quantidade para [{quant}]: "))
            lot_fields["quant"] = new_quant
        except ValueError:
            print("Quantidade inválida! Campo ignorado.")

    if 4 in args:
        try:
            new_date = input("Digite a nova data em formato (22/12/2028 ou 22-12-2028): ").strip()
            datef = datetime.strptime(new_date.replace("/", "-"), "%d-%m-%Y").strftime("%Y-%m-%d")
            lot_fields["date_valid"] = datef
        except ValueError:
            print("Data inválida! Campo ignorado.")

    if 5 in args:
        try:
            new_local = input("Digite a novo local para o produto: ").strip().upper()
            lot_fields["location"] = new_local
        except ValueError:
            print("Local Inválido! Campo ignorado.")

    if 6 in args:
        try:
            new_status = input("Digite o novo status exemplo (vencido): ").strip().upper()
            lot_fields["status"] = new_status
        except ValueError:
            print("Status inválido! Campo ignorado.")

    # 3. Executa o update dinâmico via repositório
    if lot_fields:
        sucesso = lot_repo.update(lot_id, lot_fields)
        if sucesso:
            print(f"\n[OK] Lote #{lot_id} atualizado com sucesso!")
        else:
            print("\n[!] Falha ao atualizar o lote.")
