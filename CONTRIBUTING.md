# Contribuindo com o DateLimit

Obrigado por contribuir com o DateLimit.

O projeto está em evolução e, neste momento, uma das prioridades é melhorar sua arquitetura sem quebrar o comportamento existente.

## Antes de começar

Leia:

- [README.md](README.md)
- Os requisitos funcionais e não funcionais acompanhados nas Issues do GitHub.
- As Issues relacionadas à tarefa que você pretende implementar.

## Fluxo de desenvolvimento

Sempre que possível:

1. Escolha ou abra uma Issue.
2. Entenda os critérios de aceitação.
3. Crie uma branch específica.
4. Faça uma mudança pequena e verificável.
5. Teste o comportamento.
6. Faça um commit com uma mensagem clara.
7. Abra um Pull Request descrevendo a mudança.

Exemplo:

```bash
git checkout -b feat/product-repository
```

## Convenção de branches

Prefira nomes que indiquem a intenção da alteração:

```text
feat/nome-da-funcionalidade
fix/nome-do-problema
refactor/nome-da-refatoracao
docs/nome-da-documentacao
test/nome-dos-testes
chore/nome-da-tarefa
```

## Commits

Prefira mensagens curtas e objetivas.

Exemplos:

```text
feat: add product repository
fix: validate advanced search options
refactor: migrate lot queries to repository
docs: add contribution guide
test: add product repository tests
```

Evite commits que misturem mudanças sem relação.

## Arquitetura

O DateLimit está migrando gradualmente para uma separação semelhante a:

```text
View
  ↓
Controller
  ↓
Service
  ↓
Repository
  ↓
Database
```

### Repository

O Repository é responsável pelo acesso e persistência dos dados.

Ele deve encapsular o SQL e os detalhes necessários para conversar com o banco.

Não coloque nele:

- `input()`
- `print()`
- regras de apresentação
- lógica específica de interface

### Service

Services devem concentrar regras de negócio quando sua complexidade justificar uma camada própria.

### Controller

O Controller deve coordenar o fluxo da aplicação, evitando acumular SQL e lógica de apresentação.

### View

Views serão responsáveis pela interação e apresentação ao usuário.

## Refatorações

O projeto prefere refatorações incrementais.

Não remova uma camada antiga antes de garantir que a responsabilidade correspondente já foi migrada e testada.

Na branch de refatoração, por exemplo, a pasta `crud/` permanece temporariamente para permitir uma migração gradual para `repositories/`.

## Pull Requests

Um Pull Request deve explicar:

- O que foi alterado.
- Por que a alteração foi necessária.
- Qual Issue ela resolve.
- Como foi testada.
- Se existe algum impacto conhecido.

Exemplo:

```text
Closes #XX
```

## O que evitar

- Introduzir abstrações sem necessidade.
- Refatorar arquivos não relacionados à tarefa.
- Alterar comportamento existente sem documentar.
- Adicionar dependências sem justificativa.
- Commitar bancos locais, credenciais ou arquivos gerados.
