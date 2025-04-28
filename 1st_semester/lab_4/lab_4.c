#include <stdio.h>
#include <windows.h>

void hout_print(char sym) {
    printf("%c", sym);
    Sleep(15);
};
int main() {
    const int WIDTH;
    const int HEIGHT;
    char sym;
    printf("Enter the symbol of filling: ");
    scanf("%c",&sym);
    printf("Let\'s come up with the size of rectangle.\n");
    printf("The height has to be even.\n");
    printf("Enter them here:\n");
    printf("WIDTH: ");
    scanf("%d",&WIDTH);
    printf("HEIGHT: ");
    scanf("%d",&HEIGHT);
    if (HEIGHT%2 != 0) {
        printf("Height was entered in a wrong way.");
        return 0;
    };
    int step_horizontal = WIDTH - HEIGHT;
    int step_vertical = 0;
    COORD main_position = { 0, 0 };
    HANDLE hout = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD a;
    FillConsoleOutputAttribute(hout, 0, 5000, main_position, &a);
    COORD position = { step_horizontal + HEIGHT/2 - 1, HEIGHT/2 };
    SetConsoleCursorPosition(hout, position);
    hout_print(sym);
    while (step_horizontal < WIDTH && step_vertical < HEIGHT) {
        for (int a = 1; a <= step_horizontal; a++) {
            COORD start_left = {position.X - a, position.Y};
            SetConsoleCursorPosition(hout, start_left);
            hout_print(sym);
        };
        position.X = position.X - step_horizontal;
        for (int a = 1; a <= step_vertical; a++) {
            COORD start_up = {position.X, position.Y - a};
            SetConsoleCursorPosition(hout, start_up);
            hout_print(sym);
        };
        position.Y = position.Y - step_vertical - 1;
        for (int a = 0; a < (step_horizontal + 1); a++) {
            COORD start_right = {position.X + a, position.Y};
            SetConsoleCursorPosition(hout, start_right);
            hout_print(sym);
        };
        position.X = position.X + step_horizontal + 1;
        int difference = (HEIGHT - step_vertical != 2) ? 2 : 1;
        for (int a = 0; a <= (step_vertical + difference); a++) {
            COORD start_down = {position.X, position.Y + a};
            SetConsoleCursorPosition(hout, start_down);
            hout_print(sym);
        };
        position.Y = position.Y + step_vertical + difference;
        step_horizontal+=2;
        step_vertical+=2;
    };
    return 0;
};
