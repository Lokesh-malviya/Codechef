#include <stdio.h>
 
void main()
{
    
    struct details
    {
        char name[20];
        int price;
       
    };
    struct details item[50];
    int n, i;
    FILE *of;
    n=10
    fflush(stdin);
    for (i = 0; i < n; i++)
    {
        fflush(stdin);
        printf("Item name: \n");
        scanf("%s", item[i].name);
        fflush(stdin);
        printf("item price: \n");
        scanf("%d",  &item[i].price);
        fflush(stdin);

    }
}
    for (int j = 0; j < 10; i++)
    {
        fwrite (&item[j], sizeof(struct details), 1, of);
         printf("             *****  INVENTORY ***** \n");
    printf("------------------------------------------------------------------\n");
    printf("S.N.|    NAME           | PRICE  \n");
    printf("------------------------------------------------------------------\n");
    for (i = 0; i < n; i++)
        printf("%d     %-15s        %-d         %d \n", i + 1, item[i].name,item[i].price);
    printf("------------------------------------------------------------------\n");
    }
    

   
}

