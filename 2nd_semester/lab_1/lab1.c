#include <stdio.h>

float recDescent(float x, unsigned int n, float Fi, float sum, int i) {
  if (i > n) {
    return sum - Fi;
  }
  Fi *= -i * (x - 1) / (i + 1);
  sum += Fi;
  return recDescent(x, n, Fi, sum, i + 1);
}

float recAscent(float x, unsigned int n, float Fi, int i) {
  float sum = -1;
  if (i > n) {
    sum = 0;
  }
  else {
    float element = -Fi * i * (x - 1 ) / (i + 1);
    sum = Fi + recAscent(x, n, element, i + 1);
  }
  return sum;
}

float recMixed(float x, unsigned int n, float Fi, int i) {
  if (i > n) {
    return 0;
  }
  float element = -Fi * i * (x - 1) / (i + 1);
  float sum = recMixed(x, n, element, i + 1);
  return Fi + sum;
}

float loopTesting (float x, unsigned int n, float Fi, float sum) {
  for (int i = 1; i <= n; i++) {
    Fi *= -i * (x - 1) / (i + 1);
    sum += Fi;
  }
  return sum - Fi;
}
int main() {
  float x;
  unsigned int n;
  printf("Choose the value of x: ");
  scanf("%f", &x);
  printf("Choose the value of n: ");
  scanf("%d", &n);
  if (x >= 2 || x <= 0 || n <= 0) {
    printf("You chose the incorrect input!");
    return 0;
  }
  float Fi = x - 1;
  printf("Descent recursion - the value of sum: %f\n", recDescent(x, n, Fi, x - 1, 1));
  printf("Ascent recursion - the value of sum: %f\n", recAscent(x, n, Fi, 1));
  printf("Mixed recursion - the value of sum: %f\n", recMixed(x, n, Fi, 1));
  printf("Loop testing - the value of sum: %f\n", loopTesting(x, n, Fi, x - 1));
  return 0;
}
