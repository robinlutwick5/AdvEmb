#include<Servo.h>

Servo RCservo;

int potpin=0;
int val;
int pos;

void setup(){
  RCservo.attach(9);  //our servo motor is connected to pin 9
  pinMode(potpin, INPUT);
  Serial.begin(9600);
}

void loop(){
  
  val=analogRead(potpin);

  pos = val*180./1023;

  RCservo.write(pos);
  Serial.println(pos);
  
  delay(20);
}
