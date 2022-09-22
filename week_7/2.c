#include <stdio.h>
int main() {
    int n, start, i=0;
    scanf("%d", &n);
    int sq = n*n, l[sq];
    int sign=1, digit=0, num[5] = {0};
    for (int line=0; line <= n;) {
        char c = getchar();
        switch (c) {
            case '\n':
            case '\r': line++;
            case ' ': 
                if (digit) {
                    for (int j=0; j<digit; j++) {
                        for (int k=1; k<digit-j; k++) 
                            num[j] *= 10;
                        l[i] += num[j];
                        num[j] = 0;
                    }
                    i++;
                    sign = 1;
                    digit = 0;
                }
                break;
            case 'S': start = i++;
                break;
            case '-': sign = -1;
                break;
            default:
                num[digit++] = sign*(c-48);
        }
    }
    int min_index, min, first, sum=0;
    while (1) {
        l[start] = 0;
        first = 1;
        for (int index=0; index<sq; index++) {
            if (index/n >= start/n-1 && index/n <= start/n+1 && index%n >= start%n-1 && index%n <= start%n+1) {
                int val = l[index];
                if (val != 0 && (first || val < min)) {
                    min = val;
                    min_index = index;
                    first = 0;
                }
            }
        }
        if (first) break;
        start = min_index;
        sum += min;
    }
    printf("%d", sum);
}
