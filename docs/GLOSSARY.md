# Glossário — DateLimit

Este documento reúne os principais termos e conceitos utilizados no DateLimit.

## Produto (Product)

Representa um item comercial de forma geral.

O produto contém informações que identificam o item e que são compartilhadas entre seus diferentes lotes.

Exemplos de atributos:

- ID
- Nome
- Código de barras

---

## Lote (Lot)

Representa um conjunto específico de unidades de um produto.

Um produto pode possuir vários lotes, e cada lote pode possuir informações próprias.

Exemplos de atributos:

- ID
- Quantidade
- Preço
- Data de validade
- Localização
- Status

---

## Entidade (Entity)

No DateLimit, uma **Entidade** representa um produto associado a um lote específico.

A entidade reúne as informações necessárias para identificar, consultar e manipular uma ocorrência específica de um produto no sistema.

Conceitualmente:

```text
Entidade
├── Produto
└── Lote
```

Um mesmo produto pode, portanto, originar várias entidades quando possui diferentes lotes.

---

## Repository

Componente responsável por encapsular o acesso e a persistência dos dados.

No DateLimit, os repositories concentram as operações relacionadas ao banco de dados, como criação, consulta, atualização e exclusão.

Exemplos:

- ProductRepository
- LotRepository

---

## View

Componente responsável pela interação com o usuário.

A View apresenta informações, recebe entradas e encaminha os dados para o fluxo da aplicação.

Exemplos atuais:

- Menus
- Telas da CLI

---

## Controller

Componente responsável por coordenar o fluxo das operações do sistema.

O Controller recebe informações da View, utiliza os componentes necessários e determina quais operações devem ser executadas.

---

## Domínio (Domain)

Conjunto de conceitos, entidades e regras que representam o problema que o sistema procura resolver.

No DateLimit, fazem parte do domínio conceitos como:

- Produto
- Lote
- Entidade
- Validade
- Quantidade
- Localização
- Status

---

## Arquitetura Hexagonal

Modelo arquitetural que busca manter o núcleo da aplicação independente de detalhes externos, como banco de dados, interface e frameworks.

É um objetivo arquitetural futuro do DateLimit e não representa a estrutura final atualmente implementada.

---

## SQLite

Sistema de banco de dados relacional utilizado atualmente pelo DateLimit.

---

## PostgreSQL

Sistema de banco de dados relacional previsto para uma futura evolução do DateLimit, especialmente para cenários que exigem maior concorrência e escalabilidade.

---

## Status

Representa a situação atual de um lote dentro do sistema.

Exemplos de possíveis estados:

- NORMAL
- ATENÇÃO
- CRÍTICO
- VENCIDO

A lista definitiva de status pode evoluir conforme as regras do sistema forem implementadas.

---

## Localização (Location)

Representa o local físico associado a um lote.

Exemplos:

- LOJA
- ESTOQUE
- DEPÓSITO

---

## RF — Requisito Funcional

Define uma funcionalidade ou comportamento que o sistema deve oferecer.

Exemplo:

```text
RF01 — Cadastro de produtos e lotes
```

---

## RNF — Requisito Não Funcional

Define uma característica ou restrição relacionada à qualidade, arquitetura, desempenho ou operação do sistema.

Exemplos:

- desempenho
- escalabilidade
- segurança
- concorrência

---

## Refatoração

Processo de reorganização e melhoria da estrutura interna do código sem alterar intencionalmente seu comportamento externo.

Objetivos comuns:

- melhorar legibilidade;
- reduzir acoplamento;
- melhorar manutenção;
- facilitar testes.

---

## Teste Automatizado

Código executado automaticamente para verificar se determinado comportamento continua funcionando conforme esperado.

O DateLimit utiliza inicialmente `doctest` como forma simples de introduzir testes automatizados.

---

## Doctest

Ferramenta nativa do Python que permite transformar exemplos escritos em docstrings em testes executáveis.

Exemplo:

```python
def add(a, b):
    """
    >>> add(2, 3)
    5
    """
    return a + b
```

---

## SQLite em memória

Banco SQLite temporário criado com `sqlite3.connect(":memory:")`.

É utilizado para executar testes sem modificar o banco de dados real do DateLimit.

---

## Branch

Linha de desenvolvimento independente dentro do Git.

Exemplo:

```text
main
feat/refactoring
```

---

## Commit

Registro de uma alteração no histórico do Git.

Um commit representa um conjunto de mudanças que pode ser identificado e recuperado posteriormente.

---

## Pull Request (PR)

Solicitação para integrar alterações de uma branch em outra através do GitHub.

---

## Issue

Registro utilizado no GitHub para acompanhar tarefas, correções, melhorias ou requisitos do projeto.
