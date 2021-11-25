#include<stdio.h>
long long int func(int *ptr){
    if (*ptr == 1){
        return 1;
    }
    else{
        int x = *ptr-1;
        return (*ptr)*(func(&x));
    }
    

}
void main()
{
int a = 1,arr[100];
char b = 'A';
for(a=1;a<=34;a++){
    int *ptr = &a;
    long long int d = func(ptr);
    arr[a]=d;
}
int lenght = 100;

arr1(int length,int *arr[]);


}