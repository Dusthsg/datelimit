from datetime import datetime, date, timedelta
from controllers.orquest import orquest

from repositories.lot_repository import LotRepository
from repositories.product_repository import ProductRepository

prod_repo = ProductRepository()
lot_repo = LotRepository()

def query_venc():
    q_date = " AND l.date_valid < ?"
    today = date.today().strftime("%Y-%m-%d")
    dados = lot_repo.read(q_date, [today])
    colunas = lot_repo.get_columns()
    orquest(colunas, dados)


def query_days(days_min, days_max):
    today = date.today()
    init = (today + timedelta(days=days_min)).strftime("%Y-%m-%d")
    end = (today + timedelta(days=days_max)).strftime("%Y-%m-%d")

    query_search = " AND l.date_valid BETWEEN ? AND ?"
    dados = lot_repo.read(query_search, [init, end])
    colunas = lot_repo.get_columns()
    orquest(colunas, dados)


def adv_query(req_list):
    query = ""
    params = []

    if 1 in req_list:
        text = input("Insira o nome ou parte dele para buscar: ").strip()

        if not text:
            print("ERRO 301, entrada não inserida")
            return None

        query += " AND p.name LIKE ?"
        params.append(f"%{text}%")

    if 2 in req_list:
        input_date = input("Insira uma data específica como (20/10/2028 ou 20-10-2028): ").strip()
        if not input_date:
            print("ERRO 301, entrada não inserida")
            return None

        try:
            datef = datetime.strptime(input_date.replace("/", "-"), "%d-%m-%Y").strftime("%Y-%m-%d")
            query += " AND l.date_valid = ?"
            params.append(datef)
        except ValueError:
            print("Data inválida. Certifique-se de digitar no formato DD/MM/AAAA.")
            return None

    if 3 in req_list:
        datei = input("Insira um período em dias ex: (30, 45) ou apenas (30): ").strip()
        arr = [int(x.strip()) for x in datei.split(",") if x.strip().isdigit()]
        today = datetime.now().date()
        if not datei:
            print("ERRO 301, entrada não inserida")
            return None

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
            return None

    if 4 in req_list:
        entrada_qtd = input("Insira a quantidade (ex: 10 para teto, ou 0, 10 para intervalo): ").strip()
        arr_qtd = [int(x.strip()) for x in entrada_qtd.split(",") if x.strip().isdigit()]
        if not entrada_qtd:
            print("ERRO 301, entrada não inserida")
            return None

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
            return None
    dados = lot_repo.read(query, params)
    colunas = lot_repo.get_columns()
    return colunas, dados