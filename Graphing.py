# CC: Brooks Brickley & Hector Hernandez
import matplotlib.pyplot as plt

print("What is the name of the position file you want plot?")  # Gets the position file
position = input() +'.csv'

print("What is the name of the velocity file that you want to plot?")  # Gets the velocity file
velocity = input() + '.csv'

print("What is the name of the acceleration file that you want to plot?")  # Gets the acceleration file
acceleration = input() + '.csv'
pfile = open(position, 'r')
vfile = open(velocity, 'r')
afile = open(acceleration, 'r')

pdata = []
nextline = pfile.readline()
nextline = pfile.readline()

while nextline != '':
    pdata.append(nextline.split(','))
    nextline = pfile.readline()

vdata = []
nextline = vfile.readline()
nextline = vfile.readline()

while nextline != '':
    vdata.append(nextline.split(','))
    nextline = vfile.readline()

adata= []
nextline = afile.readline()
nextline = afile.readline()

while nextline != '':
    adata.append(nextline.split(','))
    nextline = afile.readline()

pos_time = []
pos_x = []
pos_y = []

for i in range(len(pdata)):  # Gets the position of both x and y and time
    pos_time.append(float(pdata[i][0]))
    pos_x.append(float(pdata[i][1]))
    pos_y.append(float(pdata[i][2]))

vel_time = []
vel_x = []
vel_y = []

for i in range(len(vdata)):  # Gets the velocity of both x and y and the velocity time
    vel_time.append(float(vdata[i][0]))
    vel_x.append(float(vdata[i][3]))
    vel_y.append(float(vdata[i][4]))

acc_time = []
acl_x = []
acl_y = []
for i in range(len(adata)):  # Gets the acceleration of both x and y and the acceleration time
    acc_time.append(float(adata[i][0]))
    acl_x.append(float(adata[i][3]))
    acl_y.append(float(adata[i][4]))

# Below are is the code to plot all the position, velocity, and acceleration
ax1 = plt.subplot(3, 2, 1)
ax1.plot(pos_time, pos_x)
ax1.set(ylabel=' X Position (CM)')
ax1.set_title('Position of X')

ax2 = plt.subplot(3, 2, 2)
ax2.plot(pos_time, pos_y)
ax2.set(ylabel='Y Position (CM)')
ax2.set_title('Position of Y')

ax3 = plt.subplot(3, 2, 3)
ax3.plot(vel_time, vel_x, 'r-')
ax3.set(ylabel='Velocity (CM/S)')
ax3.set_title('Velocity of X')

ax4 = plt.subplot(3, 2, 4)
ax4.plot(vel_time, vel_y, 'r-')
ax4.set(ylabel='Velocity (CM/S)')
ax4.set_title('Velocity of Y')

ax5 = plt.subplot(3, 2, 5)
ax5.plot(acc_time, acl_x, 'g-')
ax5.set(ylabel='Acceleration (CM/S\u00B2)')
ax5.set(xlabel='Time (Seconds)')
ax5.set_title('Acceleration of X')

ax6 = plt.subplot(3, 2, 6)
ax6.plot(acc_time, acl_y, 'g-')
ax6.set(ylabel='Acceleration (CM/S\u00B2)')
ax6.set(xlabel='Time (Seconds)')
ax6.set_title('Acceleration of Y')

plt.suptitle('Position, Velocity, and Acceleration of X and Y Components of the Puck')
plt.show()