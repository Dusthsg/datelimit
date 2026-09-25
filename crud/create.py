from datetime import datetime
from database import conn, cursor
from models import NewLotItem

def add_product():
   try:
       input_name = str(input("Digite o nome do Produto: "))
       input_quant = int(input("Digite a quantidade do produto: "))
       input_date_valid = input("Data de validade (DD/MM/AAAA): ").strip()

       data_obj = datetime.strptime(input_date_valid, "%Y/%m/%d")
       validade_iso = data_obj.strftime("%Y-%m-%d")

       product = NewLotItem(input_name, input_quant, validade_iso)
       send_product = "INSERT INTO products (name, quant, date_valid) VALUES (?, ?, ?)"

       cursor.execute(send_product, product.to_tuple())
       conn.commit()
       print("-> Produto cadastrado com sucesso!")


   except ValueError:
        print("-> Erro: Verifique os dados digitados. A data deve estar no formato DD/MM/AAAA.")