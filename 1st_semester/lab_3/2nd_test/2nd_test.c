#include <stdio.h>
#include <stdlib.h>

int main(){
    double matrix[7][7] = { // створення матриці
        {34.56, -72.14, 18.23, -93.78, 56.12, -21.45, 77.89},
        {-65.43, 14.67, -89.56, 23.12, -41.78, 92.34, -8.91},
        {19.45, -58.67, 81.23, -17.56, 63.89, -32.12, 44.76},
        {78.91, -49.23, 27.89, -63.78, 90.34, -10.45, 52.78},
        {-35.67, 61.23, -88.91, 49.78, -24.56, 84.45, -11.32},
        {93.12, -37.89, 15.67, -69.34, 72.23, -50.89, 38.56},
        {-82.45, 47.12, -22.34, 85.78, -60.11, 13.67, -99.89}
    };
    int i = 0; //створення змінної для індексів
    int j = 0; //створення змінної для індексів
    // вивід початкової матриці
    printf("{\n");
    for (i = 0; i < 7; i++){
        printf("{");
        for (j = 0; j < 7; j++){
            if (j != 6){
                printf("%.2f\t", matrix[i][j]);
            }
            else {
                printf("%.2f", matrix[i][j]);
            }
        }
        printf("}");
        if (i != 6){
            printf("\n");
        }
        printf("\n");
    }
    printf("}\n");
    j = 0;
    while (j < 7){ //пошук першого від'ємного елемента побічної діагоналі
        if (matrix[6-j][j]<0){
            break;
        }
        j++;
    }
    double first_element = matrix[6-j][j]; //присвоєння змінній значення цього елемента
    printf("The first negative element of side diagonal is %.2f.\n", first_element); //вивід елемента
    i = 0;
    while (i < 7){ //пошук останнього додатнього елемента побічної діагоналі
        if (matrix[i][6-i]>0) {
            break;
        }
        i++;
    }
    double second_element = matrix[i][6-i]; //присвоєння змінній значення цього елемента
    printf("The last positive element of side diagonal is %.2f.\n", second_element); //вивід елемента
    // зміна елементів у матриці між собою
    matrix[6-j][j] = second_element;
    matrix[i][6-i] = first_element;
    // вивід зміненої матриці
    printf("{\n");
    for (i = 0; i < 7; i++){
        printf("{");
        for (j = 0; j < 7; j++){
            if (j != 6){
                printf("%.2f\t", matrix[i][j]);
            }
            else {
                printf("%.2f", matrix[i][j]);
            }
        }
        printf("}");
        if (i != 6){
            printf("\n");
        }
        printf("\n");
    }
    printf("}");
    return 0;
}
