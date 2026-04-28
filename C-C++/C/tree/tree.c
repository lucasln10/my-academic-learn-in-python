#include <stdio.h>
#include <stdlib.h>


struct no {
    int no;
    struct no *dir, *esq;
};

int list[5] = { 15, 25, 84, 75, 95 };

int main()
{
    int temp = 0;
    int tamanho = sizeof(list) / sizeof(int);
    for (int i = 0; i < tamanho; i++){
        if (temp != 0){
            if (temp > list[i]){
                no.esq = list[i];
            }else{
                no.dir = list[i];
            }
        }else{
            temp = list[i];
            no.no = temp;
        }
    }
    return 0;
}
