
characters = {
    'A' : ['0xE0','0xDB','0xBB','0xDB','0xE0'],
    'B' : ['0xF9','0xC6','0xB6','0xB6','0x80'],
    'C' : ['0xDD','0xBE','0xBE','0xDD','0xE3'],
    'D' : ['0xE3','0xDD','0xBE','0xBE','0x80'],
    'E' : ['0xB6','0xB6','0xB6','0xB6','0x80'],
    'F' : ['0xBF','0xB7','0xB7','0xB7','0x80'],
    'G' : ['0xF3','0xB5','0xB6','0xBC','0xC3'],
    'H' : ['0x80','0xF7','0xF7','0xF7','0x80'],
    'I' : ['0xBE','0xBE','0x80','0xBE','0xBE'],
    'J' : ['0x81','0xFE','0xFE','0xFE','0xFD'],
    'K' : ['0xBE','0xDD','0xEB','0xF7','0x80'],
    'L' : ['0xFE','0xFE','0xFE','0xFE','0x80'],
    'M' : ['0x80','0xDF','0xEF','0xDF','0x80'],
    'N' : ['0x80','0xF9','0xE3','0xCF','0x80'],
    'O' : ['0xE3','0xDD','0xBE','0xDD','0xE3'],
    'P' : ['0xCF','0xB7','0xB7','0xB7','0x80'],
    'Q' : ['0xE2','0xDD','0xBA','0xDD','0xE3'],
    'R' : ['0xDE','0xAD','0xAB','0xB7','0x80'],
    'S' : ['0xD9','0xB6','0xB6','0xB6','0xCD'],
    'T' : ['0xBF','0xBF','0x80','0xBF','0xBF'],
    'U' : ['0x81','0xFE','0xFE','0xFE','0x81'],
    'V' : ['0x83','0xFD','0xFE','0xFD','0x83'],
    'W' : ['0x80','0xFD','0xFB','0xFD','0x80'],
    'X' : ['0xBE','0xDD','0xE3','0xDD','0xBE'],
    'Y' : ['0x8F','0xEF','0xE0','0xEF','0x8F'],
    'Z' : ['0x9E','0xAE','0xB6','0xBA','0xBC'],				    
    ' ' : ['0xFF','0xFF','0xFF','0xFF','0xFF'],
}

header = """\
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
"""

footer = """\
  Wire.endTransmission();

  while(1){
    digitalWrite(13, HIGH);   // set the LED on
    delay(1000);              // wait for a second
    digitalWrite(13, LOW);    // set the LED off
    delay(1000);              // wait for a second
  }
}
"""

class POV():
    
    def __init__(self, screens, filename='pov_sketch.pde'):
        self.address_counter = 0
        self.i2c_address = '0x50'
        
        self.sketch = open(filename, 'w')
        self.sketch.write(header)
        self.sketch.write('  Wire.beginTransmission(' + str(self.i2c_address) +  ');\n')
        self.sketch.write('  Wire.write(' + str(self.address_counter) + ');\n')
        self.sketch.write('  Wire.write(' + str(len(screens)) + ');\n')
        
        for screen in screens:
            self.write_screen(screen)
        
        self.sketch.write(footer)
        self.sketch.close()

    def increment_address(self):
        self.address_counter += 1
        if self.address_counter >= 256:
            self.i2c_address = '0x51'
    
    def check_page_break(self):
        if self.address_counter % 16 == 0:
            self.sketch.write('  Wire.endTransmission();\n')
            self.sketch.write('  delay(500);\n')
            self.sketch.write('  Wire.beginTransmission(' + str(self.i2c_address) + ');\n')
            self.sketch.write('  Wire.write(' + str(self.address_counter % 256) + ');\n')
    
    def write_screen(self, screen):
        self.sketch.write('  // ' + '#'*20  + screen + '#'*20  +  '\n')
        self.sketch.write('  Wire.write(' + str(len(screen)) + ');\n')
        self.increment_address()
        self.check_page_break()
        for letter in reversed(screen):
            self.sketch.write('  //' + '-'*10 + letter + '-'*10 +  '\n')
            for character in characters[letter.upper()]:
                self.sketch.write('  Wire.write(' + character + ');\n')
                self.increment_address()
                self.check_page_break()