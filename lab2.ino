int right = 3, center = 4, left = 2,
    green = 12, red = 10, yellow = 11,
    delay_time = 150, interval = 50;
unsigned long time_r = 0, time_l = 0, time_c = 0, 
              time_redOn = 0, time_greenOn = 0;
              
void setup() {
    pinMode(left, INPUT);
    pinMode(center, INPUT);
    pinMode(right, INPUT_PULLUP);
    pinMode(red, OUTPUT);
    pinMode(yellow, OUTPUT);
    pinMode(green, OUTPUT);
    attachInterrupt(digitalPinToInterrupt(left), when_press_left, RISING);
    attachInterrupt(digitalPinToInterrupt(right), when_press_right, FALLING);
}
void when_press_right() {
    if (millis()-time_r > delay_time) {
        if (digitalRead(red) == LOW) {
            digitalWrite(green, !digitalRead(green));
            time_greenOn = millis();
        }
    }
    time_r = millis();
}
void when_press_left() {
    if (millis()-time_l > delay_time) {
        digitalWrite(red, !digitalRead(red));
        time_redOn = millis();
    }
    time_l = millis();
}
void sleep(int pin, int ms) {
    unsigned long t = millis();
    while (millis()-t < ms && digitalRead(pin) == HIGH) delay(interval);
    digitalWrite(pin, LOW);
}
void loop() {    
    if (digitalRead(red) == HIGH && digitalRead(green) == LOW)
        sleep(red, 3000 - (millis() - time_redOn));
    else {
        if (digitalRead(green) == HIGH) {
            sleep(green, 3000 - (millis() - time_greenOn));
        }
        else if (digitalRead(center) == LOW && millis()-time_c > delay_time) {
            for (int i=0;i<4;i++) {
                digitalWrite(yellow, !digitalRead(yellow));
                unsigned long t = millis();
                while (millis()-t < 500) delay(interval);
            }
            time_c = millis();
        }
    }
}
