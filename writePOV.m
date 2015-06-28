%writePOV.m
%08-24-11
%Zach Jones
%This script creates an Arduino sketch to load
%text onto the POV fan.  Add phrases in the
%user input section below

%Run with Octave (or Matlab)

%Cell arrays of character codes for LEDs
A = {'0xE0','0xDB','0xBB','0xDB','0xE0'};
B = {'0xF9','0xC6','0xB6','0xB6','0x80'};
C = {'0xDD','0xBE','0xBE','0xDD','0xE3'};
D = {'0xE3','0xDD','0xBE','0xBE','0x80'};
E = {'0xB6','0xB6','0xB6','0xB6','0x80'};
F = {'0xBF','0xB7','0xB7','0xB7','0x80'};
G = {'0xF3','0xB5','0xB6','0xBC','0xC3'};
H = {'0x80','0xF7','0xF7','0xF7','0x80'};
I = {'0xBE','0xBE','0x80','0xBE','0xBE'};
J = {'0x81','0xFE','0xFE','0xFE','0xFD'};
K = {'0xBE','0xDD','0xEB','0xF7','0x80'};
L = {'0xFE','0xFE','0xFE','0xFE','0x80'};
M = {'0x80','0xDF','0xEF','0xDF','0x80'};
N = {'0x80','0xF9','0xE3','0xCF','0x80'};
O = {'0xE3','0xDD','0xBE','0xDD','0xE3'};
P = {'0xCF','0xB7','0xB7','0xB7','0x80'};
Q = {'0xE2','0xDD','0xBA','0xDD','0xE3'};
R = {'0xDE','0xAD','0xAB','0xB7','0x80'};
S = {'0xD9','0xB6','0xB6','0xB6','0xCD'};
T = {'0xBF','0xBF','0x80','0xBF','0xBF'};
U = {'0x81','0xFE','0xFE','0xFE','0x81'};
V = {'0x83','0xFD','0xFE','0xFD','0x83'};
W = {'0x80','0xFD','0xFB','0xFD','0x80'};
X = {'0xBE','0xDD','0xE3','0xDD','0xBE'};
Y = {'0x8F','0xEF','0xE0','0xEF','0x8F'};
Z = {'0x9E','0xAE','0xB6','0xBA','0xBC'};				    
space = {'0xFF','0xFF','0xFF','0xFF','0xFF'};

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% User Input Start %%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Create a new cell array for each screen to appear on the fan
screen1 = {T,E,S,T,I,N,G,space,P,O,V,space,F,A,N};
screen2 = {A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T};
screen3 = {U,V,W,X,Y,Z};
screen4 = {S,C,R,E,E,N,space,F,O,U,R};
screen5 = {S,C,R,E,E,N,space,F,I,V,E};
screen6 = {S,C,R,E,E,N,space,S,I,X};

%Put name of each screen cell array in this array
screens = {screen1,screen2,screen3,screen4,screen5,screen6};
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%% User Input End %%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%Check inputs
if length(screens)>6
	error('6 SCREENS MAX');
end
for i = 1:length(screens)
	if length(screens{i}) >20
		error('20 CHARACTERS MAX PER SCREEN');
	end
end

%Initialize counter
addressCounter = 0;
i2cAddress = '0x50';

%Create output file
delete('pdeText.txt');
fid = fopen('pdeText.txt','w');
fprintf(fid,'Wire.beginTransmission(%s);\n',i2cAddress);
fprintf(fid,'Wire.send(%.0f);\n',addressCounter);
fprintf(fid,'Wire.send(%.0f);\n',size(screens,2));
addressCounter = addressCounter + 1;

for i = 1:size(screens,2)
	message = fliplr(screens{i});
	fprintf(fid,'Wire.send(%.0f);\n',size(message,2));
	addressCounter = addressCounter+1;
	if addressCounter >= 256
		i2cAddress = '0x51';
	end
	if mod(addressCounter,16) == 0
		fprintf(fid,'Wire.endTransmission();\n');
		fprintf(fid,'delay(500);\n');
		fprintf(fid,'Wire.beginTransmission(%s);\n',i2cAddress);
		fprintf(fid,'Wire.send(%.0f);\n',mod(addressCounter,256));
	end
	for j = 1:size(message,2)
		for k = 1:5
			fprintf(fid,'\tWire.send(%s);\n',message{j}(k));
			addressCounter = addressCounter+1;
			if addressCounter >= 256
				i2cAddress = '0x51';
			end
			if mod(addressCounter,16) == 0
				fprintf(fid,'Wire.endTransmission();\n');
				fprintf(fid,'delay(500);\n');
				fprintf(fid,'Wire.beginTransmission(%s);\n',i2cAddress);
				fprintf(fid,'Wire.send(%.0f);\n',mod(addressCounter,256));
			end
		end
	end
end
fprintf(fid,'Wire.endTransmission();\n');
fclose(fid);
%finalPDE.pde is the resulting Arduino sketch to run
system('cat header.txt pdeText.txt footer.txt > finalPDE.pde');
if addressCounter >511
	error('TOO MUCH DATA....SHORTEN MESSAGES');
end
