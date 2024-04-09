const int led = 4;

void setup(){
  Serial.begin(115200);

  pinMode(led, OUTPUT);
}

void loop(){
  // digitalWrite(led, HIGH);
  if(Serial.available()) {
    String msg = Serial.readStringUntil('\n');
    Serial.println(msg);
    if(msg.indexOf("O") != -1) {
      // digitalWrite(led, HIGH);
      digitalWrite(led, HIGH);
      // Serial.println("Relay is ON");
    }else{
      digitalWrite(led, LOW);
    }
  }
}