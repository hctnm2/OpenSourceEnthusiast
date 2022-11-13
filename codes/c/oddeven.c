#include <stdio.h>

char* odd_even(int i);

int main()
{
   int number;

   printf("Enter an integer : ");
   scanf("%d", &number);

   printf("Result : %s",odd_even(number));
   return 0;
}

char* odd_even(int number)
{
  if (number%2 == 0){
      return "YOUR NUMBER IS EVEN NUMBER";
   }else{
      return "YOUR NUMBER IS ODD NUMBER";
   }
}
