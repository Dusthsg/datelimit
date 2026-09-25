from database import conn, cursor


def update_product():
   product_id = input("Insira o nome ou id do produto que deseja editar: ")

   cursor.execute("SELECT * from products WHERE = ?", (product_id,))
   product = cursor.fetchone()

   if not product:
      print("\nProduto não encontrado no banco de dados")
      return

   print(f"Produto selecionado: ID: {product[0]} | Nome: {product[1]} | Quantidade: {product[2]} | Data de Validade: {product[3]} ")

   print("\nO que deseja alterar?")
   print("1 - Nome")
   print("2 - Quantidade")
   print("3 - Validade")
   option = input("Escolha a opção: ")

   try:
      if option == 1:
         new_name = input(f"Insira um novo nome para {product[1]}")
         cursor.execute("UPDATE products SET = ? WHERE = ?",(new_name, product_id))

      elif option == 2:
        new_quant = int(input(f"Insira uma nova quantidade para {product[2]}"))
        cursor.execute("UPDATE products SET = ? WHERE = ?",(new_quant, product_id))

      elif option == 3:
         new_date = float(input(f"Insira uma nova data para {product[3]}"))
         cursor.execute("UPDATE products SET = ? WHERE = ?",(new_date, product_id))

      else:
            print("Opção inválida!")
            return

      conn.commit()
      print("-> Produto atualizado com sucesso!")

   except ValueError:
        print("-> Erro: Digite um valor numérico válido.")
      