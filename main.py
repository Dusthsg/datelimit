from database import conn, cursor, init_db
from controller import call_menu


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
            ...
        elif opcao == 3:
            ...
        elif opcao == 4:
            ...
        elif opcao == 0:
            print("Encerrando o programa...")
            cursor.close()
            conn.close()
            break
        else:
            print("Opção inválida! Escolha entre 0 e 4.")


if __name__ == "__main__":
    main()