/*
Alessia De Giovannini
Esercizio 1
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  int n;
  int i;

  printf("quanti numeri vuoi? ");
  scanf("%d", &n);

  //vado ad allocare in memoria un vettore di float dalla dimesione n
  //bisogna fare un casting (float*) per fargli riconoscere il tipo
  float *vet=(float*)malloc(n*sizeof(float));
  printf("\n");

  for(i=0; i<n; i++){
      printf("Inserisci il numero nella cella [%d]: ", i);
      scanf("%f", vet+i);
   }

   for(i=0; i<n; i++) {
     printf("%f \t", *(vet+i));
   }
  return 0;
}
