#include <stdio.h>
#include <stdlib.h>
int main() {
    char a[128], b[128], c[999999], ch;
    FILE *f1, *f2;
    printf("Input: ");
    scanf("%s", a);
    printf("Output: ");
    scanf("%s", b);
    f1 = fopen(a, "r");
    if (f1 == NULL) {
        printf("Can't open file");
        return 1;
    }
    f2 = fopen(b, "w");
    for (int i=0; (ch=fgetc(f1)) != EOF; i++)
        c[i] = ch;
    printf("%s", c);
    fprintf(f2, "%s", c);
    fclose(f1);
    fclose(f2);
}
