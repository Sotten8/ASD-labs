#include <stdio.h>
#include <stdlib.h>
#define LENGTH 10
#define SIZE 8

void print_array(double matrix[SIZE][LENGTH]){
    for (int row = 0; row < SIZE; row++) {
        for (int column = 0; column < LENGTH; column++) {
            printf("%.1lf\t", matrix[row][column]);
        }
        printf("\n");
    }
    printf("\n-----------------------------------------------------------------\n\n");
}

void binary_search(double matrix[SIZE][LENGTH], int left_border, int right_border, int index, int min, int max, int position) {
    int check = 0;
    char *text = (position) ? "last row" : "first column";
    while (left_border <= right_border) {
        int center = (right_border + left_border) / 2;
        double element = (position) ? matrix[index][center] : matrix[center][index];
        if (element < min) {
            right_border = center - 1;
        }
        else if (element > max) {
            left_border = center + 1;
        }
        else {
            printf("The wanted element in the %s is %.1lf.", text, element);
            printf(" It is on index: %d.\n", center);
            check = 1;
            break;
        }
    }
    if (!check) {
        printf("There is no such element in the %s.\n", text);
    }
};
int main()
{
    double matrix[SIZE][LENGTH] = {
        {5.0, 3.1, -5.2, 2.3, 4.7, 0.9, 3.8, 15.4, 15.4, -1.6},
        {4.5, 1.2, 0.4, -10.5, 3.2, 1.8, 4.6, 10.9, 8.9, 7.1},
        {4.2, 0.5, -20.7, 3.3, 1.9, -5.4, 2.8, 5.3, 6.6, 1,7},
        {4.2, 2.8, 0.2, -15.6, 4.5, 1.0, 0.7, 4.2, 9.2, 0.1},
        {4.1, 3.7, 4.4, 0.1, 0.5, 2.6, -2.3, 3.9, 1.0, 17.5},
        {3.3, -10.9, -5.7, -20.4, 1.3, 0.3, 3.9, 1.2, 3.4, -5.6},
        {3.3, 4.3, 1.5, 0.7, 3.0, 4.2, -5.9, -3.7, 2.1, -7.2},
        {3.3, 3.2, 3.1, 3.0, 3.0, 2.1, 2.0, 2.0, 1.0, 0.9}
    };

    print_array(matrix);

    int min = 0;
    int max = 5;

    int L = 0;
    int R = LENGTH - 1;
    int row = SIZE - 1;
    int position = 1;

    binary_search(matrix, L, R, row, min, max, position);

    L = 0;
    R = SIZE - 1;
    int column = 0;
    position = 0;

    binary_search(matrix, L, R, column, min, max, position);

    return 0;
}
