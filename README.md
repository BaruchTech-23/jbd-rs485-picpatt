# jbd-rs485-picpatt

This python module is to decode and read the RS485 data from the JBD BMS, exclusively for 4S300A (SP04S060-S-H V2.1) BMS. 

**Prerequisites**

RS485 to USB Converter 

**File structure** 

<pre>
pic-patt-rs485
           |_ main.py
           |_ JBD_RS485_4s300a.py
           |_requirements.txt   
</pre>
           



**Brief Explanation of the module**

In the JBD_RS485_4s300a.py, there is a function called read_jbd_rs485 that takes the command as the parameter. There are several commands to manipulate and control the BMS, but essentially, there are only two commands required to get overall voltage, current, alarms, individual cell voltages, and state-of-charge of the batteries. 

Command code 0x03 is to get the overall status and information of the batteries, and 0x04 is for monitoring the individual cell voltages. Those are mapped as OVERALL_STATUS_COMMAND and CELL_VOLTAGE_COMMAND in the script. 0xDD and 0x77 are the start byte and stop byte of the frame, respectively. CRC is done by a lambda function named "calculateCRC" and takes the command code as the function parameter. 

**How to use the module?**

Just import the read_jbd_rs485 from JBD_RS485_4s300a and read the values. The function returns a dictionary. Since the module already imported time and serial (pyserial), functions or classes associated with those modules and packages can be accessed through the JBD_RS485_4s300a module. Example usage 

<pre>
from JBD_RS485_4s300a import read_jbd_rs485
print(read_jbd_rs485())
</pre>

It will return a dictionary to read as follows and later can be utilised in automation. 

![result](https://github.com/user-attachments/assets/8abf0042-a6ce-4073-8f71-be2da25a1529)
