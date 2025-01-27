
""" This is example script for JBD_RS485_4s300a module """

from JBD_RS485_4s300a import read_jbd_rs485, sleep


if __name__ == "__main__":
    COM = 5 #Check the COM port of the USB-RS485 in device manager
    results = read_jbd_rs485(COM) #Read RS485 data from COM
    print(results) #It will return as Dictionary
    print("Leaving in 5 seconds")
    sleep(5) # Some delays before exit 

