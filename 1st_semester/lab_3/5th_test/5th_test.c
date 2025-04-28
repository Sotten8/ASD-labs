#include <stdio.h>
#include <stdlib.h>

int main(){
    double matrix[8][8] = { //створення матриці
        {88.45, -56.12, 72.34, -29.78, 41.56, -83.67, 64.12, -37.89},
        {-27.45, 92.78, -64.34, 55.67, -11.23, 79.12, 36.78, 18.34},
        {14.89, -48.56, 37.12, -82.45, 63.78, 95.12, 20.34, -49.67},
        {-19.34, 45.78, -72.89, 84.12, 60.23, 30.67, -77.45, 99.12},
        {76.12, -11.34, 53.89, 88.67, 22.45, -32.78, 90.34, -5.12},
        {-82.12, 19.78, 74.56, 41.23, -17.89, 89.34, -61.12, 34.45},
        {67.89, 93.45, 15.67, -24.12, 54.78, -42.23, 80.12, -39.67},
        {35.67, 62.34, -88.12, 49.78, -7.23, 33.89, -66.34, 91.56}
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
