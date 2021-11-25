#include<stdio.h>

int main(){
    int a = 34;
    int * ptra = &a;

    char c = 'A';
    char * ptrc = &c;

// //For integer datatype
    printf("Value of A is %d\n", a);
    printf("Address of A is %d\n", &a);
    printf("Address of A is %u\n", &a);
    printf("Address of A is %u\n", ptra);
    printf("Address of A is %p\n", &a);
    printf("Value of A is %u\n", *ptra);

    printf("Address of c is %d\n", ptra);
    printf("Incremented Address of c is %d\n", ptra + 1);

//For char datatype
    printf("Value of c is %c\n", c);
    printf("Address of c is %d\n", &c);
    printf("Address of c is %u\n", &c);
    printf("Address of c is %p\n", &c);
    printf("Address of c is %d\n", ptrc);
    printf("Incremented Address of c is %d\n", ptrc +1);

}