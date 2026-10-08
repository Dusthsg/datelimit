# Modelo de Domínio — DateLimit

Este documento define os principais conceitos do domínio do DateLimit e a relação entre eles.

O objetivo é estabelecer o significado dos conceitos antes de definir como eles serão representados no código.

---

## Entidade

No DateLimit, uma **Entidade** representa um produto associado a um lote específico.

Uma entidade reúne as informações necessárias para que o sistema possa identificar, consultar e manipular uma ocorrência específica de um produto dentro do estoque.

A entidade não deve ser confundida com o Produto ou com o Lote isoladamente.

### Composição conceitual

```text
Entidade
├── Produto
│   ├── ID
│   ├── Nome
│   └── Código de barras
│
└── Lote
    ├── ID
    ├── Quantidade
    ├── Preço
    ├── Data de validade
    ├── Localização
    └── Status
```

---

## Produto

O **Produto** representa o item comercial de forma geral.

Suas informações identificam o produto independentemente de qual lote esteja sendo manipulado.

Exemplo:

```text
Produto
    Nome: Coca-Cola 2L
    Código de barras: 7890000000000
```

Um mesmo produto pode possuir vários lotes.

---

## Lote

O **Lote** representa uma ocorrência específica de um produto.

As informações do lote podem variar entre diferentes lotes do mesmo produto.

Exemplo:

```text
Lote
    ID: 15
    Quantidade: 20
    Preço: R$ 8,50
    Validade: 10/10/2026
    Localização: LOJA
    Status: NORMAL
```

---

## Relação entre Produto e Lote

A relação conceitual é:

```text
Produto
   │
   ├── Lote 15
   ├── Lote 27
   └── Lote 31
```

Cada lote pertence a um produto.

Portanto:

- um produto pode possuir vários lotes;
- cada lote está associado a um produto;
- lotes diferentes do mesmo produto podem possuir informações diferentes.

---

## Relação entre Produto, Lote e Entidade

Quando um produto é associado a um lote específico, essa combinação representa uma entidade do DateLimit.

Exemplo:

```text
Produto: Coca-Cola 2L

├── Lote 15
│   └── Entidade 1
│
├── Lote 27
│   └── Entidade 2
│
└── Lote 31
    └── Entidade 3
```

Nesse exemplo existe um único produto, três lotes e três entidades.

Cada entidade representa uma ocorrência específica do produto no contexto de um lote.

---

## Representação no banco de dados

Atualmente, o banco separa Produto e Lote em tabelas distintas:

```text
products
    │
    │ 1:N
    ▼
product_lots
```

A tabela `products` contém informações próprias do produto:

```text
products
├── id
├── name
└── bar_code
```

A tabela `product_lots` contém informações próprias do lote e sua referência ao produto:

```text
product_lots
├── id
├── product_id
├── quant
├── price
├── date_valid
├── location
└── status
```

O campo `product_id` estabelece a relação entre o lote e o produto.

---

## Entidade e implementação

O conceito de Entidade é uma definição do domínio e não determina, por si só, como ela deve ser implementada no código.

A implementação poderá evoluir conforme o projeto amadurecer.

Uma possível representação futura poderá utilizar objetos ou `dataclass`, mas essa decisão pertence à implementação e não à definição do domínio.

---

## Objetivo do modelo

O modelo de domínio serve como referência para manter consistente o significado dos conceitos utilizados no DateLimit.

Antes de criar ou alterar uma estrutura de código, deve ser possível responder:

- O que esse objeto representa?
- Ele pertence ao Produto ou ao Lote?
- Ele faz parte da Entidade?
- Essa informação é própria do produto ou pode variar entre lotes?

Dessa forma, a documentação funciona como uma referência para o desenvolvimento sem exigir que todos os conceitos do sistema sejam mantidos apenas na memória do desenvolvedor.
