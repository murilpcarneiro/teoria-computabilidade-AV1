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
trabalho-computabilidade/
├── src/
│   ├── fatorial_monolitico.c   ← programa monolítico (usa goto)
│   ├── fatorial_iterativo.c    ← programa iterativo (usa for)
│   ├── fatorial_recursivo.c    ← programa recursivo
│   └── maquina_de_tracos.py   ← simulador da Máquina de Traços
└── README.md
```

---

## Instruções de Compilação e Execução

### Pré-requisitos
- GCC (qualquer versão moderna)
- Python 3.6+

### Compilar os programas C

```bash
gcc src/fatorial_monolitico.c -o fatorial_monolitico
gcc src/fatorial_iterativo.c  -o fatorial_iterativo
gcc src/fatorial_recursivo.c  -o fatorial_recursivo
```

### Executar os programas C

```bash
./fatorial_monolitico   # solicita n e imprime n!
./fatorial_iterativo
./fatorial_recursivo
```

### Executar a Máquina de Traços

```bash
python3 src/maquina_de_tracos.py
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
