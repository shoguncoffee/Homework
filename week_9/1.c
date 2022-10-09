#include <stdio.h>
#include <math.h>

int isprime(int value) {
    int est = (int)pow(value, (float)4/5) + 5;
    int p[est], now = 0;
    for (int i = 0; i<est; i++) 
        p[i] = 0;
    for (int n = 2; n <= value; n++) {
        for (int x = 0; x <= now; x++) {
            if (p[x] == 0) {
                p[now] = n;
                now++;
                break;
            }
            else if (n % p[x] == 0) 
                break;
        }
    }
    return p[now-1] == value;
}

int main() {
    int v;
    while (1) {
        scanf("%d", &v);
        if (isprime(v)) break;
    }
    printf("that's prime number");
}
