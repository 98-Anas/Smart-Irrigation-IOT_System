# Import standard python modules
import time
import requests
from ipcqueue import sysvmq
import ipcqueue

# BLYNK_AUTH_TOKEN
token="tNLSsoClrefAM_7Ma9USfUNCSDAMgWrd"
queue = sysvmq.Queue(1)                # Make a Queue to send to Adafruit

def readVirtualPin(token,pin):
        api_url = "https://blynk.cloud/external/api/get?token="+token+"&"+pin
        response = requests.get(api_url)
        return response.content.decode()

data = "0"

#charge = readVirtualPin(token,"v2") # Read the charge button
mode = readVirtualPin(token,"v1") # Read the mode button
data = readVirtualPin(token,"v0") # Read pump button
prevmode = " "                    # Initialize previous variable to send only on change
prevdata = " "
#prevcharge= " "

try:
    while True:
        mode = readVirtualPin(token,"v1") # Read the mode button
        data = readVirtualPin(token,"v0") # Read pump button
        #charge = readVirtualPin(token,"v2") # Read the charge button
        if prevmode!=mode or prevdata!=data:
#            print("Mode is: ",mode)
#            print("Data is: ",data)
            #print("charge
            queue.put((mode, data))
        prevmode=mode
        prevdata=data
        #prevcharge=charge
        time.sleep(1)
finally:
    pass
