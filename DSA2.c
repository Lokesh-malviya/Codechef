#include<stdio.h>
#include <stdlib.h>
#include <string.h>
void delete(int*,int,int);
void insert(int*,int,int,int);
void search(int* arr,int,int);
void sort(int*,int);
int linear(int*,int,int);
int search12(int* arr,int,int,int);
void merge(int*,int*,int,int);
void main()
{
   int a,j,*arr,n,del,choose,ans;
   int element,index;
   int arr2[10] = {15,23,54,7,8,99,44,55,6,9};
   printf("Enter the number of Blocks you want :\t");
    scanf("%d",&n);
  arr = (int*)calloc(n,sizeof(int));
  for(int i = 0;i<n;i++)
    {
    scanf("%d",&arr[i]);
    }
    
    printf("enter the case you want :\t");
   scanf("%d",&choose); 
    
    switch (choose)
    {

        case 1:
                
                printf("Enter the Element and the index where you want to insert");
                scanf("%d%d",&element,&index);
                insert(arr,n,element,index);
                printf("answer : \t");
                for(int m = 0;m<=n;m++){
                       printf("%d ",arr[m]);
                    }
                break;
        case 2:
                printf("Enter the index of element you want to delete :\t");
                scanf("%d",&del);
                delete(arr,n,del);
                printf("answer : \t");
                for(int m = 0;m<n;m++){
                        printf("%d ",arr[m]);
                    }
                break;
        case 3:
                sort(arr,n);
                printf("maximum : %d ",arr[n-1]);
                 break;
                    
        case 4:
                sort(arr,n);
                printf("minimum : %d ",arr[0]);
        case 5:
                printf("Enter the index of element you want to delete :\t");
                scanf("%d",&del);
                delete(arr,n,del);
                printf("Enter the numer you want to search:\t");
                scanf("%d",&a);
                ans = linear(arr,n,a);
                if(ans!=0){
                    printf("Your number is at : %d position ",ans);
                }
                else if (ans==0)
                {
                    printf("the numer is not present in arry");
                }
                
                break;
        case 6: 
                printf("Enter the element you want to search :\t");
                scanf("%d",&a);
                int ret = search12(arr,0,n,a);
                if (ret==0){
                    printf("no");
                }
                else{
                     printf("Yes it is present");
                }
                break;
        case 7:
                
                merge(arr,arr2,n,10);
                for(int m = 0;m<n+10;m++){
                        printf("%d ",arr[m]);
                    }
                break;
        case 8:
                sort(arr,n);
                for(int m = 0;m<n;m++){
                        printf("%d ",arr[m]);
                    }
                break;
        

    }
   
}
void delete(int* arr,int n,int del ){
    // delete any element
   for (int j = 0; j < n; j++) {
       if(j==del){
           arr[j]=arr[j+1];
           del = del + 1;
       }
       arr[n-1] = 999;
   }
}
void insert(int* arr,int n,int element,int index){
     // insert any element
     int temp,S = arr[index];
     arr[index]=element;
   for (int j = 0; j < n; j++) {
       
       if(j>=index){
           temp = S;
           S = arr[j+1];
           arr[j+1] = temp;
       } 
   }
}
void sort(int* arr,int n){
    int i,j = 0,temp;
    for ( i = 1; i < n; i++)
    {
        for (int j = 0; j  < i ;j++)
        {
            if (arr[j]>arr[i]){
                temp = arr[j];
                arr[j]=arr[i];
                arr[i]= temp;
            }
        }
        
    }
    
}
int linear(int* arr,int len,int search){
    int flag = 0,s=0;
    for (int i = 0; i < len; i++)
    {
        if(i!=999){
            if (arr[i]==search){
                return s;
            }
            else{
                s = s+ 1;
            }
        }
        else{
            return(0);
        }
        
    }
    
}
int search12(int* arr,int start,int len,int search1){
    int mid;
    mid = (start + len)/2;
    if (arr[mid]==search1){
        return(1);
    }
    else if(search1<arr[mid])
    {
        return search12(arr,0,mid-1,search1);
    }
    else if(search1>arr[mid])
    {
        return search12(arr,mid+1,len,search1);
    }
    else{
        return (0);
    }
    
}
void merge(int* arr,int* arr2,int n,int m){
    int cou = n+m;
    arr = (int*)realloc(arr,cou*sizeof(int));
    int j =0;
    for (int i = 0; i < m+n; i++)
    {
        if(i>=n){
            arr[i] = arr2[j];
            j = j +1;
        }
    }
    
}
