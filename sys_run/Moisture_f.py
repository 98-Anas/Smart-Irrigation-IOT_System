import ADC_f
import Adafruit_MCP3008
import time

def init_mois():
    adc=ADC_f.init_adc()
    return adc

def read_Moisture(adc):
    try:
        num_readings=20
        # Read ADC value from the sensor
        # adc_value = ADC_f.read_adc(0,adc)
        adc_values = [ADC_f.read_adc(6,adc) for _ in range(num_readings)]
        avg_adc_value = sum(adc_values) / num_readings
        map=map_value(avg_adc_value)
        # Convert ADC value to percentage (adjust as needed)
        moisture_percentage = (map / 600) * 100
        #print("ADC value is:",avg_adc_value)
        #print("mapped ADC value is:",map)
        #print(f"Soil Moisture: {moisture_percentage:.2f}%")
        #sleep(1)  # Wait for a second before the next reading
        return moisture_percentage
    except KeyboardInterrupt:
        pass

def map_value(input_value):
    input_min = 290
    input_max = 775
    output_min = 0
    output_max = 600

    # Map the input value to the output range
    mapped_value = (input_value - input_min) * (output_max - output_min) / (input_max - input_min) + output_min
    return mapped_value


"""
adc=init_mois()
while(1):
    read_Moisture(adc)
    time.sleep(2)
"""
