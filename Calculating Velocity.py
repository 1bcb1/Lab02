# CC: Brooks Brickley & Hector Hernandez
from math import *
print("What is the name of the file you want to open?")  # Takes in position file
file = input() + '.csv'
fileID = open(file, 'r')
print("What do you want to name the outputfile?")  # Creates Velocity File
file = input() + '.csv'
outfile = open(file, 'w')

nextline = fileID.readline()
nextline = fileID.readline()
data = []
while nextline != '':
    data.append(nextline.split(','))
    nextline = fileID.readline()

time = []
x = []
y = []
for i in range(len(data)):
    time.append(float(data[i][0]))
    x.append(float(data[i][1]))
    y.append(float(data[i][2]))

velocity_x = []
velocity_y = []

for i in range(len(data)-1):  # Calculates the velocity for both x and y using rate of change
    change_time = time[i + 1] - time[i]
    a = (x[i + 1] - x[i])/(change_time)
    b = (y[i + 1] - y[i])/(change_time)
    velocity_x.append(a)
    velocity_y.append(b)

outfile.write("Time, VelocityX, VelocityY \n")
for i in range(len(velocity_x)):  # Writes the new output file
    c = str(time[i]) +',' + str(velocity_x[i]) + ',' + str(velocity_y[i]) + '\n'
    outfile.write(c)
