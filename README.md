### Reading-Robot
A socially assistive robot that can help students with reading practice. For 
instructions on how to use the system, see [user guide]().

1. [Background](#background)
2. [Making a Reading Robot](#making-a-reading-robot)
   1. [Part List](#part-list)
      1. [General parts:](#general-parts)
      2. [Actuation:](#actuation)
      3. [Fasteners:](#fasteners)
      4. [Electronics:](#electronics)
   2. [Power:](#power)
   3. [Code](#code)


## Background

There is an insufficient availability of human experts to assist students in 
reading competency and comprehension. The goal of this porject is to create an 
socially assistive robot that can be used by therapists, teachers, and parents 
to help children and adults develop and practice reading comprehension skills 
while they do not have access to specialists. This robot enables the user to 
improve their reading skills without an educator present and allows educators to 
review the student's performance remotely. 

The design includes a robot and a phone running an app. The basic tasks that the
robot performs is to give instructions for the reading sessions and prompts the
student to start reading. The robot then records the passage read to allow a 
teacher or therapist to review it at a later time. Then, the robot asks 
questions based on the reading and gives constructive feedback based on the 
correctness of the responses. During the interaction, the robot has the ability
to tilt the phone back and forth, wiggle its antennas, and show different faces
on its LED screen. This gives the interaction with the user more embodiment.

## Making a Reading Robot

### Part List
To make one of this robots, the following parts are needed:

#### General parts:
- 3D printed parts (see [CAD files](src/hardware/cad/solidworks/)).
- Android phone (1)
- Bluetooth headset (optional) (1)
- Pimoroni Unicorn Hat HD LED array (1)					

#### Actuation:
- TowerPro MG995 Digital servo motor (1)				
- Uxcell 6V DC motor, 100-rpm (1)	
- Adafruit TB6612 motor driver board (1)					
- 6455K13 plastic ball bearing (2)					
- RB-Tib-11 Lynxmotion servo timing belt pulley (2)					
- 1254N22 MXL timing belt pulley (1)	

#### Fasteners:
- Tapered heat-set inserts:
  - 2-56 thread size (93365A110)			
  - 4-40 thread size (93365A120)
- Screws:
  - 18-8 screw 1/2'' long (91772A110)
  - 2-56 screw 11/32'' long (91772A506)
  - 2-56 screw 3/16'' long (91772A076)
  - 4-40 screw 3/4'' long (91772A113)			
- Neodymium magnet 1/4'' (5862K103) (8)
- 18-8 binding barrel & screw (99637A307) (1)
- Nylon spacers (90176A114)
- 5/8'' Long Dowel Pin (98381A539)					
- 2 – 1/8'' Long Dowel Pin (98381A325)					


#### Electronics:
- Raspberry Pi 4 + SD card
- Custom PCB for power distribution (see [board files](src/hardware/pcb/))
- 40-pin connector (S9200-ND) (2)
- USB-C breakout board (1568-1958-ND)
- JST RCY connector, 2-pin (PRT-10501)					
- JST jumper 2-wire (PRT-09914)					
- JST jumper 3-wire (PRT-09915)

### Power:
- AUKEY USB-C 2 port charger					
- AC adapter/power supply (2)					
- USB 3.1 type C M-F data extension cable (2)					

The assembly of the robot can be facilitated by refering to the assembly drawings
or the [CAD files](src/hardware/cad/solidworks/). Some reference images are 
included below.

<p align="center">
    <img src="" 
    width=40%    
    alt="Body assembly"/>
</p>

<p align="center">
    <img src="" 
    width=40%    
    alt="Head assembly"/>
</p>

### Code

See [source files](src/firmware/python/) for details.