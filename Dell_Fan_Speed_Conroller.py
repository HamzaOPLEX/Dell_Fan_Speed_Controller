import subprocess

# Prompt user for fan speed in decimal format
speed_decimal = int(input("Enter fan speed (e.g. 30): "))

# Convert decimal speed to hex format
speed_hex = hex(speed_decimal)[2:]  # remove '0x' prefix from hex string

# Build IPMItool command string with selected speed
command = f"ipmitool -H 192.168.1.120 -U root -P calvin raw 0x30 0x30 0x02 0xff 0x{speed_hex}"

# Run IPMItool command
subprocess.run(command, shell=True)
