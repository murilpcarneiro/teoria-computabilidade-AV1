/*
 * PROGRAMA ITERATIVO – Fatorial
 * Disciplina: Teoria da Computabilidade
 *
 * Estilo iterativo: o controle de fluxo usa estrutura de repetição
 * explícita (for), sem chamadas recursivas.
 *
 * Função computada: f(n) = n!  para n >= 0
 */

#include <stdio.h>

long long fatorial_iterativo(int n) {
    long long resultado = 1;
    for (int i = 1; i <= n; i++) {
        resultado = resultado * i;
    }
    return resultado;
}

int main() {
    int n;
    printf("Digite um numero inteiro nao-negativo: ");
    scanf("%d", &n);

    if (n < 0) {
        printf("Erro: entrada invalida (n deve ser >= 0)\n");
        return 1;
    }

    printf("Fatorial de %d = %lld\n", n, fatorial_iterativo(n));
    return 0;
}
