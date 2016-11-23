from __future__ import print_function
import os

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
	'0' : ['0xC1','0xAE','0xB6','0xBA','0xC1'],
	'1' : ['0xFF','0xFE','0x80','0xDE','0xFF'],
	'2' : ['0xCE','0xB6','0xBA','0xBC','0xDE'],
	'3' : ['0xB9','0x96','0xAE','0xBE','0xBD'],
	'4' : ['0xFB','0x80','0xDB','0xEB','0xF3'],
	'5' : ['0xB1','0xAE','0xAE','0xAE','0x8D'],
	'6' : ['0xF9','0xB6','0xB6','0xD6','0xE1'],
	'7' : ['0x9F','0xAF','0xB7','0xB8','0xBF'],
	'8' : ['0xC9','0xB6','0xB6','0xB6','0xC9'],
	'9' : ['0xC3','0xB5','0xB6','0xB6','0xCF'],
	'a' : ['0xF0','0xEA','0xEA','0xEA','0xFD'],
	'b' : ['0xF1','0xEE','0xEE','0xF6','0x80'],
	'c' : ['0xFD','0xEE','0xEE','0xEE','0xF1'],
	'd' : ['0x80','0xF6','0xEE','0xEE','0xF1'],
	'e' : ['0xF3','0xEA','0xEA','0xEA','0xF1'],
	'f' : ['0xDF','0xBF','0xB7','0xC0','0xF7'],
	'g' : ['0xC1','0xDA','0xDA','0xDA','0xE7'],
	'h' : ['0xF0','0xEF','0xEF','0xF7','0x80'],
	'i' : ['0xFF','0xFE','0xA0','0xEE','0xFF'],
	'j' : ['0xFF','0xA1','0xFE','0xFE','0xFD'],
	'k' : ['0xFF','0xEE','0xF5','0xFB','0x80'],
	'l' : ['0xFF','0xFE','0x80','0xBE','0xFF'],
	'm' : ['0xF0','0xEF','0xF3','0xEF','0xE0'],
	'n' : ['0xF0','0xEF','0xEF','0xF7','0xE0'],
	'o' : ['0xF1','0xEE','0xEE','0xEE','0xF1'],
	'p' : ['0xF7','0xEB','0xEB','0xEB','0xE0'],
	'q' : ['0xE0','0xF3','0xEB','0xEB','0xF7'],
	'r' : ['0xF7','0xEF','0xEF','0xF7','0xE0'],
	's' : ['0xFD','0xEA','0xEA','0xEA','0xF6'],
	't' : ['0xFD','0xFE','0xEE','0x81','0xEF'],
	'u' : ['0xE0','0xFD','0xFE','0xFE','0xE1'],
	'v' : ['0xE3','0xFD','0xFE','0xFD','0xE3'],
	'w' : ['0xE1','0xFE','0xF9','0xFE','0xE1'],
	'x' : ['0xEE','0xF5','0xFB','0xF5','0xEE'],
	'y' : ['0xE1','0xFA','0xFA','0xFA','0xE7'],
	'z' : ['0xEE','0xE6','0xEA','0xEC','0xEE'],
	':' : ['0xFF','0xFF','0xC9','0xC9','0xFF'],
	'!' : ['0xFF','0xFF','0x86','0xFF','0xFF'],
	',' : ['0xFF','0xFF','0xF9','0xFA','0xFF'],
	'-' : ['0xFF','0xF7','0xF7','0xF7','0xFF'],
	' ' : ['0xFF','0xFF','0xFF','0xFF','0xFF'],	# Space
	'*' : ['0x80','0x80','0x80','0x80','0x80'],	# ALL ON
	')' : ['0xFD','0xDE','0xF2','0xDE','0xFD'],	# Smile
	'#' : ['0xE3','0xB6','0x9C','0xB6','0xE3']	# DMC

}

header = """\
//This sketch was created using the pov.py module to 
//fill the I2C EEPROM on the POV fan
//
//LED on Pin 13 blinks once data transfer is complete
//
//Connections required:
//With fan connector on the right, pins from top to bottom
//	Fan	Pin		Arduino	UNO		Arduino Mega
//	DATA  <--->	Analog Pin 4	SDA Pin 20
//	Vcc   <--->	3.3V            3.3V
//	CLK   <--->	Analog Pin 5	SCL Pin 21
//	GND   <--->	GND             GND
//	(botom pin is not used)


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
    """
    :param screens: Screen contents
    :type screens: list of strings
    :param name: Folder/File name for Arduino sketch
    :type name: string
    """        
    def __init__(self, screens, name='pov_sketch'):
        self.screens = screens
        self.name = name     
        self.check_inputs()
        
        self.address_counter = 0
        self.i2c_address = '0x50'
        
        if not os.path.isdir(name):
            os.mkdir(name)
        
        self.sketch = open(name + '/' + name + '.ino', 'w')
        self.sketch.write(header)
        self.sketch.write('  Wire.beginTransmission(' + str(self.i2c_address) +  ');\n')
        self.sketch.write('  Wire.write(' + str(self.address_counter) + ');\n')
        self.sketch.write('  Wire.write(' + str(len(screens)) + ');\n')
        self.increment_address()
        
        for screen in self.screens:
            self.write_screen(screen)
        
        self.sketch.write(footer)
        self.sketch.close()

    def check_inputs(self):
        #Drop screens with invalid characters
        for screen in self.screens:
            try:
                for letter in screen:
                    characters[letter]
            except KeyError:
                print('Bad character: ' + letter)
                print('\tOn screen: ' + screen)
                raise(Exception)
        
        #Drop screens with too many characters
        for screen in self.screens:
            if len(screen) > 20:
                print('Max number of letters is 20')
                print('\tOn screen: ' + screen)
                raise(Exception)
        
        #Drop screens if too many provided
        if len(self.screens) > 6:
            print('Max number of screens is 6')
            while len(self.screens) > 6:
                raise(Exception)
        
        print('Valid Screens:')
        print(self.screens)

    def increment_address(self):
        self.address_counter += 1
        if self.address_counter >= 256:
            self.i2c_address = '0x51'
        if self.address_counter >= 511:
            print('Error: Too much data...shorten messages')
            raise(Exception)
    
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
            for character in characters[letter]:
                self.sketch.write('  Wire.write(' + character + ');\n')
                self.increment_address()
                self.check_page_break()