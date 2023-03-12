//UART
int led = 13;

void setup() {

  pinMode(led, OUTPUT);
  
  Serial.begin(9600); //baudios
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to tun repeatedly:
  digitalWrite(led, HIGH);
  delay(1000);

  digitalWrite(led, LOW);
  delay(1000);

}
