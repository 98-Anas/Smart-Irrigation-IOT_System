import Cpu_Temp_f
import time

while(1):
    temperature = Cpu_Temp_f.get_cpu_temperature()
    print(f"CPU Temperature: {temperature:.2f} °C")
    time.sleep(2)
