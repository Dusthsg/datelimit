import pandas as pd


def make_xlsx(colunas: list, dados: list, nome_arquivo: str = "lotes.xlsx") -> None:
    """Recebe as colunas e os dados e salva em Excel."""
    df = pd.DataFrame(dados, columns=colunas)
    df.to_excel(nome_arquivo, index=False)
    print(f"\n[OK] Planilha '{nome_arquivo}' gerada com sucesso!")


def make_csv(colunas: list, dados: list, nome_arquivo: str = "lotes.csv") -> None:
    """Recebe as colunas e os dados e salva em CSV.

    sep=";" e utf-8-sig fazem o Excel em português abrir o arquivo
    com as colunas separadas e os acentos corretos.
    """
    df = pd.DataFrame(dados, columns=colunas)
    df.to_csv(nome_arquivo, index=False, sep=";", encoding="utf-8-sig")
    print(f"\n[OK] Arquivo CSV '{nome_arquivo}' gerado com sucesso!")
