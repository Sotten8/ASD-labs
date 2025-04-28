#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    double S = 0.0;
    double P = 1.0;
    int n;
    printf("Input n: ");
    scanf("%d",&n);
    if (n>=0){
        int i = 1;
        while (i<=n) {
            P *= (i+1)*sin(i);
            S+=P/(i*(i+1));
            i++;
        }
        printf("The sum is %.7f\n", S);
    }
    else {
        printf("Error...");
    }
    return 0;
}
