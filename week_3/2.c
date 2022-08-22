#include <stdio.h>
int main() {
    int num[2] = {0};
    for (int i=0;i<3;i++) {
      printf("(%d) Enter number: ", i+1);
      int x, y=0;
      scanf("%d", &x);
      for (int n=0;n<2;n++) if (num[y] > num[n]) y = n;
      if (x > num[y]) num[y] = x;
    }
  printf("%d + %d = %d", num[0], num[1], num[0] + num[1]);
}
