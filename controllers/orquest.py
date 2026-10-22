from archive_mp.export import make_xlsx, make_csv
from views.screens import show_data

def orquest(colunas: list, dados: list) -> None:
    """Recebe os dados que já foram consultados e decide a exportação."""
    if not dados:
        print("\nNenhum registro encontrado para exportar.")
        return
    show_data(dados)

    # opção digitada -> (função de exportação, nome padrão, extensão)
    formatos = {
        "x": (make_xlsx, "lotes.xlsx", ".xlsx"),
        "c": (make_csv, "lotes.csv", ".csv"),
    }

    while True:
        opcao = input("\nExportar os dados? [x] Excel  [c] CSV  [n] Não: ").strip().lower()

        if opcao == "n":
            print("Finalizado sem exportação.")
            return

        if opcao not in formatos:
            print("Opção inválida! Digite x, c ou n.")
            continue

        funcao, nome_padrao, extensao = formatos[opcao]
        nome = input(f"Nome do arquivo (Enter para '{nome_padrao}'): ").strip() or nome_padrao
        if not nome.endswith(extensao):
            nome += extensao

        try:
            funcao(colunas, dados, nome)
        except OSError as erro:
            # arquivo aberto em outro programa, pasta inexistente, sem permissão etc.
            print(f"\n[ERRO] Não foi possível salvar '{nome}': {erro}")
            continue
        return