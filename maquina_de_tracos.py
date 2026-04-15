"""
MÁQUINA DE TRAÇOS – Simulador
Disciplina: Teoria da Computabilidade

Simula a execução dos três programas (monolítico, iterativo, recursivo)
gerando as cadeias/rastros de execução no formato de fita, para análise
de equivalência forte.

Notação de estado da fita:
  (estado_atual, valor_i, valor_resultado) → próximo passo
"""

# ─────────────────────────────────────────────
#  MÁQUINA DE TRAÇOS – PROGRAMA MONOLÍTICO
#  Estados: S0(leitura), S1(validação), S2(init),
#           S3(teste), S4(corpo), S5(saída), S6(erro)
# ─────────────────────────────────────────────

def trace_monolitico(n):
    trace = []

    # S0 – leitura
    trace.append(f"S0 | entrada={n}")

    # S1 – validação
    if n < 0:
        trace.append(f"S1 | teste: {n} < 0 → TRUE → goto S6")
        trace.append(f"S6 | ERRO: entrada inválida")
        trace.append(f"⊥  | programa encerra (falha)")
        return trace

    trace.append(f"S1 | teste: {n} < 0 → FALSE → goto S2")

    # S2 – inicialização
    resultado = 1
    i = 1
    trace.append(f"S2 | init: resultado={resultado}, i={i}")

    # S3/S4 – laço com goto
    while True:
        # S3 – teste
        trace.append(f"S3 | teste: i={i} > n={n} → {'TRUE' if i > n else 'FALSE'}")
        if i > n:
            trace.append(f"     → goto S5")
            break
        # S4 – corpo
        resultado = resultado * i
        trace.append(f"S4 | resultado = resultado * i = {resultado // i} * {i} = {resultado}, i={i+1}")
        i += 1
        trace.append(f"     → goto S3")

    # S5 – saída
    trace.append(f"S5 | saída: {n}! = {resultado}")
    trace.append(f"✓  | programa encerra normalmente")
    return trace, resultado


# ─────────────────────────────────────────────
#  MÁQUINA DE TRAÇOS – PROGRAMA ITERATIVO
#  Estados: I0(init), I1(teste for), I2(corpo), I3(saída)
# ─────────────────────────────────────────────

def trace_iterativo(n):
    trace = []
    trace.append(f"I0 | entrada={n}, resultado=1, i=1")

    resultado = 1
    i = 1

    while i <= n:
        trace.append(f"I1 | teste: i={i} <= n={n} → TRUE")
        resultado *= i
        trace.append(f"I2 | resultado = {resultado // i} * {i} = {resultado}, i → {i+1}")
        i += 1

    trace.append(f"I1 | teste: i={i} <= n={n} → FALSE → sai do laço")
    trace.append(f"I3 | saída: {n}! = {resultado}")
    trace.append(f"✓  | programa encerra normalmente")
    return trace, resultado


# ─────────────────────────────────────────────
#  MÁQUINA DE TRAÇOS – PROGRAMA RECURSIVO
#  Estados: R0(chamada), Rbase(base), Rrec(retorno)
# ─────────────────────────────────────────────

def trace_recursivo(n, depth=0):
    trace = []
    indent = "  " * depth
    trace.append(f"{indent}R0 | chamada fatorial({n})")

    if n == 0:
        trace.append(f"{indent}Rb | CASO BASE: n=0 → retorna 1")
        return trace, 1

    subtrace, sub_resultado = trace_recursivo(n - 1, depth + 1)
    trace.extend(subtrace)

    resultado = n * sub_resultado
    trace.append(f"{indent}Rr | retorno: {n} * fatorial({n-1}) = {n} * {sub_resultado} = {resultado}")
    return trace, resultado


# ─────────────────────────────────────────────
#  ANÁLISE DE EQUIVALÊNCIA FORTE
# ─────────────────────────────────────────────

def comparar_traces(n, label_a, trace_a, resultado_a, label_b, trace_b, resultado_b):
    print(f"\n{'='*60}")
    print(f"  COMPARAÇÃO DE EQUIVALÊNCIA – entrada n={n}")
    print(f"{'='*60}")

    print(f"\n── Traço {label_a} ──")
    for linha in trace_a:
        print("  " + linha)

    print(f"\n── Traço {label_b} ──")
    for linha in trace_b:
        print("  " + linha)

    print(f"\n── Resultado {label_a}: {resultado_a}")
    print(f"── Resultado {label_b}: {resultado_b}")

    if resultado_a == resultado_b:
        print(f"\n✅ EQUIVALÊNCIA FORTE: ambos produzem o mesmo resultado ({resultado_a})")
        print(f"   Os programas computam a mesma função para n={n}.")
    else:
        print(f"\n❌ NÃO-EQUIVALÊNCIA: resultados divergem!")
        print(f"   {label_a} → {resultado_a} | {label_b} → {resultado_b}")


# ─────────────────────────────────────────────
#  PROGRAMA DE NÃO-EQUIVALÊNCIA (proposital)
#  Versão BUGADA do iterativo: começa i=0 (erra)
# ─────────────────────────────────────────────

def trace_iterativo_bugado(n):
    """
    Versão com bug: começa i=0 em vez de i=1.
    Isso faz resultado sempre ser 0 (multiplica por 0).
    Serve para demonstrar NÃO-EQUIVALÊNCIA.
    """
    trace = []
    trace.append(f"IB0 | entrada={n}, resultado=1, i=0  ← BUG: deveria iniciar em 1")

    resultado = 1
    i = 0  # BUG AQUI

    while i <= n:
        trace.append(f"IB1 | teste: i={i} <= n={n} → TRUE")
        resultado *= i
        trace.append(f"IB2 | resultado = {resultado // i if i != 0 else 'x'} * {i} = {resultado}, i → {i+1}")
        i += 1

    trace.append(f"IB1 | teste: i={i} <= n={n} → FALSE → sai do laço")
    trace.append(f"IB3 | saída: {n}! = {resultado}  ← INCORRETO")
    trace.append(f"✗   | programa encerra (resultado errado)")
    return trace, resultado


# ─────────────────────────────────────────────
#  NORMALIZAÇÃO DE TRAÇOS (ANÁLISE FORMAL)
# ─────────────────────────────────────────────

def extrair_passos_formais_monolitico(n):
    """
    Gera uma sequência de passos abstratos para o monolítico.
    Cada passo é uma tupla (operação, i, resultado).
    """
    passos = []

    if n < 0:
        passos.append(("erro_entrada", None, None))
        return passos

    resultado = 1
    i = 1
    passos.append(("init", i, resultado))

    while True:
        passos.append(("teste", i, resultado))
        if i > n:
            passos.append(("saida", i, resultado))
            break
        resultado *= i
        passos.append(("multiplica", i, resultado))
        i += 1

    return passos


def extrair_passos_formais_iterativo(n, iniciar_em_zero=False):
    """
    Gera sequência de passos abstratos para o iterativo.
    iniciar_em_zero=True reproduz a versão bugada.
    """
    passos = []

    if n < 0:
        passos.append(("erro_entrada", None, None))
        return passos

    resultado = 1
    i = 0 if iniciar_em_zero else 1
    passos.append(("init", i, resultado))

    while True:
        passos.append(("teste", i, resultado))
        if i > n:
            passos.append(("saida", i, resultado))
            break
        resultado *= i
        passos.append(("multiplica", i, resultado))
        i += 1

    return passos


def comparar_passos_formais(label_a, passos_a, label_b, passos_b):
    """
    Compara duas cadeias formais passo a passo.
    Retorna (equivalente, indice_primeira_divergencia).
    """
    limite = min(len(passos_a), len(passos_b))
    for idx in range(limite):
        if passos_a[idx] != passos_b[idx]:
            return False, idx

    if len(passos_a) != len(passos_b):
        return False, limite

    return True, None


def exibir_analise_formal(n, label_a, passos_a, label_b, passos_b):
    print(f"\n{'='*60}")
    print(f"  ANÁLISE FORMAL POR PASSOS – entrada n={n}")
    print(f"{'='*60}")
    print(f"\nCadeia formal {label_a} (passo, operação, i, resultado):")
    for idx, (op, i, r) in enumerate(passos_a, start=1):
        print(f"  {idx:02d}. ({op}, {i}, {r})")

    print(f"\nCadeia formal {label_b} (passo, operação, i, resultado):")
    for idx, (op, i, r) in enumerate(passos_b, start=1):
        print(f"  {idx:02d}. ({op}, {i}, {r})")

    equivalente, divergencia = comparar_passos_formais(label_a, passos_a, label_b, passos_b)
    if equivalente:
        print("\n✅ PROVA FORMAL: cadeias idênticas passo a passo.")
        print("   Conclusão: equivalência forte para a entrada analisada.")
        return

    print("\n❌ PROVA FORMAL: as cadeias divergem.")
    print(f"   Primeira divergência no passo {divergencia + 1}.")

    passo_a = passos_a[divergencia] if divergencia < len(passos_a) else "<sem passo>"
    passo_b = passos_b[divergencia] if divergencia < len(passos_b) else "<sem passo>"
    print(f"   {label_a}: {passo_a}")
    print(f"   {label_b}: {passo_b}")


# ─────────────────────────────────────────────
#  EXECUÇÃO PRINCIPAL
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("╔══════════════════════════════════════════════════════════╗")
    print("║         MÁQUINA DE TRAÇOS – FATORIAL                    ║")
    print("║         Teoria da Computabilidade – AV1                  ║")
    print("╚══════════════════════════════════════════════════════════╝")

    # Caso de teste
    N = 4

    print(f"\n{'─'*60}")
    print(f"  GERANDO TRAÇOS INDIVIDUAIS PARA n={N}")
    print(f"{'─'*60}")

    trace_m, res_m = trace_monolitico(N)
    trace_i, res_i = trace_iterativo(N)
    trace_r, res_r = trace_recursivo(N)

    print(f"\n── Traço Monolítico (n={N}) ──")
    for l in trace_m: print("  " + l)

    print(f"\n── Traço Iterativo (n={N}) ──")
    for l in trace_i: print("  " + l)

    print(f"\n── Traço Recursivo (n={N}) ──")
    for l in trace_r: print("  " + l)

    # ── CASO 1: EQUIVALÊNCIA (monolítico vs iterativo)
    print(f"\n\n{'═'*60}")
    print("  CASO 1 – EXEMPLO DE EQUIVALÊNCIA FORTE")
    print(f"  Comparando: Monolítico × Iterativo  (n={N})")
    print(f"{'═'*60}")
    comparar_traces(N,
        "Monolítico", trace_m, res_m,
        "Iterativo",  trace_i, res_i)

    passos_m = extrair_passos_formais_monolitico(N)
    passos_i = extrair_passos_formais_iterativo(N)
    exibir_analise_formal(N,
        "Monolítico", passos_m,
        "Iterativo",  passos_i)

    # ── CASO 2: NÃO-EQUIVALÊNCIA (iterativo vs iterativo bugado)
    trace_bug, res_bug = trace_iterativo_bugado(N)
    print(f"\n\n{'═'*60}")
    print("  CASO 2 – EXEMPLO DE NÃO-EQUIVALÊNCIA")
    print(f"  Comparando: Iterativo Correto × Iterativo com Bug  (n={N})")
    print(f"{'═'*60}")
    comparar_traces(N,
        "Iterativo Correto", trace_i, res_i,
        "Iterativo Bugado",  trace_bug, res_bug)

    passos_ib = extrair_passos_formais_iterativo(N, iniciar_em_zero=True)
    exibir_analise_formal(N,
        "Iterativo Correto", passos_i,
        "Iterativo Bugado",  passos_ib)

    print(f"\n{'─'*60}")
    print("  TABELA RESUMO DE EXECUÇÕES")
    print(f"{'─'*60}")
    print(f"  {'n':>4} | {'Monolítico':>12} | {'Iterativo':>10} | {'Recursivo':>10}")
    print(f"  {'─'*4}-+-{'─'*12}-+-{'─'*10}-+-{'─'*10}")
    for n_test in [0, 1, 3, 4, 5]:
        _, r_m = trace_monolitico(n_test)
        _, r_i = trace_iterativo(n_test)
        _, r_r = trace_recursivo(n_test)
        print(f"  {n_test:>4} | {r_m:>12} | {r_i:>10} | {r_r:>10}")
    print()
