void setup(){
  Serial.begin(115200);
  pinMode(3, INPUT);
}

void loop(){
  int val = digitalRead(3);

  if(val == 1){
    Serial.println("O");
  }else{
    Serial.println("F");
  }
}