//This sketch was created using writePOV.m to fill the I2C EEPROM on the POV fan
//LED on Pin 13 blinks once data transfer is complete
//
//Connections required:
//	Fan			Arduino
//	DATA  <--->	Analog Pin 4
//	CLK   <--->	Analog Pin 5
//	Vcc   <--->	3.3V
//	GND   <--->	GND


#include <Wire.h>

void setup()
{
  Wire.begin();        // join i2c bus (address optional for master)
  pinMode(13, OUTPUT);    
}

void loop()
{ 
Wire.beginTransmission(0x50);
Wire.send(0);
Wire.send(2);
  while(1){
    digitalWrite(13, HIGH);   // set the LED on
    delay(1000);              // wait for a second
    digitalWrite(13, LOW);    // set the LED off
    delay(1000);              // wait for a second
  }
}
