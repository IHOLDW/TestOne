// int sensor1 = A0;
int trigger = 7;

int val = 0;

void setup() {
  // pinMode(sensor1, INPUT);
  pinMode(trigger, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  val = analogRead(0);
  Serial.println(val);
  delay(300);

  if(val > 500){
    digitalWrite(trigger, HIGH);
  }
  else{
    digitalWrite(trigger, LOW);
  }

}
