from database import conn, cursor


def delete_product():
    inputNI = input("Insira o ID ou nome do produto para remover: ")
    query = ("""DELETE FROM products WHERE id = ? OR name = ?""")
    cursor.execute(query, (inputNI, inputNI))
    conn.commit()

    if cursor.rowcount > 0:
        print("-> Produto removido com sucesso!")
    else:
        print("-> Nenhum produto encontrado com esse ID ou Nome.")