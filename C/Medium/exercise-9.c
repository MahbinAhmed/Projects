// Rock, Paper, Scissor game
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>

// Function for computers choice
int rand_num(){
    srand(time(NULL));
    int val = rand()%3;
    return val;
}

// Function for printing result after each round
void printer(int result,int pp,int cp, char pn){
    if(result=='D'){
        printf("Match drawn!\n");
    }
    else if(result=='W'){
        printf("You won this round!\n");
    }
    else{
        printf("You loose this round!\n");
    }
    printf("%s's score:- %d\n",pn,pp);
    printf("Player 2 score:- %d\n\n",cp);
}

int main(){
    char user_name[30];
    int user_point = 0;
    int computer_point = 0;
    int rounds;

    printf("<<<<<-----Welcome to \"Rock, Paper, Scissor\" Hub----->>>>>\n");
    printf("Please enter your name [Within 30 letters]:- ");
    scanf("%s",&user_name);
    getchar();

    // This while loop will take input for the round numbers. This input can only handle positive number and decimal numbers. If the input is in negative it will crash!
    while (1)
    {
        printf("How many rounds you want to play this game?[3-999] :- ");
        scanf("%d",&rounds);
        getchar();
        if(rounds<3 || rounds>999){
            printf("Please enter a number between 3 and 999!\n");
            continue;
        }
        else{
            break;
        }
    }
    
    // The game will be started from this loop.
    for(int i=0;i<rounds;i++){
        char user_inp;
        char result;
        printf("Round %d\n\n", i+1);
        printf("Enter 'r' for Rock, 'p' for Paper and 's' for Scissor :- \n");
        scanf("%c", &user_inp);
        getchar();
        
        int pc_choice = rand_num(); //Taking random number from rand_num function as computers choice
        // 0 - Rock
        // 1 - Paper
        // 2 - Scissor
        if(pc_choice==0){
            if (user_inp=='r'){
                result = 'D';
                user_point = user_point+0;
                computer_point = computer_point+0;
                printer(result,user_point,computer_point,user_name);
            }
            else if (user_inp=='p'){
                result = 'W';
                user_point = user_point+1;
                computer_point = computer_point+0;
                printer(result,user_point,computer_point,user_name);
            }
            else if (user_inp=='s'){
                result = 'L';
                user_point = user_point+0;
                computer_point = computer_point+1;
                printer(result,user_point,computer_point,user_name);
            }
            else{
                printf("Please enter a valid input!\n");
                i = i-1;
            }
        }
        else if(pc_choice==1){
            if (user_inp=='p'){
                result = 'D';
                user_point = user_point+0;
                computer_point = computer_point+0;
                printer(result,user_point,computer_point,user_name);
            }
            else if (user_inp=='s'){
                result = 'W';
                user_point = user_point+1;
                computer_point = computer_point+0;
                printer(result,user_point,computer_point,user_name);
            }
            else if (user_inp=='r'){
                result = 'L';
                user_point = user_point+0;
                computer_point = computer_point+1;
                printer(result,user_point,computer_point,user_name);
            }
            else{
                printf("Please enter a valid input!\n");
                i = i-1;
            }
        }
        else if(pc_choice==2){
            if (user_inp=='s'){
                result = 'D';
                user_point = user_point+0;
                computer_point = computer_point+0;
                printer(result,user_point,computer_point,user_name);
            }
            else if (user_inp=='r'){
                result = 'W';
                user_point = user_point+1;
                computer_point = computer_point+0;
                printer(result,user_point,computer_point,user_name);
            }
            else if (user_inp=='p'){
                result = 'L';
                user_point = user_point+0;
                computer_point = computer_point+1;
                printer(result,user_point,computer_point,user_name);
            }
            else{
                printf("Please enter a valid input!\n");
                i = i-1;
            }
        }
    }
    // Showing results
    printf("-----All rounds have finished-----\n\n");
    if(user_point>computer_point){
        printf("Congratulations!!! You've won the game!\n");
        printf("Your score:- %d\n",user_point);
        printf("Player 2 score:- %d\n",computer_point);
    }
    else if(user_point<computer_point){
        printf("Sorry! You've lost the game! Better luck next time\n");
        printf("Your score:- %d\n",user_point);
        printf("Player 2 score:- %d\n",computer_point);
    }
    else if(user_point==computer_point){
        printf("Match drawn!\n");
        printf("Your score:- %d\n",user_point);
        printf("Player 2 score:- %d\n",computer_point);
    }
}