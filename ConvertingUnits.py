# CC: Brooks Brickley & Hector Hernandez
from math import *
print("What is the name of the file you are converting?")
file = input() + '.csv'
FileID = open(file, 'r')
data = []
nextline = FileID.readline()
print("What do you want to name the output file?")
print("What is the conversion factor in CM/PX?")
factor = float(input())
file = input() + '.csv'
outfile = open(file, 'w')
nextline = FileID.readline()

while nextline != '':
    data.append(nextline.split(','))
    nextline = FileID.readline()

time = []
for i in range(len(data)):  # Converts the milliseconds to seconds
    time.append((float(data[i][1]))/1000)

position_x = []
position_y = []
for i in range(len(data)):  # Converts the position from pixels to centimeters
    position_x.append((float(data[i][3]))*factor)
    position_y.append((float(data[i][4]))*factor)

outfile.write('Time, Position_x, Position_y, \n')
for i in range(len(data)):
    a = str(time[i]) + ',' + str(position_x[i]) + ',' + str(position_y[i]) + '\n'
    outfile.write(a)


