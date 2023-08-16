#include <stdio.h>


int buscaLinear(int vetor[], int tamanho, int chave){	
	int i=0;
	while ((i <= tamanho) && (vetor[i] != chave)){
		i++;
	}
	if( (i<=tamanho) && (vetor[i] == chave) ){
		return i;
	}
	else
		return -1;
}


int busca_binaria(int vetor[], int tamanho, int chave) {
    int inicio = 0;
    int fim = tamanho - 1;
    int meio;

    while (inicio <= fim) {
        meio = (inicio + fim) / 2;

        if (vetor[meio] == chave) {
            return meio;
        }

        if (vetor[meio] < chave) {
            inicio = meio + 1;
        } else {
            fim = meio - 1;
        }
    }

    return -1;
}

int main() {
    int vetor[] = {1, 3, 5, 6, 9, 12, 15, 20, 25};
    int teste = sizeof(vetor);
    int teste2=sizeof(vetor[0]);
    int tamanho = sizeof(vetor) / sizeof(vetor[0]);
    int chave = 1;
    
    printf("\nVar. teste com SIZEOF(vetor) = %d",teste);
    printf("\nVar. teste com SIZEOF(vetor[0]) = %d",teste2);
	printf("\nVar. tamanho = %d",tamanho);

	printf("\n\n BUSCA BINARIA" );
    int resultado = busca_binaria(vetor, tamanho, chave);

    if (resultado == -1) {
        printf("\n Elemento não encontrado.\n");
    } else {
        printf("\n Elemento encontrado na posição %d.\n", resultado);
    }

	printf("\n\n BUSCA LINEAR" );
	chave = 5;
	int res=busca_binaria(vetor, tamanho, chave);
	
	if (res == -1) {
        printf("\n Elemento não encontrado.\n");
    } else {
        printf("\n Elemento encontrado na posição %d.\n", res);
    }

    return 0;
}
