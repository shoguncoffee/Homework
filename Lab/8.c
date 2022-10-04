#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <time.h>
#include <conio.h>
#include <pthread.h>
#include <string.h>

#define screen_x 80
#define screen_y 25
#define NS_PER_SECOND 1000000000
#define num_star 80
#define wHnd GetStdHandle(STD_OUTPUT_HANDLE)
#define rHnd GetStdHandle(STD_INPUT_HANDLE)

SMALL_RECT windowSize = { 0, 0, screen_x - 1, screen_y - 1 };
CHAR_INFO consoleBuffer[screen_x * screen_y];
char Aship[] = "<-0->", //len should be odd number
     Astar = '*';
int halfship = (strlen(Aship) - 1)/2;
struct object {
    int x, y, live, bg, fg;
};
struct object
    ship = { 32, 20, 10, 4, 2},
    star[num_star];

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
void *beeper(void *array) {
    int *arg = (int *)array;
    Beep(arg[0], arg[1]);
}
void fill(int x, int y, char c, int bg, int fg) {
    consoleBuffer[y*screen_x + x].Char.AsciiChar = c;
    consoleBuffer[y*screen_x + x].Attributes = bg * 16 + fg;
}
void clear_buffer() {
    for (int y=0; y<screen_y; y++)
        for (int x=0; x<screen_x; x++)
            fill(x, y, ' ', 0, 7);
}
void setting() {
    CONSOLE_CURSOR_INFO lpCursor = {.dwSize = 20, .bVisible = 0};
    SetConsoleWindowInfo(wHnd, 1, &windowSize);
    SetConsoleScreenBufferSize(wHnd, (COORD){ screen_x, screen_y });
    SetConsoleCursorInfo(wHnd, &lpCursor);
    SetConsoleMode(rHnd, ENABLE_EXTENDED_FLAGS | ENABLE_WINDOW_INPUT | ENABLE_MOUSE_INPUT);
    srand(time(NULL));
    clear_buffer();
}
int is_blank(int x, int y) {
    return consoleBuffer[y*screen_x + x].Char.AsciiChar == ' ';
}
void gotoxy(int x, int y) {
    SetConsoleCursorPosition(wHnd, (COORD){x, y});
}
void draw() {
    WriteConsoleOutputA(wHnd, consoleBuffer, (COORD){ screen_x, screen_y }, (COORD){0, 0}, &windowSize);
}
void end() {
    clear_buffer(); draw();
    gotoxy(36, 12); printf("Game Over");
    for (int i = 5; i > 0; i--) {
        gotoxy(40, 14); printf("%d", i);
        Sleep(1000);
    }
    exit(0);
}
int random(int min, int max) {
    return rand() % (max - min + 1) + min-1;
}
void fill_ship() {
    char *p = Aship;
    int start = ship.x - halfship;
    for (int i=0; *p != '\0'; p++, i++)
        fill(start + i, ship.y, *p, ship.bg, ship.fg);
}
void init_star() {
    int x, y;
    for (int i=0; i<num_star; i++)
        if (!star[i].live)
            while (1) {
                x = random(0, 79);
                y = random(0, 24);
                if (is_blank(x, y)) {
                    star[i].x = x;
                    star[i].y = y;                    
                    star[i].live = 1;
                    break;
                }
            }
}
void process(int* tick, int interval) {
    if (*tick == interval) *tick = 0;
    for (int i=0; i<num_star; i++) {
        if (star[i].live) {
            fill(star[i].x, star[i].y, '*', 0, 7);
            if (*tick == 0)
                if (++star[i].y == screen_y) 
                    star[i].live = 0;
            if (star[i].y == ship.y && star[i].x >= ship.x-halfship && star[i].x <= ship.x+halfship) {
                ship.live--;
                star[i].live = 0;
                int beep[2] = {700, 250};
                pthread_create(NULL, NULL, beeper, (void *)beep);
                Sleep(1);
                if (!ship.live) end();
            }
        }
    }
}
int controlling() {
    DWORD numEvents, numEventsRead;
    GetNumberOfConsoleInputEvents(rHnd, &numEvents);
    if (numEvents) {
        INPUT_RECORD* eventBuffer = new INPUT_RECORD[numEvents];
        ReadConsoleInput(rHnd, eventBuffer, numEvents, &numEventsRead);
        for (DWORD i = 0; i < numEventsRead; i++) {
            if (eventBuffer[i].EventType == MOUSE_EVENT) {
                if (eventBuffer[i].Event.MouseEvent.dwEventFlags & MOUSE_MOVED) {
                    int x = eventBuffer[i].Event.MouseEvent.dwMousePosition.X,
                        y = eventBuffer[i].Event.MouseEvent.dwMousePosition.Y;
                    if (x <= halfship) ship.x = halfship;
                    else if (x >= screen_x-halfship-1) ship.x = screen_x-halfship-1;
                    else ship.x = x;
                    if (y < 0) ship.y = 0;
                    else if (y > screen_y) ship.y = screen_y;
                    else ship.y = y;
                }
                else if (eventBuffer[i].Event.MouseEvent.dwButtonState & FROM_LEFT_1ST_BUTTON_PRESSED) {
                    ship.bg = random(0, 16);
                    ship.fg = random(0, 16);
                }
            }
            else if (eventBuffer[i].EventType == KEY_EVENT && eventBuffer[i].Event.KeyEvent.bKeyDown) {
                if (eventBuffer[i].Event.KeyEvent.wVirtualKeyCode == VK_ESCAPE)
                    end();
                else if (eventBuffer[i].Event.KeyEvent.uChar.AsciiChar == 'c') {
                    ship.bg = random(0, 16);
                    ship.fg = random(0, 16);
                }
            }
        }
        delete[] eventBuffer;
    }
}
int main() {
    setting();
    struct timespec start, finish, diff, delta, delay = {0, 10*1000*1000};
    for (int tick = 0;; tick++) {
        clock_gettime(CLOCK_REALTIME, &start);
        init_star();
        clear_buffer();
        fill_ship();
        controlling();
        process(&tick, 24);
        draw();
        clock_gettime(CLOCK_REALTIME, &finish);
        sub_timespec(start, finish, &diff);
        sub_timespec(diff, delay, &delta);
        if (delta.tv_nsec > 0) nanosleep(&delta, NULL);
    }
}
