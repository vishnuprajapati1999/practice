#include <stdio.h>
#include <stdlib.h>

int main () {
   int i, a,q,n,b,t,v,p=4;
   n = 1;

   /* Intializes random number generator */
   srand((unsigned) time(&t));

   /* Print 1 random numbers from range choosen by user */
   for( i = 0 ; i < n ; i++ ) { //for loop run till 1  number generated
     printf("Enter The Range In Which You Want To Play: ");
     scanf("%d",&b);
     v= rand() % b;//function for choose random number
     while(1){ // infinite while loop
    printf("1: Start Game\n");
    printf("2: End Game\n");
    printf("Enter Your Choice: ");
    scanf("%d",&q);
    switch (q) {
      case 1:
{
while (p>0)//run for only three times.
  {
        printf("\nEnter The Number: ");
        scanf("%d",&a);
if (b>a)
{
        if (a==v)

        {
          printf("Your Answer Is Correct\n");
          printf("You are lucky\n");
          exit(0);
        }
        else if (a<v)
  {
        printf("Your Guess Is Smaller Than Our Number");
          p--;
}
        else
        {
          printf("Your Guess Is Larger Than Our Number");
          p--;
    }
  }

 else
   printf("Out Of Range");
}
   case 2:
     exit(0);

    }

}
   }

   return(0);
}
}
