# DateLimit

> Sistema de gerenciamento de produtos, lotes e validade de estoque.

## Sobre

O **DateLimit** nasceu como uma aplicação CLI para auxiliar no controle de produtos perecíveis e seus lotes, com foco em validade, quantidade e identificação de itens próximos do vencimento.

O projeto está evoluindo de uma aplicação local em Python/SQLite para uma arquitetura preparada para interface web, PostgreSQL, automações, auditoria e, posteriormente, análise preditiva de estoque.

## Status

🚧 **Em desenvolvimento**

A versão atual ainda está em evolução. A branch `feat/refactoring` concentra a reorganização interna da aplicação, começando pela camada de persistência com o padrão Repository.

## Principais objetivos

- Gerenciar produtos e lotes.
- Monitorar datas de validade.
- Pesquisar e filtrar estoque.
- Exportar relatórios.
- Controlar localização física dos lotes.
- Registrar movimentações de estoque.
- Automatizar alertas e relatórios.
- Preparar a aplicação para PostgreSQL e acesso concorrente.
- Construir uma base histórica para analytics e Machine Learning.

## Requisitos

### Funcionais

- **RF01** — CRUD de Produtos e Lotes
- **RF02** — Atualização Dinâmica de Lotes
- **RF03** — Controle e Monitoramento de Validade
- **RF04** — Busca e Filtragem Avançada
- **RF05** — Manipulação e Exportação de Planilhas
- **RF06** — Interface Gráfica Responsiva
- **RF07** — Launcher da aplicação
- **RF08** — Download direto de relatórios
- **RF09** — Agendamento de relatórios
- **RF10** — Alertas automáticos
- **RF11–RF14** — Motor de status e regras
- **RF15–RF17** — Localização e transferências
- **RF18–RF22** — Histórico, previsões, recomendações e métricas

Os requisitos completos são acompanhados no GitHub através das Issues do projeto.

### Não funcionais

Entre os objetivos arquiteturais estão:

- PostgreSQL para cenários concorrentes.
- Repository Pattern.
- Integridade referencial e transações.
- Interface responsiva.
- Inicialização simplificada.
- Processamento em segundo plano.
- Consultas eficientes.
- Logs e auditoria.
- Pipeline de ML isolado das operações.
- Fallback para cold start.
- Previsões interpretáveis.

## Arquitetura em evolução

A arquitetura atual está sendo migrada gradualmente para:

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

A branch `feat/refactoring` começou pela camada de Repository.

A intenção é migrar gradualmente as responsabilidades existentes de `crud/` para os repositories, depois separar a apresentação através de Views e introduzir Services quando a lógica de negócio justificar essa camada.

## Estrutura em evolução

```text
datelimit/
├── main.py
├── controller.py
├── models.py
├── database.py
├── repositories/
│   ├── product_repository.py
│   └── lot_repository.py
├── crud/                 # legado durante a migração
├── archive_mp/
└── database/
```

A pasta `crud/` será removida somente depois que suas responsabilidades forem migradas e validadas.

## Tecnologia atual

- Python
- SQLite
- SQL parametrizado
- Exportação de dados para planilhas
- Git/GitHub

## Visão futura

O DateLimit pretende evoluir para uma plataforma capaz de:

```text
Estoque
  ↓
Movimentações
  ↓
Histórico
  ↓
Analytics
  ↓
Previsão de risco
  ↓
Recomendação de ação
```

O Machine Learning será construído sobre dados históricos reais de movimentação. A prioridade é primeiro garantir uma base operacional e de dados confiável.

## Desenvolvimento

Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para orientações sobre desenvolvimento, branches, commits e Pull Requests.

## Segurança

Consulte [SECURITY.md](SECURITY.md) para reportar vulnerabilidades.

## Licença

Este projeto ainda não possui uma licença open source definida. Não assuma permissão para redistribuição ou uso comercial até que uma licença seja adicionada.
