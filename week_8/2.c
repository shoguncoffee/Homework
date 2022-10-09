#include <stdio.h>

int main() {
    int v;
    scanf("%d", &v);
    for (int i = 2; i<v; i++) {
        if (v % i == 0) {
            printf("that is't prime number");
            return;
        }
    }
    printf("that's prime number");
}
