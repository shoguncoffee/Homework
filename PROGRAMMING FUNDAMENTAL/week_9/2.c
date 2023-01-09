#include <stdio.h>

int isprime(int value) {
    for (int i = 2; i<value; i++)
        if (value % i == 0) return 0;
    return 1;
}

int main() {
    int v;
    while (1) {
        scanf("%d", &v);
        if (isprime(v)) break;
    }
    printf("that's prime number");
}
