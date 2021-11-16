#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int convertDecimalToOctal(char DN[], int *n, int *m);
int main()
{
  char decimalNumber[30];
  int a=0, b=0;

  printf("Enter a decimal number: ");
  scanf("%s",decimalNumber);
  //puts(decimalNumber);
  /*convertDecimalToOctal(decimalNumber, &a, &b);*/
 // printf("%s in decimal = %d.%d in octal", decimalNumber, a, b);
 int count=0,j=0;
 char num1[5];
 while (decimalNumber[j]!="."){
     count = count + 1;
     j = j+1;
 }
 printf("%d",count);
  for (int i = 0; i<=count; i++)
  {
      num1[i] = decimalNumber[i];
  }
  
printf("%c",num1[0]);
  return 0;
}

