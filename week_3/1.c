#include <stdio.h>
int main() {
    int q,w,e,z,x,c;
    printf("Enter 1 number: ");
    scanf("%d", &q);
    printf("Enter 2 number: ");
    scanf("%d", &w);
    printf("Enter 3 number: ");
    scanf("%d", &e);
    z = q+e;
    x = q+w;
    c = w+e;
    if (z>x && z>c) printf("%d + %d = %d", q, e, z);
    else if (x>z && x>c) printf("%d + %d = %d", q, w, x);
    else printf("%d + %d = %d", w, e, c);
}
