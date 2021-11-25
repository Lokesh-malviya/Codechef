#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int i,j,n,arr[100],temp;
    scanf("%d",&n);
    for(i = 0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for(j=0;j<n;j++){
        for(int k = j+1;k<n;k++){
            if(arr[j]>arr[k]){
                temp = arr[j];
                arr[j]=arr[k];
                arr[k]=temp;
            }
        }
    }
    for (int l = 0; l < n; l++)
    {
        printf("%d ",arr[l]);
    }
    
    
    return 0;
}