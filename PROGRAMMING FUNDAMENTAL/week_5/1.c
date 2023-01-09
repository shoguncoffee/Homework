#include <stdio.h>
int main() {
    FILE *f;
    f = fopen("/Users/shogun/Desktop/ttest.txt", "w");
    printf("Input data string:\n");
    for (char c; c!='.'; fprintf(f, "%c", c))
        c = getchar();
    fclose(f);
}
