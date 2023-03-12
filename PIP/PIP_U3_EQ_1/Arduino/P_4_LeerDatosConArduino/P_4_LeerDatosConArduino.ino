//UART

void setup() {
  Serial.begin(9600); //baudios
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to tun repeatedly:

  //available retorna cuantos bytes existen en el buffer de entrada
  if (Serial.available()>0){
  
  // Arduino intentara leer todos los bytes que se lean posible hasta que se llegue el limite (timeout)
  //por defect, el timeout del arduino es de 1 segundo
  cadena = Serial.readString();

  Serial.println(cadena);

  }

}
