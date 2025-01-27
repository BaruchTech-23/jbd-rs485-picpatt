# jbd-rs485-picpatt
This python module is to decode and read the RS485 data from the JBD BMS, exclusively for 4S300A (SP04S060-S-H V2.1) BMS. 

File structure 

pic-patt-rs485
           |_ main.py
           |_ JBD_RS485_4s300a.py
           |_requirements.txt 

Connections 

|---------|                    |------------------------|
|         |_A_______________A_ |                        |  
| JBD BMS |                    | RS485 to USB Converter | -----------> Computer 
|         |_B_______________B_ |                        |
|---------|                    |------------------------|

Brief Explanation

In the JBD_RS485_4s300a.py, there is a function called read_jbd_rs485 and takes the command as the parameter. There are several commands to manipulate and control the BMS but essentially, there are only two command required to get overall voltage, current, alarams, individual cell voltages and state-of-charge of the batteries. 

Command code 0x03 is to get the overall status and information of the batteries and 0x04 is for monitoring the individual cell voltages. Those are mapped as OVERALL_STATUS_COMMAND and CELL_VOLTAGE_COMMAND in the script. 0xDD and 0x77 are start byte and stop byte of the frame respectively. CRC is done by lambda function named 
"calculateCRC" and takes the command code as the function parameter. 
