# CC: Brooks Brickley & Hector Hernandez
from math import *

print('What is the name of the velocity file you want to open?')  # Asks for velocity file
file = input() + '.csv'

print('What is the name of the file you want to output?')  # Creates new Acceleration file
output = input() + '.csv'

fileID = open(file, 'r')
outputfile = open(output, 'w')

data = []
nextline = fileID.readline()
nextline = fileID.readline()

while nextline != '':
    data.append(nextline.split(','))
    nextline = fileID.readline()

time = []
vel_x = []
vel_y = []
for i in range(len(data)):
    time.append(float(data[i][0]))
    vel_x.append(float(data[i][3]))
    vel_y.append(float(data[i][4]))

acl_x = []
acl_y = []

for i in range(len(data)-1):  # Calculates the Acceleration using the rate of change formula
    change_time = time[i+1] - time[i]
    a = (vel_x[i+1]-vel_x[i])/(change_time)
    b = (vel_y[i+1]-vel_y[i])/(change_time)
    acl_x.append(a)
    acl_y.append(b)

outputfile.write('Time, Accleration_X, Accleration_Y \n')
for i in range(len(acl_x)):
    c = str(time[i]) + ',' + str(acl_x[i]) + ',' + str(acl_y[i]) + '\n'
    outputfile.write(c)
