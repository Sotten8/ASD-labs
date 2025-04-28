#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    double S = 0.0;
    double P = 1.0;
    int n;
    int ct = 0;
    int sin_ct = 0;
    int operations = 0;
    printf("Input n: ");
    scanf("%d",&n);
    if (n>=0){
        int i = 1;
        while (i<=n){
            int j = 1;
            while (j<=i) {
                P *= (j+1)*sin(j);
                j++;
                ct += 6;
                sin_ct++;
            }
            S+=P/(i*(i+1));
            i++;
            ct += 8;
        }
        operations = ct + sin_ct + 3;
        printf("Operations = %d",operations);
    }
    else {
        printf("Error...\n");
    }
    return 0;
}
