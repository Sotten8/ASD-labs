#include <stdio.h>
#include <stdlib.h>
#define SIZE 10
#define LENGTH 8

void print_array(int matrix[SIZE][LENGTH]){
    for (int row = 0; row < SIZE; row++) {
        for (int column = 0; column < LENGTH; column++) {
            printf("%d\t", matrix[row][column]);
        }
        printf("\n");
    }
    printf("\n-----------------------------------------------------------------\n\n");
}

int main()
{
    int row;
    int column;

    int index;
    int additional_index;
    int another_index;

    int element;

    int matrix[SIZE][LENGTH] = {
        { -99,  95,  -10,  50,  -16,   32,   14,  -25 },
        { -56,  81,  -15,  50,  -21,   19,   18,  38 },
        { -23,  63,  -36,  50,   10,   -5,   30,   0 },
        {   0,  42,  -44,  50,   23,   14,   42, -11 },
        {  11,  29,  -58,  50,   23,   -7,   52,   5 },
        {  32,  10,  -78,  50,  -39,   40,   58,  -11 },
        {  70,   5,  -83,  50,   35,   -2,   69,  15 },
        {  87,   4,  -90,  50,  -10,   25,   75,  -8 },
        {  97,   3,  -95,  50,   10,   25,   82,  1 },
        {  98,   3,  -98,  50,  -6,    25,   93,  2 }
    };

    print_array(matrix);

    for (column = 0; column < LENGTH; column++) {
        for (index = 1; index < SIZE; index++) {
            element = matrix[index][column];
            additional_index = 0;
            while (matrix[additional_index][column] < element) {
                additional_index++;
            }
            for (another_index = index - 1; another_index >= additional_index; another_index--) {
                matrix[another_index + 1][column] = matrix[another_index][column];
            }
            matrix[additional_index][column] = element;
        }
    }

    print_array(matrix);

    return 0;
}
