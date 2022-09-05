#include <stdio.h>
int main() {
    FILE *f;
    f = fopen("/Users/shogun/Desktop/ttest.txt", "w");
    printf("Input data string:");
    while (1) {
        char c[512];
        scanf("%s", c);
        fprintf(f, "\n%s", c);
        if (c[0] == '.' && c[1] == '\0') break;
    }
    fclose(f);
}
