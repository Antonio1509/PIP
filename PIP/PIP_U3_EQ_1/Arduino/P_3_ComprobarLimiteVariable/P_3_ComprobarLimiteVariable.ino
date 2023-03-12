//UART
byte contador; //max = 255

void setup() {
  contador = 0;
  Serial.begin(9600); //baudios

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(contador++);
  delay(1000); //ms
}
