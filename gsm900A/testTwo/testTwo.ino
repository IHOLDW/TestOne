#include <SoftwareSerial.h>
SoftwareSerial mySerial(9, 10);

const int led = 8;
const int relay = 7;

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);

  pinMode(led, OUTPUT);
  pinMode(relay, OUTPUT);
}

void loop() {
  if(mySerial.available()) {
    String message = mySerial.readString();
    Serial.println(message);
    if(message.indexOf("ON") != -1) {
      digitalWrite(led, HIGH);
      digitalWrite(relay, HIGH);
      Serial.println("LED is ON");
    } 
    else if(message.indexOf("OFF") != -1) {
      digitalWrite(led, LOW);
      digitalWrite(relay, LOW);
      Serial.println("LED is OFF");
    }
  }
}
