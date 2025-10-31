import relay_f
import time


fan = relay_f

while(1):
    fan.on(20)
    print("Fan ON")
    time.sleep(4)
    fan.off(20)
    print("Fan OFF")
    time.sleep(4)
