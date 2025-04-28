#include <stdio.h>
#include <stdlib.h>

int main()
{
    float x;
    double y;
    printf("Input x: ");
    scanf("%f", &x);
    if (x<=-21)
    {
        printf("Number %f",x);
        printf(" is less than or equal to -21.\n");
        if (x<=-41)
        {
            y=(double)13*x*x/(double)11 - (double)6;
            printf("It is also less than or equal to -41! So... ");
            printf("Variable \"y\" = %f",y);
            printf("!");
        }
        else
        {
            printf("It is also greater than -41! ");
            printf("So... Variable \"y\" belongs to the empty cell!");
        }

    }
    else
    {
        printf("Number %f",x);
        printf(" is greater than -21.\n");
        if (x<=3)
        {
            y=(double)-14*x - (double)20;
            printf("It is also less than or equal to 3! So... ");
            printf("Variable \"y\" = %f",y);
            printf("!");
        }
        else
        {
            printf("It is also greater than 3");
            if (x>12)
            {
                y=(double)-14*x - (double)20;
                printf(" and greater than 12! So... ");
                printf("Variable \"y\" = %f",y);
                printf("!");
            }
            else
            {
                printf(", but less than or equal to 12! So... ");
                printf("Variable \"y\" belongs to the empty cell!");
            }
        }
    }
    return 0;
}
