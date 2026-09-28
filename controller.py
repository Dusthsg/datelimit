from datetime import datetime, date, timedelta
from archive_mp.export import make_ex 
from crud.read import executar_consulta

def orquest(colunas: list, dados: list) -> None:
    """Recebe os dados que já foram consultados e decide a exportação."""
    if not dados:
        print("\nNenhum registro encontrado para exportar.")
        return

    # 1. EXIBIÇÃO NO TERMINAL
    print("\n" + "=" * 105)
    print(f"{'Lote':<6} | {'Produto':<50} | {'Prod ID':<8} | {'Qtd':<6} | {'Preço':<8} | {'Validade':<10}")
    print("-" * 100)
    
    for lin in dados:
        lot_id, nome, prod_id, quant, price, validade = lin
        print(f"{lot_id:<6} | {nome:<50} | {prod_id:<8} | {quant:<6} | R${price:<6.2f} | {validade:<10}")
    print("=" * 105)

    opcao = input("\nDeseja exportar esses dados para Excel? (s/n): ").strip().lower()
    
    if opcao == "s":
        nome = input("Nome do arquivo (Enter para 'lotes.xlsx'): ").strip() or "lotes.xlsx"
        if not nome.endswith(".xlsx"):
            nome += ".xlsx"
            
        make_ex(colunas, dados, nome)
    else:
        print("Finalizado sem exportação.")


def query_venc():
    q_date = " AND l.date_valid < ?"
    today = date.today().strftime("%Y-%m-%d")
    colunas, dados = executar_consulta(q_date, [today])
    orquest(colunas, dados)


def query_days(days_min, days_max):
    today = date.today()
    init = (today + timedelta(days=days_min)).strftime("%Y-%m-%d")
    end = (today + timedelta(days=days_max)).strftime("%Y-%m-%d")

    q_date = " AND l.date_valid BETWEEN ? AND ?"
    colunas, dados = executar_consulta(q_date, [init, end])
    orquest(colunas, dados)


"""==================== MENU DE BUSCA AVANÇADA ====================
Opções de Busca: Nome, data especifica, período e quantidade 
"""

def adv_query(req_list):
    query = ""
    params = []

    if 1 in req_list:
        text = input("Insira o nome ou parte dele para buscar: ").strip()
        query += " AND p.name LIKE ?"
        params.append(f"%{text}%")

    if 2 in req_list:
        input_date = input("Insira uma data específica como (20/10/2028 ou 20-10-2028): ").strip()
        try:
            datef = datetime.strptime(input_date.replace("/", "-"), "%d-%m-%Y").strftime("%Y-%m-%d")
            query += " AND l.date_valid = ?"
            params.append(datef)
        except ValueError:
            print("Data inválida. Certifique-se de digitar no formato DD/MM/AAAA.")
            return [], []

    if 3 in req_list:
        text = input("Insira um período em dias ex: (30, 45) ou apenas (30): ").strip()
        arr = [int(x.strip()) for x in text.split(",") if x.strip().isdigit()]
        today = datetime.now().date()

        if len(arr) == 2:
            days_min, days_max = sorted(arr)
            init = today + timedelta(days=days_min)
            end = today + timedelta(days=days_max)

            query += " AND l.date_valid BETWEEN ? AND ?"
            params.append(init.strftime("%Y-%m-%d"))
            params.append(end.strftime("%Y-%m-%d"))

        elif len(arr) == 1:
            days_max = arr[0]
            end = today + timedelta(days=days_max)

            query += " AND l.date_valid BETWEEN ? AND ?"
            params.append(today.strftime("%Y-%m-%d"))
            params.append(end.strftime("%Y-%m-%d"))
        else:
            print("Entrada inválida! Digite 1 ou 2 números separados por vírgula.")
            return [], []

    if 4 in req_list:
        entrada_qtd = input("Insira a quantidade (ex: 10 para teto, ou 0, 10 para intervalo): ").strip()
        arr_qtd = [int(x.strip()) for x in entrada_qtd.split(",") if x.strip().isdigit()]

        if len(arr_qtd) == 1:
            query += " AND l.quant <= ?"
            params.append(arr_qtd[0])
        elif len(arr_qtd) == 2:
            qtd_min, qtd_max = sorted(arr_qtd)
            query += " AND l.quant BETWEEN ? AND ?"
            params.append(qtd_min)
            params.append(qtd_max)
        else:
            print("Entrada de quantidade inválida! Digite 1 ou 2 números.")
            return [], []

    colunas, dados = executar_consulta(query, params)
    return colunas, dados

"""===================================================================================================================="""
"""Selector"""
"""===================================================================================================================="""

def selector(data: list):
    if not data:
        print("\nNenhum registro para selecionar.")
        return None
    
    for i, row in enumerate(data, start=1):
         lot_id, nome, prod_id, quant, price, validade = row
         print(f"[{i}] Lote #{lot_id} | {nome:<50} | Qtd: {quant:<5} | Preço: R$ {price:<7} | {validade:<10} ")
    print("[0] Cancelar operação")
    print("=" * 60)

    while True:
        try:
            escolha = int(input("\nEscolha o número do item desejado: "))
            
            if escolha == 0:
                print("Operação cancelada.")
                return None
            
            # Verifica se o número digitado existe na lista (entre 1 e o total de linhas)
            if 1 <= escolha <= len(data):
                # O índice real da lista em Python começa em 0, então subtrai 1:
                item_selecionado = data[escolha - 1]
                return item_selecionado
            else:
                print(f"Número fora do intervalo! Digite um valor entre 1 e {len(data)}.")
                
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
"""===================================================================================================================="""
"""Delete"""
"""===================================================================================================================="""


def advanced_menu():
    print("\n" + "=" * 55)
    print(f"{'DATELIMIT Menu de Busca Avançada':^50}")
    print("=" * 55)
    print("[1] Nome")
    print("[2] Data Específica")
    print("[3] Período")
    print("[4] Quantidade")
    print("[0] Sair")
    print("=" * 55)
    while True:
        try:
            input_query = input("Insira o(s) número(s) referente às opções separadas por vírgula ( , ): ")
            args = [int(x.strip()) for x in input_query.split(",") if x.strip().isdigit()]
            if 0 in args or not args:
                return [], []
            return adv_query(args)
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")


def main_menu():
    print("\n" + "=" * 55)
    print(f"{'DATELIMIT Menu Principal':^50}")
    print("=" * 55)
    print("[1] Vencidos")
    print("[2] Crítico (7 dias)")
    print("[3] Atenção (8 - 29 dias)")
    print("[4] Alerta (30 - 45 dias)")
    print("[5] Completa (0 - 45 dias)")
    print("[6] Todos os registros")
    print("[7] Busca avançada")
    print("[0] Sair")
    print("=" * 55)

    while True:
        try:
            return int(input("Insira a opção que deseja: "))
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")


def call_menu():
    while True:
        num = main_menu()

        if num == 1:
            query_venc()
        elif num == 2:
            query_days(0, 7)
        elif num == 3:
            query_days(8, 29)
        elif num == 4:
            query_days(30, 45)
        elif num == 5:
            query_days(0, 45)
        elif num == 6:
            colunas, dados = executar_consulta()
            orquest(colunas, dados)
        elif num == 7:
            column, data = advanced_menu()
            orquest(column, data)
        elif num == 0:
            print("Saindo...")
            break