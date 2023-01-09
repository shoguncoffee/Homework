#include <stdio.h>

int main() {
    int n[4],
        q = 0;
    printf("Enter number(eg.'32 14 65 78'): ");
    scanf("%d %d %d %d", &n[0], &n[1], &n[2], &n[3]);
    for (int i=0;i<4;i++) {
        if (n[i]%2 == 0) q++;
    }
    printf("There're %d even numbers", q);
    return 0;
}
