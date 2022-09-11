#define a 10
#define b 11
#define c 12

void setup() {
}

void loop() {
  int l[6][3] = {{a,b,c},{b,c,a},{a,c,b},{c,a,b},{c,b,a},{b,a,c}};
  for (int i=0;i<6;i++) {
    pinMode(l[i][0], OUTPUT);
    digitalWrite(l[i][0], HIGH);
    pinMode(l[i][1], OUTPUT);
    digitalWrite(l[i][1], LOW);
    pinMode(l[i][2], INPUT);
    delay(500);
  }
}
