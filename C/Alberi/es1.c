/*
Alessia De Giovannini
Esercizio 1
riampire e stampare l'albero
cercare x nell'albero
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct tree_node{
  struct tree_node *left;
  struct tree_node* right;
  int key;
  int val;
}tree_node;

//inserimento
void insert(struct tree_node **tree, struct tree_node *new){
  if (*tree == NULL) {
    *tree = new;
    (*tree)->left = NULL;
    (*tree)->right = NULL;
  }else{
    if (new->key < (*tree)->key) {
      insert(&(*tree)->left, new);
    }else if (new->key > (*tree)->key) {
      insert(&(*tree)->right, new);
    }else{
      printf("Chiave duplicata\n");
    }
  }
}

//ricerca
struct tree_node * find_by_key(struct tree_node *tree, int key){
  if (tree == NULL) {
    return NULL;
  }else{
    if (key < tree->key) {
      return find_by_key(tree->left, key);
    }else if (key > tree->key) {
      return find_by_key(tree->right, key);
    }else{
      return tree;
    }
  }
}

//vista
void in_order_view(struct tree_node *tree){
  if (tree != NULL) {
    in_order_view(tree->left);
    printf("Key %d, value %d\n", tree->key, tree->val);
    in_order_view(tree->right);
  }
}

int main(int argc, char const *argv[]) {
  struct tree_node* tree=NULL;
  struct tree_node* new;
  struct tree_node* tree2;
  int chiave;
  int valore;

  //tree=(struct tree_node*) malloc(sizeof(struct tree_node));
  do{
    new=(struct tree_node*) malloc(sizeof(struct tree_node));
    //chi=(struct tree_node*) malloc(sizeof(struct tree_node));
    printf("Inserisci un elemento dell'albero o -1 per terminare: ");
    scanf("%d", &valore);
    if (valore>=0) {
      printf("Inserisci la chiave dell'elemento dell'albero: ");
      scanf("%d", &chiave);
      new->val=valore;
      new->key=chiave;
      insert(&tree, new);   //aggiunge l'elemento all'albero
    }
  }while(valore>0);

  printf("Stampa albero: \n");
  in_order_view(tree);
  printf("\n");
  printf("Inserisci la chiave da cercare: ");
  scanf("%d", &chiave);
  tree2 = find_by_key(tree, chiave);
  printf("Valore: %d", tree2->val); 
  return 0;
}
