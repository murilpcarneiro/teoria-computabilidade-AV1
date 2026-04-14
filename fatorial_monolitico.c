/*
 * PROGRAMA MONOLÍTICO – Fatorial
 * Disciplina: Teoria da Computabilidade
 *
 * Estilo monolítico: sem funções auxiliares, sem laços estruturados.
 * O fluxo é controlado exclusivamente por rótulos e desvios (goto),
 * refletindo a lógica de uma máquina com estados explícitos.
 *
 * Função computada: f(n) = n!  para n >= 0
 *   f(0) = 1
 *   f(n) = n * (n-1) * ... * 1
 */

#include <stdio.h>

int main() {
    int n;
    long long resultado;
    int i;

    /* ESTADO 0 – Leitura da entrada */
    printf("Digite um numero inteiro nao-negativo: ");
    scanf("%d", &n);

    /* ESTADO 1 – Validação */
    if (n < 0) goto estado_erro;

    /* ESTADO 2 – Inicialização */
    resultado = 1;
    i = 1;

    /* ESTADO 3 – Teste de condição */
estado_teste:
    if (i > n) goto estado_saida;

    /* ESTADO 4 – Corpo da multiplicação */
    resultado = resultado * i;
    i = i + 1;
    goto estado_teste;

    /* ESTADO 5 – Saída */
estado_saida:
    printf("Fatorial de %d = %lld\n", n, resultado);
    return 0;

    /* ESTADO 6 – Erro */
estado_erro:
    printf("Erro: entrada invalida (n deve ser >= 0)\n");
    return 1;
}
