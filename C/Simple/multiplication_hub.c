#include <stdio.h>

void mul_table(int n){
    for(int i = 1; i<=10;i++){
        printf("%d * %d = %d\n",n,i,n*i);
    }
}

int main(){
    printf("<<<<<---Welcome to Multiplication Hub--->>>>>\n\n");
    int input;
    while (1)
    {
        printf("\n\nEnter number to print multiplication table or enter 0 to quit:- \n");
        scanf("%d", &input);
        fflush(stdin);
        if (input==0){
            break;
        }
        else{
            mul_table(input);
        }
    }
    printf("Program runned successfully!");
    return 0;
}