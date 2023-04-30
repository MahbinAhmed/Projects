/*Have to write a program which can transfer units stated below. User will use the program until they quite.
Units to be converted:-
1.kms - miles
2.inches - foot
3. cms - inches
4. pound - kgs
5. inches - meters
*/

#include<stdio.h>
float kms_to_miles(float kms){
    float mile = 0.62137;
    return kms*mile;
}

float inches_to_foot(float inch){
    float foot = 0.0833;
    return inch*foot;
}

float cms_to_inches(float cms){
    float inch = 0.39370;
    return cms*inch;
    }

float pound_to_kgs(float pound){
    float kg = 0.45359;
    return pound*kg;
    }

float inches_to_meters(float inch){
    float meter = 0.0254;
    return inch*meter;
}
int main()
{
    int input,option;
    for (int i=0; i<1;)
    {
        printf("<<<<<------Welcome to unit converter------>>>>>\n\n");
        printf("1.kms to miles\n");
        printf("2. inches to foot\n");
        printf("3. cms to inches\n");
        printf("4. pound to kgs\n");
        printf("5. inches to meters\n");
        printf("0 to exit\n");
        printf("Select your desire option from the list:- \n");
        scanf("%d", &input);
        if (input==0){
            break;
        }
        else if(input==1){
            printf("Enter km value:- ");
            scanf("%d", &option);
            printf("\t%d km = %f mile\n\n", option, kms_to_miles(option));
        }
        else if(input==2){
            printf("Enter inch value:- ");
            scanf("%d", &option);
            printf("\t%d inch = %f foot\n\n", option, inches_to_foot(option));
        }
        else if(input==3){
            printf("Enter cms value:- ");
            scanf("%d", &option);
            printf("\t%d cms = %f inches\n\n", option, cms_to_inches(option));
        }
        else if(input==4){
            printf("Enter pound value:- ");
            scanf("%d", &option);
            printf("\t%d pound = %f kgs\n\n", option, pound_to_kgs(option));
        }
        else if(input==5){
            printf("Enter inch value:- ");
            scanf("%d", &option);
            printf("\t%d inch = %f meter\n\n", option, inches_to_meters(option));
        }
    }
}