#include <stdio.h>
#include <stdlib.h>
int main() {
    int num;
    scanf("%d", &num);
    int l = 4*num-2;
    for (int i=1;i<2*num;i++) {
        char c[l];
        for (int n=0;n<l;n++) c[n] = ' ';
        int x = 2*abs(i-num)+1,
            nu = num-1;
        for (int n=0;n<x;n++) {
            c[2*(nu - abs(i-1-nu)+n)] = '*';
        }
        c[l] = '\0';
        printf("%s\n", c);
    }
}
