# Trabalho AV1 – Teoria da Computabilidade
**Programas, Máquinas e Equivalência**

Disciplina: Teoria da Computabilidade  
Professor: Daniel Leal Souza  
Turmas: CC5MA / CC5NA – Semestre 01/2026  

---

## Integrantes da Equipe
Pedro Lyra, Murilo Pantoja, Vithor dos Santos, João Felipe Soares
---

## Função Implementada

**Fatorial** — `f(n) = n!` para `n ≥ 0`

| n | f(n) |
|---|------|
| 0 | 1 |
| 1 | 1 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |

- **Entrada:** inteiro não-negativo `n`
- **Saída:** inteiro longo `n!`
- **Caso especial:** `0! = 1` (por definição)

---

## Linguagens Utilizadas

| Programa | Linguagem |
|---|---|
| Monolítico | C (com `goto`) |
| Iterativo | C (com `for`) |
| Recursivo | C (com chamada recursiva) |
| Máquina de Traços | Python 3 |

---

## Organização dos Arquivos

```
teoria-computabilidade-AV1/
├── fatorial_monolitico.c     ← programa monolítico (usa goto)
├── fatorial_iterativo.c      ← programa iterativo (usa for)
├── fatorial_recursivo.c      ← programa recursivo
├── fatorial_monolitico.exe   ← binário pronto para execução
├── fatorial_iterativo.exe    ← binário pronto para execução
├── fatorial_recursivo.exe    ← binário pronto para execução
├── maquina_de_tracos.py      ← simulador da Máquina de Traços
└── README.md
```

---

## Instruções de Execução (sem GCC)

### Pré-requisitos
- Python 3.6+

### Executar os programas C (binários prontos)

```bash
./fatorial_monolitico.exe
./fatorial_iterativo.exe
./fatorial_recursivo.exe
```

No Windows PowerShell:

```bash
.\fatorial_monolitico.exe
.\fatorial_iterativo.exe
.\fatorial_recursivo.exe
```

### Executar a Máquina de Traços

```bash
python maquina_de_tracos.py
```

No Windows PowerShell (com ambiente virtual local):

```bash
.\.venv\Scripts\python.exe .\maquina_de_tracos.py
```

### Executar pelo VS Code (Tasks)

Se o projeto tiver o arquivo `.vscode/tasks.json`, use:

1. `Terminal > Run Task`
2. Escolha uma das tarefas:
	- `Rodar C: monolitico`
	- `Rodar C: iterativo`
	- `Rodar C: recursivo`
	- `Rodar Python: maquina de tracos`
	- `Rodar todos os codigos`

### Compilação (opcional)

Se você instalar GCC no futuro, pode recompilar com:

```bash
gcc fatorial_monolitico.c -o fatorial_monolitico.exe
gcc fatorial_iterativo.c  -o fatorial_iterativo.exe
gcc fatorial_recursivo.c  -o fatorial_recursivo.exe
```

A Máquina de Traços gera:
- Traço completo dos três programas para `n=4`
- Análise de **equivalência forte** (Monolítico × Iterativo)
- Análise de **não-equivalência** (Iterativo Correto × Iterativo Bugado)
- Tabela resumo de execuções

---

## Descrição dos Programas

### Monolítico (`fatorial_monolitico.c`)
Fluxo controlado exclusivamente por `goto`. Sem funções auxiliares, sem laços estruturados. Os estados são explícitos via rótulos (`estado_teste`, `estado_saida`, `estado_erro`), refletindo a lógica de máquina com estados.

### Iterativo (`fatorial_iterativo.c`)
Usa estrutura de repetição `for` explícita. A variável `i` percorre de 1 a `n`, acumulando o produto em `resultado`.

### Recursivo (`fatorial_recursivo.c`)
A função `fatorial_recursivo(n)` se chama diretamente. A condição-base é `n == 0 → retorna 1`. Cada chamada reduz o problema em 1 unidade até atingir a base.

---

## Uso de Inteligência Artificial

| Item | Detalhe |
|---|---|
| Ferramenta | Claude (Anthropic) |
| Finalidade | Suporte na estruturação do trabalho, geração inicial dos códigos e simulador |
| Trechos aproveitados | Estrutura dos três programas C e simulador Python |
| Revisões da equipe | Validação dos traços, verificação da lógica dos estados, adequação à notação da disciplina |
