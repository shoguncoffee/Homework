#include <stdio.h>
#include <stdlib.h>
int main() {
    int num;
    scanf("%d", &num);
    int n = num-1;
    for (int i=n;i>=-n;i--) {
        for (int k=-n;k<=n;k++) {
            char c = (k >= -abs(i) && k <= abs(i))? '*':' ';
            printf("%c ", c);
        }
        printf("\n");
    }
}
