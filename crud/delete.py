from database import conn, cursor


def delete(entity):
    lot_id, nome, prod_id, quant, price, validade = entity
    print(f"Entidade Seleciona: Lote #{lot_id} | {nome:<50} | Qtd: {quant:<5} | Preço: R$ {price:<7} | {validade:<10} ")

    try:
     num = int(input("Digite [1] para deletar o lote e [2] para deletar o produto: "))

     if num == 1:
         choose = input("Tem certeza que deseja deletar o item selecionado s/n: ").lower().strip()
         if choose == "s":
           cursor.execute("DELETE FROM product_lots WHERE id = ?", (lot_id,))
           conn.commit()
           print(f"Lote #{lot_id} deletado com sucesso!")
         else:
           print("Operação cancelada")
         
     elif num == 2:
         print(f"Item Lote #{lot_id} | {nome:<50} | Qtd: {quant:<5} | Preço: R$ {price:<7} | {validade:<10} ")
         print(f"\nATENÇÃO! isso deletará o '{nome}' e todos os seus lotes correpondentes do banco de dados")
         choose = input("Tem certeza que deseja deletar o item selecionado s/n: ").lower().strip()
         if choose == "s":
             cursor.execute("DELETE FROM products WHERE id = ?", (prod_id,))
             conn.commit()
             print(f"Produto '{nome}' e todos os seus lotes foram deletados com sucesso!")
         else:
             print("Operação cancelada")
     else:
        print("Opção inválida! Digite um número válido entre 1 e 2")

    except ValueError:
        print("Digite um número válido entre 1 e 2")