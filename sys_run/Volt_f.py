import ADC_f
import Adafruit_MCP3008
import time

def init_Volt():
    adc=ADC_f.init_adc()
    return adc

def read_volt(adc):
    #channel = 1  # Change this to the channel where your voltage sensor is connected
    channel=7

    # Floats for resistor values in divider (in ohms)
    R1 = 30000.0
    R2 = 7500.0

    # Float for Reference Voltage
    ref_voltage = 3.35
    # Number of readings to average
    num_readings = 20
    # Read the Analog Input multiple times
    #adc_values = [read_adc(channel) for _ in range(num_readings)]
    adc_values = [ADC_f.read_adc(channel,adc) for _ in range(num_readings)]

    # Calculate average ADC value
    avg_adc_value = sum(adc_values) / num_readings

    # Determine voltage at ADC input
    adc_voltage = (avg_adc_value / 1023) * ref_voltage  # MCP3008 has 10-bit resolution

    # Calculate voltage at divider input
    in_voltage = adc_voltage / (R2 / (R1 + R2))
    
    return in_voltage
