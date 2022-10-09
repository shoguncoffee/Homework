#include <stdio.h>
#include <math.h>

int main() {
    int value;
    scanf("%d", &value);
    int p[2000] = {0}, now = 0;
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
    if (p[now-1] == value) 
        printf("that's prime number");
    else 
        printf("that is't prime number");
}
