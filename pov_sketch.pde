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
  Wire.write(0);
  Wire.write(3);
  // ####################tesing####################
  Wire.write(6);
  //----------g----------
  Wire.write(0xF3);
  Wire.write(0xB5);
  Wire.write(0xB6);
  Wire.write(0xBC);
  Wire.write(0xC3);
  //----------n----------
  Wire.write(0x80);
  Wire.write(0xF9);
  Wire.write(0xE3);
  Wire.write(0xCF);
  Wire.write(0x80);
  //----------i----------
  Wire.write(0xBE);
  Wire.write(0xBE);
  Wire.write(0x80);
  Wire.write(0xBE);
  Wire.write(0xBE);
  Wire.endTransmission();
  delay(500);
  Wire.beginTransmission(0x50);
  Wire.write(16);
  //----------s----------
  Wire.write(0xD9);
  Wire.write(0xB6);
  Wire.write(0xB6);
  Wire.write(0xB6);
  Wire.write(0xCD);
  //----------e----------
  Wire.write(0xB6);
  Wire.write(0xB6);
  Wire.write(0xB6);
  Wire.write(0xB6);
  Wire.write(0x80);
  //----------t----------
  Wire.write(0xBF);
  Wire.write(0xBF);
  Wire.write(0x80);
  Wire.write(0xBF);
  Wire.write(0xBF);
  // ####################asdf####################
  Wire.write(4);
  Wire.endTransmission();
  delay(500);
  Wire.beginTransmission(0x50);
  Wire.write(32);
  //----------f----------
  Wire.write(0xBF);
  Wire.write(0xB7);
  Wire.write(0xB7);
  Wire.write(0xB7);
  Wire.write(0x80);
  //----------d----------
  Wire.write(0xE3);
  Wire.write(0xDD);
  Wire.write(0xBE);
  Wire.write(0xBE);
  Wire.write(0x80);
  //----------s----------
  Wire.write(0xD9);
  Wire.write(0xB6);
  Wire.write(0xB6);
  Wire.write(0xB6);
  Wire.write(0xCD);
  //----------a----------
  Wire.write(0xE0);
  Wire.endTransmission();
  delay(500);
  Wire.beginTransmission(0x50);
  Wire.write(48);
  Wire.write(0xDB);
  Wire.write(0xBB);
  Wire.write(0xDB);
  Wire.write(0xE0);
  // ####################fasdfa####################
  Wire.write(6);
  //----------a----------
  Wire.write(0xE0);
  Wire.write(0xDB);
  Wire.write(0xBB);
  Wire.write(0xDB);
  Wire.write(0xE0);
  //----------f----------
  Wire.write(0xBF);
  Wire.write(0xB7);
  Wire.write(0xB7);
  Wire.write(0xB7);
  Wire.write(0x80);
  //----------d----------
  Wire.write(0xE3);
  Wire.endTransmission();
  delay(500);
  Wire.beginTransmission(0x50);
  Wire.write(64);
  Wire.write(0xDD);
  Wire.write(0xBE);
  Wire.write(0xBE);
  Wire.write(0x80);
  //----------s----------
  Wire.write(0xD9);
  Wire.write(0xB6);
  Wire.write(0xB6);
  Wire.write(0xB6);
  Wire.write(0xCD);
  //----------a----------
  Wire.write(0xE0);
  Wire.write(0xDB);
  Wire.write(0xBB);
  Wire.write(0xDB);
  Wire.write(0xE0);
  //----------f----------
  Wire.write(0xBF);
  Wire.write(0xB7);
  Wire.endTransmission();
  delay(500);
  Wire.beginTransmission(0x50);
  Wire.write(80);
  Wire.write(0xB7);
  Wire.write(0xB7);
  Wire.write(0x80);
  Wire.endTransmission();

  while(1){
    digitalWrite(13, HIGH);   // set the LED on
    delay(1000);              // wait for a second
    digitalWrite(13, LOW);    // set the LED off
    delay(1000);              // wait for a second
  }
}
