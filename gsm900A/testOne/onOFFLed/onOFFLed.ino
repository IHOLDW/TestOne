#include <SoftwareSerial.h>
SoftwareSerial mySerial(9, 10);

int led = 7;

void setup() {
  mySerial.begin(9600);
  Serial.begin(9600);
  pinMode(led, OUTPUT);

  mySerial.write("AT");
  delay(500);
  mySerial.write("ATE0");
  delay(500);
  mySerial.write("AT+CMGF=1");
  delay(500);

}

uint8_t a[80] = {'\0'}, d, i, *bufferOne, bufferTwo;

void loop() {
  while(mySerial.available() > 0){
    a[d] = mySerial.read();
    d++;
  }

  if(d > 0){
    for(int i= 0 ; i < 80; i++){
      Serial.print(a[i]);
    }
    Serial.println();

    for(int i = 0; i < 80; i++){
      a[i] = '\0';
    }

    d = 0;
  }
}
