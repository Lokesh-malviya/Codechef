#include<stdio.h>
#include<stdlib.h>
int top = -1;
int maximum = 5;
int *ptr;
int push(int);
void show();
void pop();
void main(){
int choice,n;

ptr = (int*)calloc(maximum,sizeof(int));

while(1){
    printf("Enter the choice : \t");
    scanf("%d",&choice);
            switch(choice){
                        case 1:
                                        if(top!=maximum-1)
                                        {
                                            printf("Enter the element you want to store : \t");
                                            scanf("%d",&n);
                                            
                                            int j = push(n);
                                            if (j==-1){
                                                break;
                                            }
                                            else if(j==1){
                                                continue;
                                            }
                                            
                                        }
                                        else{
                                            printf("**************Array Over flow*************\n");
                                            break;
                                        }
                        case 2:
                                 show();
                                 break;
                        case 3:
                                pop();
                                break;
                        }
                        
                        
                        
                    }
}
int push(int n){
    
    if(top==maximum-1){
        printf("Over flow\n");
        return(-1);
    }
    else{
        top = top +1;
        ptr[top]=n;
        return(1);
        
    }
}
void show(){
    for (int i = 0; i <= top; i++) {
        printf("%d ",ptr[i]);
    }
    printf("\n");
}

void pop(){
    if(top== -1){
        printf("Array empty");
    }
    else{
        printf("%d ",top);
        ptr[top]=0;
        top = top - 1;
    }
}
