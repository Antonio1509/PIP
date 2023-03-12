//UART
int led = 13;

void setup() {

  pinMode(led, OUTPUT);
  
  Serial.begin(9600); //baudios
  Serial.setTimeout(10);
}

String op;
void loop() {

  if(Serial.available()>0){
    op = Serial.readString();
    digitalWrite(led, HIGH);
  }
  delay(1000);

  

}
