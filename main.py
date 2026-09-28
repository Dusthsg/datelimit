from database import conn, cursor, init_db
from controller import call_menu, selector, advanced_menu
from crud.delete import delete
from crud.create import add_product
from crud.update import update_product


def menu():
    print("\n-------- Devstore --------")
    print("Opção 0 : Sair")
    print("Opção 1 : Listar Produtos")
    print("Opção 2 : Inserir Produto")
    print("Opção 3 : Atualizar Produto")
    print("Opção 4 : Deletar Produto")

    while True:
        try:
            return int(input("Insira a opção que deseja: "))
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")


def main():
    init_db()  # Garante que a tabela existe ao iniciar

    while True:
        opcao = menu()

        if opcao == 1:
            call_menu()
        elif opcao == 2:
            add_product()
        elif opcao == 3:
             _, data = advanced_menu()
             if data:  
                entity = selector(data)
                if entity:  
                  update_product(entity)
                else:
                  print("\nNenhum registro encontrado para exclusão.")
        elif opcao == 4:
          _, data = advanced_menu()
          if data:  
             entity = selector(data)
             if entity:  
                delete(entity)
             else:
               print("\nNenhum registro encontrado para exclusão.")


        elif opcao == 0:
            print("Encerrando o programa...")
            cursor.close()
            conn.close()
            break
        else:
            print("Opção inválida! Escolha entre 0 e 4.")


if __name__ == "__main__":
    main()