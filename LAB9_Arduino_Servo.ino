

//  Robin Lutwick 
//  Advanced Embedded II
//  Lab 9 Arduino Code
#include <Servo.h>
Servo ser1,ser2;  //these are my two servos which will be connected to pins 11 & 10 on the arduino

int pos;
//int pos2 = 0;

void setup(){
  
 Serial.begin(9600);
 ser1.attach(11);  // attaches the servo on pin 11
 ser2.attach(10);  // attaches the servo on pin 10
 
}

void loop(){
  String data; //declaration q        

 if(Serial.available()>0){
  
   data = Serial.readStringUntil('\n'); //read my string data up until a new line char

   if (data == "M1"){ //ifdata is Motor 1 then read the data until end, convert string to integer and then tell my servo where to go
     
     data = Serial.readStringUntil('\n');
     pos = data.toInt(); 
     ser1.write(pos);   //writing the int angle value to the servo motor
   
   }


   if (data == "M2"){
     
     data = Serial.readStringUntil('\n');
     pos = data.toInt();
     ser2.write(pos);

   }
   
   Serial.flush(); //this will clear the serial buffer
   delay(20); //wait for the system to change
 
 }
}

//this is what you gave us in the lab period
//#include <Servo.h>
//Servo RCservo1;
//
//void setup() {
//  // put your setup code here, to run once:
//  
//  Serial.begin(9600);
//  RCservo.attach(10); 
//  
//}
//
//void loop() {
//  // put your main code here, to run repeatedly:
//  if(Serial.avaliable()>0)){
//    dato = Serial.parseInt();
//    RCservo1.write(dato);
//    delay(1000);
//    
//  }
//  
//}
