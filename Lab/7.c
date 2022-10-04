#include <stdio.h>
#include <windows.h>
#include <time.h>
#include <conio.h>
#include <pthread.h>
#include <stdbool.h>
#define NS_PER_SECOND 1000000000

struct object {
    int x, y, tick, live;
};
struct object
    ship = { 32, 20, 0, 1 },
    bullet = { 0, 0, 0, 0 };

void setcursor() {
    CONSOLE_CURSOR_INFO lpCursor;
    lpCursor.bVisible = false; 
    lpCursor.dwSize = 20;
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &lpCursor);
}
void setcolor(int fg, int bg) {
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), bg * 16 + fg);
}
void gotoxy(int x, int y) {
    COORD c = { x, y };
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), c);
}
char check_cursor(int x, int y) {
    char buf[2];
    COORD c = { x, y };
    DWORD num_read;
    ReadConsoleOutputCharacter(GetStdHandle(STD_OUTPUT_HANDLE), (LPTSTR)buf, 1, c, (LPDWORD)&num_read);
    return buf[0];
}
void draw_ship() {
    gotoxy(ship.x, ship.y); setcolor(2, 4); 
    printf("<-0->");
}
void erase_ship() {
    gotoxy(ship.x, ship.y); setcolor(7, 0); 
    printf("     ");
}
void draw_bullet() {
    gotoxy(bullet.x, bullet.y); setcolor(7, 0); 
    printf("!");
}
void erase_bullet(int y) {
    gotoxy(bullet.x, y); setcolor(7, 0); 
    printf(" ");
}
void draw_score(int score) {
    int k = 0;
    for (int r = score/10; r != 0; k++)
        r /= 10;
    gotoxy(80 - k, 0); setcolor(7, 0);
    printf("%d", score);
}
void *beeper(void *array) {
    int *arg = (int *)array;
    Beep(arg[0], arg[1]);
}
int random(int min, int max) {
    return rand() % (max - min + 1) + min-1;
}
void draw_star() {
    setcolor(7, 0);
    int x, y;
    while (1) {
        x = random(10, 70);
        y = random(2, 5);
        if (check_cursor(x, y) == ' ') {
            gotoxy(x, y); printf("*");
            break;
        }
    }
}
void ship_move(int* turn, int interval) {
    if (*turn && ++ship.tick == interval) {
        ship.tick = 0;
        erase_ship();
        if (*turn > 0) {
            if (ship.x < 80 - 5) ship.x++;
            else *turn = 0;
        }
        else {
            if (ship.x > 0) ship.x--;
            else *turn = 0;
        } 
    }
    draw_ship();
}
void shoot() {
    if (!bullet.live) {
        int beep[2] = {660, 250};
        pthread_create(NULL, NULL, beeper, (void *)beep);
        Sleep(1);
        bullet.x = ship.x + 2;
        bullet.y = ship.y;
        bullet.live = 1;
    }
}
void bullet_move(int* score, int interval) {
    if (bullet.live && ++bullet.tick == interval) {
        bullet.tick = 0;
        if (--bullet.y >= 0) {
            if (check_cursor(bullet.x, bullet.y) == '*') {
                (*score)++;
                int beep[2] = {900, 250};
                pthread_create(NULL, NULL, beeper, (void *)beep);
                draw_star();
                erase_bullet(bullet.y);
                bullet.live = 0;
            }
            else draw_bullet();
        }
        else bullet.live = 0;
        erase_bullet(1 + bullet.y);
    }
}
void sub_timespec(struct timespec t1, struct timespec t2, struct timespec *td) {
    td->tv_nsec = t2.tv_nsec - t1.tv_nsec;
    td->tv_sec = t2.tv_sec - t1.tv_sec;
    if (td->tv_sec > 0 && td->tv_nsec < 0) {
        td->tv_nsec += NS_PER_SECOND;
        td->tv_sec--;
    }
    else if (td->tv_sec < 0 && td->tv_nsec > 0) {
        td->tv_nsec -= NS_PER_SECOND;
        td->tv_sec++;
    }
}
int main() {
    srand(time(NULL));
    setcursor();
     struct timespec start, finish, diff, delta, delay = {0, 9*1000*1000};
    int turn = 0, score = 0;
    char ch = ' '; 
    for (int i = 0; i < 20; i++) 
        draw_star();

    for (int tick=1; ch != 'x'; tick++) {
        clock_gettime(CLOCK_REALTIME, &start);
        if (_kbhit()) {
            ch = _getch();
            switch (ch) {
            case ' ': shoot();
                break;
            case 's': turn = 0;
                break;
            case 'a': turn = -1;
                break;
            case 'd': turn = 1;
            }
            fflush(stdin);
        }
        ship_move(&turn, 2);
        bullet_move(&score, 3);
        draw_score(score);
        if (tick == 10) {
            setcolor(7, 0);
            gotoxy(0, 0); printf("%.2f ms ", (float)diff.tv_nsec/1000000);
            gotoxy(0, 1); printf("%.2f ms ", (float)delta.tv_nsec/1000000);
            gotoxy(0, 2); printf("%.2f ms ", (float)(delta.tv_nsec + diff.tv_nsec)/1000000);
            tick = 0;
        }
        clock_gettime(CLOCK_REALTIME, &finish);
        sub_timespec(start, finish, &diff);
        sub_timespec(diff, delay, &delta);
        if (delta.tv_nsec > 0) nanosleep(&delta, NULL);
    }
}
