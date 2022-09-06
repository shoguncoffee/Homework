#include <stdio.h>
#include <stdlib.h>
int main() {
    char a[128], b[128], c;
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
    while ((c = fgetc(f1)) != EOF)
        fprintf(f2, "%c", c);
    fclose(f1);
    fclose(f2);
}
