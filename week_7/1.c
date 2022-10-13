#include <stdio.h>

typedef struct {int line, point;}
    coor;
    
int n, nowmin = 100000;
coor start;

void map(int l[n][n]) {
    char test[] = 
    "\n-77 0 0 3 0\n"
    "2 3 S -1 0\n"
    "1 0 2 -4 4\n"
    "0 0 1 2 3\n"
    "0 9 2 3 0\n";
    
    int sign = 1, digit = 0, point = 0, num[5] = {0};
    char st = 0;
    
    for (int line=-1; line < n;) {
        char c = getchar();
        //char c = test[st++];
        if (c == ' ' || c == '\n' || c == '\r') {
            if (digit) {
                l[line][point] = 0;
                for (int i=0; i<digit; i++) {
                    for (int k=1; k<digit-i; k++) num[i] *= 10;
                    l[line][point] += num[i];
                    num[i] = 0;
                }
                //printf(" %d(%d %d)", l[line][point], line, point);
                point++;
                sign = 1;
                digit = 0;
            }
            if (c != ' ') {
                line++;
                point = 0;
            }
            //printf("%d ", c);
        }
        else if (c == 'S')
            start = (coor){.line = line, .point = point++};
        else if (c == '-') 
            sign = -1;
        else 
            num[digit++] = sign*(c-48);
    }
}
int forklist(int l[n][n], int *f, coor p) {        
    for (int i=0; i<3; i++) {
        int line = (p.line - 1) + i;

        if (line >= 0 && line < n) {
            for (int k=0; k<3; k++) {
                int point = (p.point - 1) + k;

                if (point >= 0 && point < n) {
                    f[i*3 + k] = l[line][point];
                }
            }
        }
    }
}
int sum_value(int l[n][n], coor *footprint, int index) {
    int s = 0;
    for (int i=0; i<=index; i++) {
        s += l[footprint[i].line][footprint[i].point];
        //printf("(%d, %d)(%d) ", footprint[i].line, footprint[i].point, l[footprint[i].line][footprint[i].point]);
    }
    /*
    if (s == -75) {
        int ss = 0;
        for (int i=0; i<=index; i++) {
            ss += l[footprint[i].line][footprint[i].point];
            printf("(%d, %d)(%d %d) ", footprint[i].line, footprint[i].point, l[footprint[i].line][footprint[i].point], ss);
        }    
    }
    */
    //printf(" %d\n", s);
    return s;
}
int is_overlap(coor *footprint, int index, coor now) {
    for(int i=0; i<=index; i++) {
        if (footprint[i].line == now.line && footprint[i].point == now.point) 
            return 1;
    }
    return 0;
}
int work(int l[n][n], coor *footprint, int index) {
    int f[9] = {0}, e = 1;
    forklist(l, f, footprint[index]);
    
    for (int i=0; i<9; i++) {
        coor now = {
            footprint[index].line + i/3 - 1, 
            footprint[index].point + i%3 -1
        };
        if (f[i] != 0 && is_overlap(footprint, index, now) == 0) {
            //printf("(%d %d) ", f[i], index);
            footprint[index+1] = now;
            work(l, footprint, index+1);
            e = 0;
            //break;
        }
    }
    if (e) {
        int s = sum_value(l, footprint, index);
        if (s < nowmin) nowmin = s;
    }
}
int main() {
    scanf("%d", &n);
    int l[n][n];
    map(l);
    
    coor footprint[n*n];
    footprint[0] = start;
    
    for (int i=0; i<n; i++)
        for (int k=0; k<n;k++) printf("", l[i][k]);
   
    work(l, footprint, 0);
    printf("%d", nowmin);
}
