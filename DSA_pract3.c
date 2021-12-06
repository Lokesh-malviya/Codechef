#include<stdio.h>
#include <stdlib.h>
struct student{
    int* ptr;
    int actual;
    int total;
};
int arr2[10],*ptra;
void createarray(struct student*a,int actual,int total){
    a->ptr = (int*)malloc(a->total*sizeof(int));
}
void intialize(struct student*a){
    for (int i = 0; i < a->actual; i++)
    {
        scanf("%d",&(a->ptr)[i]);
    }
    
}
void show(struct student*a,int size){
    for (int i = 0; i < size; i++)
    {
        printf("value at %d is : %d\n",i,(a->ptr)[i]);
    }
    
}
void delete(struct student*a,int del){
    // delete any element
   for (int j = del; j < a->actual; j++) {
       if(j==del){
           a->ptr[j]=a->ptr[j+1];
           del = del + 1;
           
       }
       
   }
}
void insert(struct student*a,int element,int index){
     // insert any element
     int temp,S = a->ptr[index];
     a->ptr[index]=element;
   for (int j = index; j < a->actual; j++) {
       
       if(j>=index){
           temp = S;
           S = a->ptr[j+1];
           a->ptr[j+1] = temp;
       } 
   }
}
void maximum(struct student*a){
    int max = a->ptr[0];
    for (int i = 1; i < a->actual; i++)
    {
        if (max < a->ptr[i]){
            max = a->ptr[i];
        }
    }
    printf("maximum : \t%d\n",max);
    
}
void minimum(struct student*a){
    int max = a->ptr[0];
    for (int i = 1; i < a->actual; i++)
    {
        if (max > a->ptr[i]){
            max = a->ptr[i];
        }
    }
    printf("maximum : \t%d\n",max);
    
}
int linear(struct student*a,int search){
    int flag = 0,s=0;
    for (int i = 0; i < a->actual; i++)
        {
            if (a->ptr[i]==search){
                return s;
            }
            else{
                s = s+ 1;
            }
        
    }
    
}
int intersection(struct student*a,int* array,int size)
{
    int count=0;
    for (int i = 0; i < a->actual; i++)
    {
        for (int j = 0; j < size; j++)
        {
            if(a->ptr[i]==array[j]){
                arr2[j]=a->ptr[i];
                count = count + 1;
            }
        }
        
    }
    for (int l = 0; l <count; l++)
        {
            printf("%d ",arr2[l]);
        }
    
    
}
int sum(struct student*a)
{
    int sum1 = 0;
    for (int i = 0; i < a->actual; i++)
    {
        sum1 = sum1 + a->ptr[i];
    }
    return (sum1);
    
}
void reverse(struct student*a){
    ptra = (int*)calloc(a->actual,sizeof(int));
    int p = 0;
    for (int i = a->actual-1; i >=0; i--)
    {
        ptra[p]=a->ptr[i];
        p = p + 1;
    }
    
}
void reverse2(struct student*a){
    int temp;
    for (int i = 0; i < a->actual/2; i++)
    {
        temp = a->ptr[i];
        a->ptr[i]=a->ptr[a->actual-i-1];
        a->ptr[a->actual-i-1]=temp;
    }
    
}
void sort(struct student*a){
    int i,j = 0,temp;
    for ( i = 1; i < a->actual; i++)
    {
        for (int j = 0; j  < i ;j++)
        {
            if (a->ptr[j]>a->ptr[i]){
                temp = a->ptr[j];
                a->ptr[j]=a->ptr[i];
                a->ptr[i]= temp;
            }
        }
        
    }
    
}
int check(struct student*a,int* arr3){
    int count = 0;
    for (int i = 0; i < a->actual; i++)
    {
        if(a->ptr[i]==arr3[i]){
            count = count + 1;
        }
    }
    return count;
    
}
void main()
{
struct student marks;
int del,index,element,choose,search;
float f;
int array[10]={1,4,6},k,j,arr3[10];
printf("Enter the actual size of array : \t");
scanf("%d",&marks.actual);
printf("Enter the total size of array : \t");
scanf("%d",&marks.total);
createarray(&marks,marks.actual,marks.total);
intialize(&marks);

while(1){
        printf("enter the case you want :\t");
        scanf("%d",&choose); 
            
            switch (choose)
            {
                case 1:
                    printf("enter the element and index you want to insert  : \t");
                    scanf("%d%d",&element,&index);
                    insert(&marks,element,index);
                    show(&marks,marks.actual+1);
                    break;
                case 2:
                    printf("enter the element you want to insert  : \t");
                    scanf("%d",&element);
                    insert(&marks,element,marks.actual);
                    show(&marks,marks.actual+1);
                    break;
                case 3:
                    printf("enter the element you want to delete : \t");
                    scanf("%d",&del);
                    delete(&marks,del);
                    show(&marks,marks.actual-1);
                    break;
                case 4:
                    maximum(&marks);
                    break;
                case 5:
                    minimum(&marks);
                    break;  
                case 6:
                    printf("enter the element you want to search : \t");
                    scanf("%d",&search);
                    int j = linear(&marks,search);
                    printf("%d",j);
                    break;
                case 7:
                    k = intersection(&marks,array,10);
                    break;
                case 8:
                    k = sum(&marks);
                    printf("sum = : %d\n",k);
                    break;
                case 9:
                    k = sum(&marks);
                    f = k/marks.actual;
                    printf("%f \n",f);
                    break;
                case 10:
                    reverse(&marks);
                    for (int l = 0; l <marks.actual; l++)
                    {
                        printf("%d ",ptra[l]);
                    }
                    break;
                case 11:
                    reverse2(&marks);
                    show(&marks,marks.actual);
                    break;
                case 12:
                    sort(&marks);
                    printf("enter the element and index you want to insert  : \t");
                    scanf("%d%d",&element,&index);
                    insert(&marks,element,index);
                    show(&marks,marks.actual+1);
                    break;
                case 13:
                    for (int i = 0; i < marks.actual; i++)
                    {
                        arr3[i] = marks.ptr[i];
                    }
                    sort(&marks);
                    j = check(&marks,arr3);
                    if(j==marks.actual){
                        printf("YES\n");
                    }
                    else{
                        printf("NO\n");
                    }
                
                   

        }
    }
}
