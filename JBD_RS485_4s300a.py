"""
Name: JBD RS485 Protocol Reader
Company: Baruch Enterprises Ltd
Date: 27/1/2025
Version: 1.0
Developer: Min T. Zan
Description: This is a Python script to read and
decode the BMS values of the 12V 300A (SP04S060-S-H V1.2) JBD BMS. 

"""

#Commands
OVERALL_STATUS_COMMAND = 0x03
CELL_VOLTAGE_COMMAND   = 0x04

def get_bms_data(command):
    """ Function to get the bms data """
    calculateCRC = lambda command: [(((~command & 0xFFFF)+1) >> 8) & 0xFF,
                                    ((~command & 0xFFFF)+1) & 0xFF]
    h_byte, l_byte = calculateCRC(command)
    return [0xDD, 0xA5, command, 0x00, h_byte, l_byte, 0x77]

"""Require headers"""
import serial
from time import sleep

"""Read RS485 data from the BMS"""
def read_jbd_rs485(COM_PORT):
    ser = serial.Serial("COM"+str(COM_PORT), baudrate=9600, timeout=1)
    
    """Get overall data"""
    
    overall_status_response = ""

    while(len(overall_status_response) < 80):
        ser.write(get_bms_data(OVERALL_STATUS_COMMAND))
        overall_status_response = ser.readline().hex().upper()
        if(len(overall_status_response) >= 80):
            two_byte_status = [int(overall_status_response[i:i+4],16) for i in range(8, 43, 4)]
            one_byte_status = [int(overall_status_response[i:i+2],16) for i in range(44, 53, 2)]
            break

    sleep(0.5)

    """Get individual cell voltages"""
    
    cell_voltage_response = ""

    while(len(cell_voltage_response) < 30):
        ser.write(get_bms_data(CELL_VOLTAGE_COMMAND))
        cell_voltage_response = ser.readline().hex().upper()
        if(len(cell_voltage_response) > 31):
            cell_raw_data = [cell_voltage_response[i:i+4] for i in range(16,len(cell_voltage_response)-6,4)]
            cell_data = [(int(val,16)/1000) for val in cell_raw_data]
            break
        elif (len(cell_voltage_response) < 38):
            cell_raw_data = [cell_voltage_response[i:i+4] for i in range(8,len(cell_voltage_response)-6,4)]
            cell_data = [(int(val,16)/1000) for val in cell_raw_data]
            break

    """Process Received Data"""
    
    #Current processing in A
    if two_byte_status[1] > 0x7FFF:
            current = (two_byte_status[1] - 0x10000) * 0.01
    else:
        current = two_byte_status[1] * 0.01

    results = {
        "Voltage" : two_byte_status[0]/100,
        "Current" : current,
        "SOC"     : one_byte_status[1],
        "installed_capacity" : two_byte_status[3]/100,
        "remaining_capacity" : two_byte_status[2]/100,
        "alarms"             : two_byte_status[8],
        "num_of_cycles"      : two_byte_status[4],
        "cell_1"             : cell_data[0],
        "cell_2"             : cell_data[1],
        "cell_3"             : cell_data[2],
        "cell_4"             : cell_data[3]
        }

    return results
        
