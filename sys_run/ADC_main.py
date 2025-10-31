import Moisture_f
import Volt_f
import time



def read_ADC(adc):
    volt=Volt_f.read_volt(adc)
    time.sleep(2)
    moisper=Moisture_f.read_Moisture(adc)
    time.sleep(2)
    return volt, moisper

def change(prev,val,diff):
    if abs(prev-val)>diff:
        return True
    else:
        return False

