# Arquitetura do Código Atual

> Documento de referência da estrutura atual do DateLimit.
>
> Este documento descreve como o código está organizado atualmente e qual é a responsabilidade de cada parte. Ele não representa a arquitetura final do projeto.

---

## 1. Visão geral

Atualmente, o DateLimit utiliza uma separação baseada principalmente em:

```
View
  ↓
Controller
  ↓
Repository
  ↓
Database
```

O projeto também possui `Models`, que representam dados e algumas operações relacionadas ao domínio.

A responsabilidade geral pode ser resumida assim:

```
View        → pergunta e mostra
Controller  → coordena e decide
Repository  → acessa e modifica o banco
Model       → representa dados e conceitos do sistema
Database    → configura a infraestrutura do banco
```

A separação ainda está em evolução. Algumas responsabilidades ainda estão misturadas e serão refatoradas posteriormente.

---

## 2. Fluxo geral

Uma operação normalmente segue:

```
Usuário
   │
   ▼
 View
   │
   ▼
Controller
   │
   ▼
Repository
   │
   ▼
SQLite
```

E o resultado retorna pelo caminho inverso:

```
SQLite
  ↓
Repository
  ↓
Controller
  ↓
View
  ↓
Usuário
```

A ideia é evitar que todas as partes do sistema conheçam todos os detalhes umas das outras.

---

## 3. View

### Responsabilidade

A `View` é responsável pela interação visual com o usuário.

Ela deve:

- mostrar informações;
- mostrar menus;
- solicitar dados;
- formatar informações para exibição;
- receber entradas do usuário.

Estrutura atual:

```
views/
├── menus.py
└── screens.py
```

### menus.py

Responsável principalmente pela apresentação das opções disponíveis.

### screens.py

Responsável por apresentar informações e solicitar determinados dados.

### O que a View não deveria fazer

A View não deveria ser responsável por:

- executar SQL;
- decidir regras de negócio;
- modificar diretamente o banco;
- descobrir como um produto é armazenado;
- executar consultas diretamente.

Por exemplo, isto não pertence à View:

```python
cursor.execute(
    "SELECT * FROM products WHERE name = ?",
    (name,)
)
```

A View não precisa saber como o banco está implementado.

---

## 4. Controller

### Responsabilidade

O `Controller` coordena o fluxo da aplicação.

Ele recebe informações da View, decide o que precisa acontecer e utiliza os Repositories para executar operações.

Em termos simples:

```
View pergunta
      ↓
Controller decide
      ↓
Repository executa
```

O Controller pode:

- interpretar uma opção de menu;
- chamar o Repository correto;
- controlar o fluxo de uma operação;
- coordenar várias operações;
- decidir qual View apresentar depois.

### Exemplo

Ao atualizar um lote:

```
Usuário
   ↓
View
   ↓
Controller
   ↓
LotRepository
   ↓
Banco
```

O Controller pode determinar:

1. Qual lote será alterado?
2. Qual campo será alterado?
3. Qual Repository deve executar a operação?
4. Qual View deve mostrar o resultado?

O Controller não deveria precisar conhecer o SQL.

Idealmente:

```python
lot_repo.update(lot_id, {
    "location": "A-03"
})
```

em vez de executar diretamente:

```python
cursor.execute(
    "UPDATE product_lots SET location = ? WHERE id = ?",
    ("A-03", lot_id)
)
```

O SQL pertence ao Repository.

---

## 5. Repository

### Responsabilidade

O Repository é a camada responsável pelo acesso aos dados persistidos.

No DateLimit, isso significa principalmente conversar com o SQLite.

Estrutura atual:

```
repositories/
├── product_repository.py
└── lot_repository.py
```

Cada Repository concentra operações relacionadas a determinado conjunto de dados.

---

## 6. ProductRepository

O `ProductRepository` é responsável pelas operações relacionadas aos produtos.

Operações atuais incluem:

```
create()
get_by_name()
search_by_name()
update_name()
delete()
```

O Controller não precisa conhecer os detalhes do SQL.

Exemplo:

```python
product_id = product_repo.get_by_name("Coca-Cola")
```

O Controller solicita a operação.

Internamente, o Repository pode executar uma consulta como:

```sql
SELECT id
FROM products
WHERE name = ?
```

A diferença é:

```
Controller
"Quero encontrar este produto."

Repository
"Eu sei como encontrar esse produto no banco."
```

---

## 7. LotRepository

O `LotRepository` é responsável pelas operações relacionadas aos lotes.

Operações atuais incluem:

```
create()
delete()
update()
read()
get_columns()
```

O lote possui informações específicas da ocorrência do produto:

```
id
product_id
quant
price
date_valid
location
status
```

O `LotRepository` também realiza consultas envolvendo `products` e `product_lots`.

Uma consulta pode retornar:

```
lot_id
product_name
product_id
quant
price
date_valid
location
status
```

Essa tupla grande é uma limitação atual que será reduzida posteriormente com objetos/dataclasses.

---

## 8. Por que o Repository existe?

Sem Repository, o Controller poderia acabar concentrando:

```
Controller
├── SQL de criação
├── SQL de consulta
├── SQL de atualização
├── SQL de exclusão
├── tratamento do banco
├── regras de fluxo
└── interação com View
```

Com Repository:

```
Controller
└── coordena operações

ProductRepository
└── operações de Product

LotRepository
└── operações de Lot
```

O objetivo é concentrar o conhecimento sobre persistência.

---

## 9. Database

O arquivo:

```
database.py
```

é responsável pela infraestrutura inicial do banco.

Atualmente ele:

- cria/conecta ao SQLite;
- configura a conexão;
- cria as tabelas;
- ativa foreign keys;
- realiza configurações iniciais.

O banco atual possui principalmente:

```
products
product_lots
```

Relação:

```
Product
   │
   │ 1
   │
   └──────────< N
               Lot
```

Um produto pode possuir vários lotes.

---

## 10. Model

O projeto também possui:

```
models.py
```

Atualmente existem estruturas como `NewLotItem`.

Essa parte ainda está em evolução.

O objetivo futuro é separar melhor:

```
Representação dos dados
        +
Regras do domínio
```

da persistência.

Atualmente, algumas responsabilidades ainda estão misturadas. Isso não precisa ser resolvido imediatamente.

---

## 11. Como as partes se relacionam

Uma operação de criação pode ser entendida assim:

```
┌──────────────┐
│     View     │
│              │
│ recebe dados │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Controller  │
│              │
│ coordena     │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Repository  │
│              │
│ persiste     │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    SQLite    │
└──────────────┘
```

O caminho de volta:

```
SQLite
  ↓
Repository
  ↓
Controller
  ↓
View
  ↓
Usuário
```

---

## 12. Regra rápida

Quando estiver escrevendo código e não souber onde colocar algo:

```
"Preciso mostrar alguma coisa?"
        ↓
      VIEW

"Preciso perguntar alguma coisa?"
        ↓
      VIEW

"Preciso decidir qual operação executar?"
        ↓
   CONTROLLER

"Preciso coordenar várias operações?"
        ↓
   CONTROLLER

"Preciso fazer SQL?"
        ↓
   REPOSITORY

"Preciso buscar, criar, atualizar ou excluir dados?"
        ↓
   REPOSITORY

"Preciso representar um conceito/dado do domínio?"
        ↓
     MODEL

"Preciso configurar o banco?"
        ↓
    DATABASE
```

---

## 13. Uma regra importante

Não pense:

> "Preciso colocar isso na arquitetura perfeita."

Pense primeiro:

> "Quem deveria ser responsável por isso?"

A arquitetura pode evoluir.

Por enquanto, o objetivo é manter responsabilidades suficientemente separadas para que o projeto continue compreensível.

---

## 14. O que não fazer

### Evitar SQL na View

```python
# Evitar
cursor.execute(...)
```

A View não precisa conhecer o banco.

### Evitar SQL no Controller

```python
# Evitar
cursor.execute(
    "UPDATE product_lots SET status = ? WHERE id = ?",
    (status, lot_id)
)
```

O Controller deve solicitar a operação ao Repository.

### Evitar interação com o usuário no Repository

```python
# Evitar
name = input("Nome: ")
```

O Repository não conversa com o usuário.

### Evitar menus no Repository

```python
# Evitar
print("1 - Atualizar")
print("2 - Excluir")
```

O Repository não controla a interface.

---

## 15. Estado atual x objetivo futuro

A arquitetura atual é:

```
View
 ↓
Controller
 ↓
Repository
 ↓
Database
```

O projeto possui uma direção futura de evolução:

```
        ┌───────────────┐
        │    Domain     │
        └───────────────┘
                ▲
                │
        ┌───────┴───────┐
        │               │
    Application      Adapters
        │               │
        │          ┌────┴────┐
        │          │         │
      View       SQLite     Web
```

Isso se aproxima da arquitetura hexagonal.

Porém:

> **A arquitetura hexagonal é um objetivo futuro, não uma obrigação para o código atual.**

O código atual deve ser compreendido e estabilizado antes de uma mudança arquitetural maior.

---

## 16. Próximas evoluções naturais

A evolução esperada é aproximadamente:

```
Código atual
     ↓
Corrigir bugs atuais
     ↓
Testes automatizados
     ↓
Melhorar representação dos dados
     ↓
Reduzir tuplas grandes
     ↓
Dataclasses / objetos de domínio
     ↓
Refinar Repositories
     ↓
Separar melhor regras de negócio
     ↓
Testes mais completos
     ↓
Arquitetura hexagonal
```

Não é necessário executar todas essas etapas de uma vez.

---

## 17. Testes e Repository

Os Repositories possuem uma característica importante para testes:

```python
ProductRepository(connection)
LotRepository(connection)
```

A possibilidade de passar uma conexão permite utilizar:

```python
sqlite3.connect(":memory:")
```

durante os testes.

Assim:

```
Teste
  ↓
SQLite em memória
  ↓
Repository
```

sem alterar o banco real do projeto.

Isso torna os Repositories um bom ponto inicial para os testes automatizados.

---

## 18. A arquitetura em uma frase

> **A View conversa com o usuário, o Controller coordena o fluxo, o Repository conversa com o banco e o Model representa os dados/conceitos do sistema.**

---

## 19. Não é necessário decorar

Este documento existe justamente para evitar que a arquitetura precise ficar toda na memória.

Durante o desenvolvimento, é normal esquecer:

- qual classe faz determinada operação;
- onde uma regra deveria ficar;
- qual camada deveria acessar o banco;
- qual Repository deve ser utilizado;
- como determinada parte do sistema funciona.

Isso não significa que você não entende o projeto.

Um projeto começa a ficar grande demais para depender apenas da memória do desenvolvedor.

Por isso, documentação, testes e uma estrutura clara fazem parte do próprio desenvolvimento do sistema.
