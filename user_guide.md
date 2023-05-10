### User Guide for the Reading Robot

1. [Set up](#set-up)
2. [Troubleshooting](#troubleshooting)


## Set up
1. Locate female USB-C ports on the back of the robot. The bottom port is dedicated to the Raspberry Pi and the one above is connected to the power distribution board.

<p align="center">
    <img src="" 
    width=40%    
    alt="Input ports for the robot."/>
</p>

2. Connect the Raspberry Pi port to power. To verify, you will see a red glow inside the robot.
3. Wait for a blue, happy face to appear on LED Array. This is important as it is an indicator that the serial port service has been registered and that GPIOs are reset.
4. Connect the power distribution board to power. 
5. If using a wireless headset, connect it to the Android through Bluetooth. During the first time, you will have to pair the headset to the phone. Later usage should connect the headset to the phone seamlessly.
   
Once this has all been completed, the robot should be ready to go. Now, you can open the phone app.

1. Open the [app](src/firmware/appinventor/) on the phone.
2. Once opened, a “connected” notification should show up fairly quickly to let the user know they are connected to Bluetooth. If this does not happen, you can press the robot's picture once the robot finishes its introduction dialogue. 
    - If a face change does not occur after introduction, Bluetooth is not connected and a notification error will pop up on the app. 
    - Refer to the next section, troubleshooting.
3. When the connected notifier appears, the app is ready to go. The user will read (press "begin reading" to start reading and "stop reading" to proceed to the next part) and answer questions afterwards (press "question" button).

<p align="center">
    <img src="https://github.com/jlunaing/Reading_Robot/blob/a0297223b0f796758bc3788b7378f4aecf31871a/img/ref_app_01.jpg" 
    width=40%    
    alt="Android app intro screen."/>
</p>

After the session is over:

1. Close the app and make sure to end it completely.
2. Turn off the PCB *first*. The robot does not like it when you power down the Raspberry Pi first.
   - This is currently an issue because the PCB has its I/O pins for the motors routed to the pins on the RPi that give a 3.3-V voltage on startup.
   - This is also the same reason why the PCB is turned on after the RPi’s startup sequence. 
3. Turn off the Raspberry Pi.

Optional step for users, parents, instructors, and educators:

1. To playback the audio file that was generated from the app stored in the phone, go to the storage settings of your phone and search for the generated "Reading Robot Study 2020" folder. The default file name is `mysound.3gp`. Make sure to look at the time associated with the file creation to see which corresponds to which user.
2. To view the text file that was generated from the app during the human-robot interaction, go to the storage settings and look for the corresponding `.txt` file.

## Troubleshooting

This section discusses some of the problems that could be encountered while
working with the robot as it relates to the **Bluetooth connection**.

If the Bluetooth connection doesn’t happen, it could be for a multitude of reasons. The first possible error is that the Raspberry Pi is no longer paired with the Android phone. To check for this, go to your phone settings and check for the Bluetooth paired devices. Under the “paired devices” section, there should a paired device corresponding to the Raspberry Pi used.

If this device is not there or no longer paired, you must direct your attention to the Raspberry Pi. Unscrew the bottom of the robot and connect to the Pi. After the Pi has turned on, it should show up in the “available devices” section of the
phone's Bluetooth settings. Click on Raspberry Pi device on the phone. A notification should appear on the Pi’s home screen and phone screen for a pairing request. Press confirm. The device should now be paired, and the Bluetooth connection should work between the Pi and the app.

You can hardcode the process in the above paragraph as well in terminal: `bluetoothctl` $\to$ `agent on` $\to$ `discoverable on` $\to$ `scan on`. The phone's bluetooth address should appear. Pair it with the Pi and that should work.

If the Raspberry Pi is still paired, there are two reasons why there is no bluetooth connection between the devices. ***First***, the bluetooth address might be incorrect from the development environment (Kodular) side of things. Double check and make sure the address is correct. You can find the address of your Raspberry Pi in terminal using the `hciconfig` command in the terminal. Look for the address followed by `BD Address`.

If the address is correct, then the *second* possibility is that the user troubleshooting is not waiting long enough to connect the devices. After the blue, happy face screen appears, wait an additional 15-30 seconds.

If none of this works, there could be an issue with the serial port service registering. This is a Python script that runs on startup and gives access to the Raspberry Pi serial ports. The name of the script is `register.py` and can be found with all the other scripts the robot utilizes to function. You can check to see if it ran on startup as well as anything else that happens between the Android and Pi. Look up the `/home/pi/logs` directory. The file called `cronlog` will give you a log of what happens during the interaction between the phone and Raspberry Pi. This will be pretty important when troubleshooting the robot and changing the script.
