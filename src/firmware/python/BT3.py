'''!    @file   BT3.py
        @brief  Bluetooth testing
        @author Juan Luna
        @date   2021-05-26 Created
'''

import bluetooth
import subprocess

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM) ## RFCOMM server setup
port = 1
server_sock.bind(("",port))
server_sock.listen(1)
client_sock,address = server_sock.accept()
print ("Accepted connection from "), address

while True:
    recvdata = client_sock.recv(1024)
    print ("Received \"%s\" through Bluetooth") % recvdata
    
    if (recvdata=="startup"):
        subprocess.call("python LEDhappy_script.py", shell = True)
    
    elif (recvdata =="gravity"):                                        # words received from Android that initate various python scripts.
        subprocess.call("python LEDsmile_script.py && python motor1.5_script.py", shell= True) # question right
        subprocess.call("python LEDhappy_script.py",shell = True)
    
    elif (recvdata == "packers"):                                     # question wrong 
         subprocess.call("python LEDneutral_script.py", shell= True)
         #subprocess.call("python LEDsmile_script.py", shell = True)
    
    elif (recvdata == "completeread"):
         subprocess.call("python stars_script.py", shell = True) # done reading
         subprocess.call("python LEDhappy_script.py", shell = True)       
    
    elif (recvdata == "completequestions"):
        subprocess.call("python rainbow_script.py && python motor3_script.py", shell = True) # done with questions
        
    elif (recvdata == "lookup"):
        subprocess.call("python servoUP_script.py", shell = True) # done with questions
        
    elif (recvdata == "lookmid"):
        subprocess.call("python servoMID_script.py", shell = True) # done with questions
        
    elif (recvdata =="rainbow"):
        subprocess.call("python stars_script.py", shell= True)
        subprocess.call("python rainbow_script.py", shell= True)
    
# client_sock.close()
# server_sock.close()