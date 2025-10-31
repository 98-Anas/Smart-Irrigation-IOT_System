import Adafruit_DHT

def DHT_init():
    sensor = Adafruit_DHT.DHT22
    return sensor

def DHT22_read(sensor,pin):
    try:
        humidity, temperature_c = Adafruit_DHT.read_retry(sensor, pin)
        #print("Temp: {:.1f} C    Humidity: {}% ".format(temperature_c, humidity))
        return humidity, temperature_c
    except RuntimeError as error:
        print(error.args[0])

