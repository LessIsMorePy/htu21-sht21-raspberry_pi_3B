import smbus
import time
 
# Get I2C bus
bus = smbus.SMBus(1)

# address: htu21df/sht21
device = 0x40

# temperature
data = bus.read_i2c_block_data(device, 0xE3)

big_int = (data[0] * 256) + data[1] # combine both bytes into one big integer 
temperature = ((big_int / 65536) * 175.72) - 46.85 # formula from datasheet

# humidity
data = bus.read_i2c_block_data(device, 0xE5)

big_int = (data[0] * 256) + data[1] # combine both bytes into one big integer 
humidity = ((big_int / 65536) * 125) - 6 # formula from datasheet

print('Temperature: {:.2f}°C'.format(temperature))
print('Humidity: {:.2f}%'.format(humidity))
# to get the compensated humidity we need to read the temperature
print('Humidity: {:.2f}%'.format((25-temperature)*0.15 + humidity))
