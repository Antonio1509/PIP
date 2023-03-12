//UART

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //baudios

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("Esto es Mensaje");
}
