#include <stdio.h>
void reversed_star_shape(int n);
void star_shape(int n)
{
    int i,j;
    for (i=1;i<=n;i++){
        for (j=1;j<=i;j++){
            printf("*");
        }
        printf("\n");
    }
    reversed_star_shape(n);
}

void reversed_star_shape(int n)
{
    int i,j;
    for (i=n;i>=1;i--){
        for(j=1;j<=i;j++){
        printf("*");
        }
        printf("\n");
    }
}

int main()
{
    int input,type_input;
    printf("Enter how many rows do you want:- ");
    scanf("%d",&input);
    printf("Enter 0 for regular star shap or 1 for reversed star shape:- ");
    scanf("%d",&type_input);
    switch (type_input)
    {
    case 0:
        star_shape(input);
        break;
    case 1:
        reversed_star_shape(input);
        break;
    default:
        break;
    }
}