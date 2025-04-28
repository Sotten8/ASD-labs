#include <stdio.h>
#include <stdlib.h>

int main(){
    double matrix[8][8] = { // створення матриці
        {23.56, -54.32, 12.78, -8.41, 44.67, -78.89, 19.45, -65.23},
        {98.12, -33.67, 14.89, -57.22, 89.34, -14.45, -67.89, 11.43},
        {-72.45, 35.78, -49.34, 76.23, -9.87, -53.11, -61.73, 21.56},
        {66.43, -28.94, 85.13, -64.21, 37.45, -47.67, 91.25, -89.56},
        {54.98, -73.11, 33.56, 9.84, -88.67, 71.43, -92.21, 23.14},
        {-31.67, 92.43, 18.56, 88.12, -57.31, 43.65, -69.78, 62.34},
        {49.23, 91.76, 10.34, -75.43, 83.12, -35.43, 77.89, -23.56},
        {64.89, 18.23, -99.34, 29.67, -48.78, 58.12, -27.45, 73.11}
    };
    int i = 0; //створення змінної для індексів
    int j = 0; //створення змінної для індексів
    // вивід початкової матриці
    printf("{\n");
    for (i = 0; i < 8; i++){
        printf("{");
        for (j = 0; j < 8; j++){
            if (j != 7){
                printf("%.2f\t", matrix[i][j]);
            }
            else {
                printf("%.2f", matrix[i][j]);
            }
        }
        printf("}");
        if (i != 7){
            printf("\n");
        }
        printf("\n");
    }
    printf("}\n");
    j = 0;
    while (j<8){ //пошук першого від'ємного елемента побічної діагоналі
        if (matrix[7-j][j]<0){
            break;
        }
        j++;
    }
    double first_element = matrix[7-j][j]; //присвоєння змінній значення цього елемента
    printf("The first negative element of side diagonal is %.2f.\n", first_element); //вивід елемента
    i = 0;
    while (i<8){ //пошук останнього додатнього елемента побічної діагоналі
        if (matrix[i][7-i]>0) {
            break;
        }
        i++;
    }
    double second_element = matrix[i][7-i]; //присвоєння змінній значення цього елемента
    printf("The last positive element of side diagonal is %.2f.\n", second_element); //вивід елемента
    // зміна елементів у матриці між собою
    matrix[7-j][j] = second_element;
    matrix[i][7-i] = first_element;
    // вивід зміненої матриці
    printf("{\n");
    for (i = 0; i < 8; i++){
        printf("{");
        for (j = 0; j < 8; j++){
            if (j != 7){
                printf("%.2f\t", matrix[i][j]);
            }
            else {
                printf("%.2f", matrix[i][j]);
            }
        }
        printf("}");
        if (i != 7){
            printf("\n");
        }
        printf("\n");
    }
    printf("}");
    return 0;
}
