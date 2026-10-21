import pandas as pd


# Nomes usados na planilha, sem alterar os nomes reais do banco de dados.
NOMES_COLUNAS = {
    "lot_id": "Lote",
    "product_name": "Produto",
    "product_id": "ID do produto",
    "quant": "Quantidade",
    "price": "Preço",
    "date_valid": "Validade",
    "location": "Local",
    "status": "Status",
}


def _make_dataframe(colunas: list, dados: list) -> pd.DataFrame:
    """Monta o DataFrame e troca apenas os cabeçalhos da exportação."""
    df = pd.DataFrame(dados, columns=colunas)
    return df.rename(columns=NOMES_COLUNAS)


def make_xlsx(colunas: list, dados: list, nome_arquivo: str = "lotes.xlsx") -> None:
    """Recebe as colunas e os dados e salva em Excel."""
    df = _make_dataframe(colunas, dados)
    df.to_excel(nome_arquivo, index=False)
    print(f"\n[OK] Planilha '{nome_arquivo}' gerada com sucesso!")


def make_csv(colunas: list, dados: list, nome_arquivo: str = "lotes.csv") -> None:
    """Recebe as colunas e os dados e salva em CSV.

    sep=";" e utf-8-sig fazem o Excel em português abrir o arquivo
    com as colunas separadas e os acentos corretos.
    """
    df = _make_dataframe(colunas, dados)
    df.to_csv(nome_arquivo, index=False, sep=";", encoding="utf-8-sig")
    print(f"\n[OK] Arquivo CSV '{nome_arquivo}' gerado com sucesso!")
