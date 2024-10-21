import serial
import time

# Set the serial port to the one your DOFBOT is connected to (check with ls /dev/tty* on Linux)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Make sure to use the correct port and baudrate
time.sleep(2)  # Give the connection some time to initialize

# Example command to move the arm (modify based on DOFBOT's command system)
# This is an example using G-code format. Adjust to match your robot's command set.
command = 'G1 X20 Y30 Z40 F1500\n'  # Example move command to set position
ser.write(command.encode())  # Send the command to the robot arm

# Wait for a response (if applicable)
response = ser.readline().decode('utf-8').strip()
print(f"Response from DOFBOT: {response}")

# Close the serial connection when done
ser.close()
