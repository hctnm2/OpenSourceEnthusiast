#include <stdlib.h>
#include <stdio.h>

int main() {
    //Making a rock paper scissor game
    printf("Welcome to the game rock paper scissors");
    
    //creating infinite loop
    while(1) {
         char userinput; 
         char compchoiceoption[3] = {'r','p','s'};

         //Taking userinput
        printf("\n What's your choice? ");
        scanf(" %c", &userinput);

        //for quiting the game
        if (userinput == 'q') {
            printf("Thank you for playing");
            exit(1);
        }

        //validating userinput
        if (userinput != 'r' && userinput != 'p' && userinput != 's') {
            printf("\n The input is wrong.");
            exit(1);
        }

        //generating random numbers
        int randomnum;
        randomnum = rand() % 3;
       
        //Computer giving a choice
        char compchoice = compchoiceoption[randomnum];

        //printing userinput and computer input
        printf("computer input is %c \n user input is %c",compchoice, userinput);

        //comparing choices-draw
        if(compchoice == userinput) {
            printf("\n draw, play again");
        }

        //comparing choices- user wins
        if(userinput == 'r' && compchoice == 's' || userinput == 's' && compchoice=='p' || userinput == 'p' && compchoice == 'r') {
            printf("\n You win");
        } else {
            printf("\n You lose, play again");
        }
    }
return 0;
}
