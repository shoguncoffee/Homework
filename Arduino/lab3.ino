int bitNum[10] = {B1110111, B0010001, B1101011, B0111011, B0011101, B0111110, B1111110, B0010011, B1111111, B0111111},
    bitG = B1110110, bitL = B1100100,
    left = 3, right = 2,
    maxdelay = 70,
    now_num = 0;
long rand_num = random(1, 10);
bool is_show_num = 1;
unsigned long timeb1 = 0, timeb2 = 0;

void bitsdisplay(int bits) {
    for (int i=0; i<7; i++)
        digitalWrite(i+4, !bitRead(bits, i));
}
void setup () {
    pinMode(left, INPUT_PULLUP);
    pinMode(right, INPUT_PULLUP);
    for (int i=4; i<=10; i++) {
        pinMode(i, OUTPUT);
        digitalWrite(i, HIGH);
    }
    attachInterrupt(digitalPinToInterrupt(right), right_res, FALLING);
    attachInterrupt(digitalPinToInterrupt(left), left_res, FALLING);
}
void right_res() {
    if (millis()-timeb1 > maxdelay) {
        now_num = (now_num < 9)? now_num+1 : 1;
        bitsdisplay(bitNum[now_num]);
        is_show_num = 1;
    }
    timeb1 = millis();
}
void left_res() {
    if (millis()-timeb2 > maxdelay) {
        if (is_show_num == 1) {
            if (now_num > rand_num) 
                bitsdisplay(bitG);
            else if (now_num < rand_num) 
                bitsdisplay(bitL);
            else {
                bitsdisplay(bitNum[0]);
                rand_num = random(1, 10);
            }
            is_show_num = 0;
        }
        else {
            bitsdisplay(bitNum[now_num]);
            is_show_num = 1;
        }
    }
    timeb2 = millis();
}
void loop() {
    if (digitalRead(right) == LOW) timeb1 = millis();
    if (digitalRead(left) == LOW) timeb2 = millis();
 }
