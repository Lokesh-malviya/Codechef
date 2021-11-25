#include<stdio.h>
#include <string.h>
//--------------------> swaping a number using call by value <----------------------
/*void swap(int,int);
void main()
{
    int a,b;
    a = 10;
    b = 20;
    //swaping a number using call by value
    printf("Diffrence Between A,B Before swaping is : \t%d\n",a-b);
    swap(a,b);
}
void swap(int x,int y){
    int temp;
    temp = x;
    x = y;
    y = temp;
    printf("Diffrence Between A,B after swaping is : \t%d\n",x-y);
}*/


//-----------------> swaping a number using call by reference <-----------------------
/*
void swap(int*,int*);
void main()
{
 int a,b;
    a = 10;
    b = 20;
    //swaping a number using call by value
    printf("Diffrence Between A,B Before swaping is : \t%d\n",a-b);
    swap(&a,&b);
    
}
void swap(int* a,int* b){
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
    printf("Diffrence Between A,B after swaping is : \t%d\n",a-b);
}*/


//------------------><--------------------------------------------------------------


// Write a program to return multiple values through c program by following ways
    // a. by pointers
    // b. by structures
    // c. by arrays
/*void reassign(int*,int*);
void main()
{
 int a,b;
    a = 10;
    b = 20;
    int *ptr1,*ptr2;
    ptr1 = &a;
    ptr2 = &b;
    //swaping a number using call by value
    printf("A,B Before : \t%d %d\n",a,b);
    reassign(ptr1,ptr2);
    printf("A,B after  : \t%d %d\n",*ptr1,*ptr2);
    
}
void reassign(int* a,int* b){
    *a = 50;
    *b = 42;
}*/


// b. Reversing the arry with call by reference and retuening multiple values
/*void reassign(int*,int);
void main()
{
 int a,b,arr[100]={1,2,3,4,5},arr1;
    a = 5;
    reassign(arr,a);
    printf("After reversing the Array : \t");
    for (int i = 0; i < a; i++)
    {
        printf("%d ",arr[i]);
    }
    
}
void reassign(int* arr,int a){
    int b = a;
    for(int i = 0;i<a;i++){
            arr[i] = b;
            b = b-1;
    }
    
}*/

// Structure Pointers

/*
struct Student
{
    char name[50];
    int roll;
};

void main()
{
    struct Student *ptra, S1;
    ptra = &S1;
    strcpy(S1.name,"Ramesh");
    S1.roll = 47;
    printf("Name of the student is : %s\n",&ptra->name);
    printf("Roll of the student is : %d",(*ptra).roll);
}
*/


//--------------------------><----------------------------------------------


//3. 1. Write a c program to perform search operation in given array using
  //a. Linear Search
  //b. Binary Search
/*
void search(int* arr,int,int);

void main()
{
   int a,j,arr[10]={1,6,5,4,8,7,9,4,7,2};
   printf("Enter the element you want to search :\t");
   scanf("%d",&a);
   j = 10;
   search(arr,10,a);
}
void search(int* arr,int len,int search){
    int flag = 0,s;
    for (int i = 0; i < len; i++)
    {
        if (arr[i]==search){
            flag = 1;
        }
        else{
            flag=0;
        }
        if(flag==1){
                printf("your search elemnt is present at : %d\n",i);
        }
        
    }
    
}*/



