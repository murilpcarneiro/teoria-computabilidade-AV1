/*
 * PROGRAMA RECURSIVO – Fatorial
 * Disciplina: Teoria da Computabilidade
 *
 * Estilo recursivo: a função se chama diretamente,
 * com condição-base de parada explícita (n == 0).
 *
 * Função computada: f(n) = n!  para n >= 0
 *   Base:      f(0) = 1
 *   Recursão:  f(n) = n * f(n-1)
 */

#include <stdio.h>

long long fatorial_recursivo(int n) {
    /* Condição-base: parada da recursão */
    if (n == 0) return 1;

    /* Chamada recursiva */
    return n * fatorial_recursivo(n - 1);
}

int main() {
    int n;
    printf("Digite um numero inteiro nao-negativo: ");
    scanf("%d", &n);

    if (n < 0) {
        printf("Erro: entrada invalida (n deve ser >= 0)\n");
        return 1;
    }

    printf("Fatorial de %d = %lld\n", n, fatorial_recursivo(n));
    return 0;
}
