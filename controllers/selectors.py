def selector(data: list):
    if not data:
        print("\nNenhum registro para selecionar.")
        return None

    for i, row in enumerate(data, start=1):
        print(f"\n[{i:<4}] Lote #{row.lot_id} | {row.product_name:<30} | Qtd: {row.quant:<5} | Preço: R$ {row.price:<7.2f} | Validade: {row.date_valid}")
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