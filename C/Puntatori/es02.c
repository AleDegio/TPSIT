/*
Alessia De Giovannini 
Esercizio 2
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  int n;
  int max;

  printf("Inserisci la dimesione del vettore? ");
  scanf("%d", &n);

  //vado ad allocare in memoria un vettore di int dalla dimesione n
  //bisogna fare un casting (int*) per fargli riconoscere il tipo
  int *vet=(int*)malloc(n*sizeof(int));
  printf("\n");

  for(int i=0; i<n; i++){
      printf("Inserisci il numero nella cella [%d]: ", i);
      scanf("%d", vet+i);
   }
   for(int i=0; i<n; i++){
     printf("%d \t", *(vet+i));
   }

   max=*vet;
   for(int k=1; k<n; k++){
       if(*(vet+k)>max){
         max=*(vet+k);
       }
   }

   printf("\nMassimo: %d" , max);
   return 0;
}
