import DHT_f
import time
from ipcqueue import sysvmq
import ipcqueue



while(1):

    sensor=DHT_f.DHT_init()
    humid,temp=DHT_f.DHT22_read(sensor,4)
    """if (prev_humid - humidity)>1.5 or (humidity - prev_humid)>1.5: # send humidity value if change occured
        dht_Q.put((humid,temp))
        print("sent_humid", humidity)
    if (prev_temp - temperature_c)>1.5 or (temperature_c - prev_temp)>1.5: # send temp value if change occured
        dht_Q.put((humid,temp))
        print("sent_temp",temperature_c)
    time.sleep(2)
"""
