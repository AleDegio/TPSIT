/*
Alessia De Giovannini
malloc
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  int n;
  int i;

  printf("quanti numeri vuoi? ");
  scanf("%d", &n);

  int *vet=(int*)malloc(n*sizeof(int));
  printf("\n");
  for(i=0; i<n; i++){
      printf("Inserisci il numero nella cella [%d]: ", i);
      scanf("%d", &vet+i);
   }
 }
