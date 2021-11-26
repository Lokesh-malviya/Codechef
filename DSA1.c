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

/*<------------------------------ DSA2------------------------------>
#include<stdio.h>
#include<stdlib.h>
/*void main(){
int *ptr;
int n;
printf("Enter the number of Blocks you want");
scanf("%d",&n);
ptr = (int*)malloc(n*sizeof(int));
for(int i = 0;i<n;i++){
    scanf("%d",&ptr[i]);
}
for(int j = 0;j<n;j++){
    printf("Value at position %d is : %d\n",j,ptr[j]);
}
}*/

// calloc use : ptr = (cast-type*)calloc(n, element-size);


/*void main(){
int *ptr;
int n;
printf("Enter the number of Blocks you want");
scanf("%d",&n);
ptr = (int*)calloc(n,sizeof(int));
for(int i = 0;i<n;i++){
    scanf("%d",&ptr[i]);
}
for(int j = 0;j<n;j++){
    printf("Value at position %d is : %d\n",j,ptr[j]);
}
}*/

// Realloc use ptr = realloc(ptr, newSize);


/*void main(){
int *ptr;
int n;
printf("Enter the number of Blocks you want");
scanf("%d",&n);
ptr = (int*)calloc(n,sizeof(int));
for(int i = 0;i<n;i++){
    scanf("%d",&ptr[i]);
}
for(int j = 0;j<n;j++){
    printf("Value at position %d is : %d\n",j,ptr[j]);
}
ptr = realloc(ptr,4*sizeof(int));
for(int l = 0;l<4;l++){
    scanf("%d",&ptr[l]);
}
for(int m = 0;m<4;m++){
    printf("Value at position %d is : %d\n",m,ptr[m]);
}
*/
 <-------------------------DELETING A ARRAY---------------------------->
     
     
     
 void search(int* arr,int,int);
void sort(int*,int,int)
void main()
{
   int a,j,*arr,n,del,choose;
   printf("Enter the number of Blocks you want :\t");
    scanf("%d",&n);
  arr = (int*)calloc(n,sizeof(int));
  for(int i = 0;i<n;i++)
    {
    scanf("%d",&arr[i]);
    }
    // delete any element
   printf("Enter the index of element you want to delete :\t");
   scanf("%d",&del);
   for (int j = 0; j < n; j++) {
       if(j==del){
           arr[j]=arr[j+1];
           del = del + 1;
       }
       arr[n-1] = 999;
   }
   for(int m = 0;m<n;m++){
    printf("Value at position %d is : %d\n",m,arr[m]);
    }
    
    printf("Enter the element you want to searc :\t");
   scanf("%d",&choose); 
    
    switch (choose)
    {
        case 1:
                printf("Enter the element you want to search :\t");
                scanf("%d",&a); 
                j = 10;
                search(arr,n,a);
                break;
        case 2:
                printf("maximum element is :\t");
                sort(arr,n)
                break;
    }
   
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
    
}




