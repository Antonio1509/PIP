//los potenciometros son dispositivos analogicos de entrada, por que tienes mas de dos estados
//en el caso de arduino, se cuentan con algunos pines analogicos para estos actuadores
//los pines analogicos se representan  por la letra a y un numero...
//ejemplo A0

int potenciometro = ;

void setup() {

  Serial.begin(9600); //baudios
  Serial.setTimeout(10);
}

int v;
void loop() {

  v = analogRead(potenciometro);
  //un actuador analogico en arduino nos puede proporcionar 1024 valores... que van del 0 al 1023
  // esto debido a que arduino cuenta con un adc de 10 bits de resolucion, asi mismo arduino trabaja en el adc con 5 volts
  //esto significa que 1023 = 5v y 0 = 0v
  //aproximadamente, se tiene un cambio de valor cada 4.8mv

  Serial.println(v)
  delay(1000);

  //el potenciometro tiene 3 patitas, de las cuales la de enmedio debe conectarse al A0 y uno de los extremos a 5v, mientras 
  //que el otro extremo a GND

}
