import smbus
import time

# Create an instance of the I2C bus (1 is the I2C bus number on the Raspberry Pi)
bus = smbus.SMBus(1)

# Update with your detected I2C address
DEVICE_ADDRESS = 0x3C  # Use the address from i2cdetect

try:
    # Example: Write to a register (replace with the correct register and value for your device)
    bus.write_byte_data(DEVICE_ADDRESS, 0x00, 0xFF)  # Writing 0xFF to register 0x00
    print("Write successful")

    # Example: Read from a register (replace with the correct register for your device)
    data = bus.read_byte_data(DEVICE_ADDRESS, 0x00)  # Reading from register 0x00
    print(f"Data read from device: {data}")

except OSError as e:
    print(f"Error: {e}")

# I2C address of your motor driver (replace with your driver's address)
MOTOR_DRIVER_ADDRESS = 0x15  # Example address (check your driver’s documentation)

def set_motor_speed(speed):
    # Assuming your motor driver accepts speed values from 0 to 255
    # where 0 is stopped and 255 is full speed
    bus.write_byte(MOTOR_DRIVER_ADDRESS, speed)

try:
    # Move forward
    print("Moving forward")
    set_motor_speed(255)  # Full speed
    time.sleep(2)         # Move for 2 seconds

    # Stop
    print("Stopping")
    set_motor_speed(0)     # Stop the motors
    time.sleep(1)

    # Move backward
    print("Moving backward")
    set_motor_speed(-255)  # Assuming your driver accepts negative values for reverse
    time.sleep(2)

    # Stop
    print("Stopping")
    set_motor_speed(0)

except Exception as e:
    print(f"Error: {e}")
finally:
    # Ensure motors stop before exiting
    set_motor_speed(0)
