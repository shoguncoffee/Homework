#include <stdio.h>

int main() {
    int q = 4;
    for (int i=0;i<4;i++) {
        int x;
        printf("Enter %d number: ", i+1);
        scanf("%d", &x);
        if (x%2) q--;
    }
    printf("There're %d even numbers", q);
    return 0;
}
