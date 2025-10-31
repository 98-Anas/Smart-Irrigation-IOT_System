import Adafruit_MCP3008
import board
from time import sleep
import paho.mqtt.client as mqtt
from ipcqueue import sysvmq
import ipcqueue
import queue


########NEW IMPORTS########
import DHT_f
import ADC_main
import Cpu_Temp_f
import relay_f


# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = 'aio_HILI73f0Vkfk8ZIso9ozk78nevuA'

# Set to your Adafruit IO username.
ADAFRUIT_IO_USERNAME = 'zonzo'

# Create an instance of the MQTT client.
client = mqtt.Client()

# Connect to the MQTT broker.
client.username_pw_set(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.connect("io.adafruit.com", 1883, 60)


# Actuators Objects
fan_f = relay_f
pump_f = relay_f
charger_f = relay_f

# Actuators Pins
fan = 20
charger = 21
pump = 17

# sensors inits
dht_sensor=DHT_f.DHT_init()
am = Adafruit_MCP3008.MCP3008(clk=11, cs=8, miso=9, mosi=10)

queue_list = sysvmq.Queue(1)                                    # initialize the queue to read from

# Adafruit IO Function
def send_to_adafruit_io(feed_name, value):
    topic = f"{ADAFRUIT_IO_USERNAME}/feeds/{feed_name}"
    client.publish(topic, str(value))


# Blynk & Adafruit values
mode = "0"                                              # Automatic mode
data = "0"                                              # Pump off initially
pstate = 0


while True:

    # Receive messages from the queue
    # mode, data, plant_type = queue_list.get(block=False)
    mode, data = queue_list.get()
#    print(f"Received: {mode}, {data}")


    if mode == "0":                                     # If automatic mode read the sensor and update automatically
        sleep(0.5)
        send_to_adafruit_io("mode", 0)

	# CPU Temp read and send
        cputemperature = int(Cpu_Temp_f.get_cpu_temperature())
        send_to_adafruit_io("cpu_temp",cputemperature)
#        print("CPU Temperature: ", cputemperature)

        sleep(0.5)

	#temp_humid_readings()
        prev_humid,prev_temp = DHT_f.DHT22_read(dht_sensor,4) # save previous readings
        send_to_adafruit_io("Temperature", prev_temp)
        send_to_adafruit_io("Humidity", prev_humid)

        sleep(1.5)

        volt, mois_per = ADC_main.read_ADC(am)
        volt_per = int((volt*100) / 12.6)
#        print("volt and batterycap = ",volt," ",volt_per)

        sleep(1.5)


        if mois_per > 50:
#            print("No water, Can you please water me")
            pstate = 1
            pump_f.on(pump)

        elif mois_per < 25:
#            print("I'm sufficient")
            pstate = 0
            pump_f.off(pump)

        if (mois_per > 0 and mois_per < 100):    # Send value only if change bigger than 2.5
            send_to_adafruit_io("soil moisture", mois_per)
#            print("Sent moisture value of:",mois_per)
            sleep(1.5)

        if (mois_per > 0 and mois_per < 100):    # Send value only if change bigger than 2.5
            send_to_adafruit_io("BatteryCapacity", volt_per)
#            print("Sent battery value of:",volt_per)
            sleep(1.5)

        if volt_per <= 25:
            charger_f.on(charger)
#            print("charger on")
            sleep(1.5)
            send_to_adafruit_io("AutoCharge", 1)

        elif volt_per > 25:
            charger_f.off(charger)
#            print("charger off")
            sleep(1.5)
            send_to_adafruit_io("AutoCharge", 0)

        if cputemperature < 40:
            fan_f.on(fan)
#            print("fan off")
            sleep(1.5)
            send_to_adafruit_io("fan_indicator", 0)

        elif cputemperature > 40:
            fan_f.off(fan)
#            print("fan on")
            sleep(0.5)
            send_to_adafruit_io("fan_indicator", 1)

    elif mode == "1":                                   # If mode is manual control by button
        sleep(0.5)
        send_to_adafruit_io("mode", 1)

        # CPU Temp read and send
        cputemperature = int(Cpu_Temp_f.get_cpu_temperature())
        send_to_adafruit_io("cpu_temp",cputemperature)
#        print("CPU Temperature: ", cputemperature)

        sleep(0.5)

        #temp_humid_readings()
        prev_humid,prev_temp = DHT_f.DHT22_read(dht_sensor,4) # save previous readings
        send_to_adafruit_io("Temperature", prev_temp)
        send_to_adafruit_io("Humidity", prev_humid)

        sleep(0.5)

        volt, mois_per = ADC_main.read_ADC(am)
        volt_per = int((volt*100) / 12.6)
#        print("volt and batterycap = ",volt," ",volt_per)

        sleep(0.5)


        if (mois_per > 0 and mois_per < 100):    # Send value only if change bigger than 2.5
            send_to_adafruit_io("soil moisture", mois_per)
#            print("Sent moisture value of:",mois_per)
            sleep(1.5)

        if (mois_per > 0 and mois_per < 100):    # Send value only if change bigger than 2.5
            send_to_adafruit_io("BatteryCapacity", volt_per)
#            print("Sent battery value of:",volt_per)
            sleep(1.5)

        if volt_per <= 25:
            charger_f.on(charger)
#            print("charger on")
            sleep(1.5)
            send_to_adafruit_io("AutoCharge", 1)

        elif volt_per > 25:
            charger_f.off(charger)
#            print("charger off")
            sleep(1.5)
            send_to_adafruit_io("AutoCharge", 0)

        if cputemperature < 40:
            fan_f.on(fan)
#            print("fan off")
            sleep(1.5)
            send_to_adafruit_io("fan_indicator", 0)

        elif cputemperature > 40:
            fan_f.off(fan)
#            print("fan on")
            sleep(0.5)
            send_to_adafruit_io("fan_indicator", 1)

        if data == "1":
            pump_f.on(pump)
            pstate = 1

        elif data == "0":
            pump_f.off(pump)
            pstate = 0

    send_to_adafruit_io("pump_indicator", pstate)
    sleep(3)
