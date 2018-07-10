# Bitalino Example made during HKU Bio Hack Day
# July 3 2018
# Mark IJzerman

# code being tested with Python 3.7

from bitalino import BITalino
import time
import OSC # SO to Machiel & the ECT/Maplab OG's yo
import math

macAddress = "/dev/tty.BITalino-DevB"

# Set OSC ip and port
ip = '127.0.0.1'
port = 4444
    
batteryThreshold = 30
acqChannels = [0, 1, 2, 3, 4] # get A1, A2, A3, A4, A5
samplingRate = 100 # only 100 or 1000?
nSamples = 1
digitalOutput = [1,1]

# Connect to BITalino
device = BITalino(macAddress)

# Set battery threshold
device.battery(batteryThreshold)

# Set OSC settings
client = OSC.OSCClient()
client.connect((ip, int(port)))

# Read BITalino version
print(device.version())
    
# Start Acquisition
device.start(samplingRate, acqChannels)



while True:
    try:
        # Read samples
        fromBitalino = device.read(nSamples)
        print(fromBitalino[0])

        # transfer functions: http://bitalino.com/datasheets/

        # READ EDA
        # implement transfer function from http://bitalino.com/datasheets/REVOLUTION_EDA_Sensor_Datasheet.pdf
        ADC_EDA = fromBitalino[0][6]
        EDA_uS = ((ADC_EDA / 2**6) * 3.3) / 0.132

        # Push EDA to OSC
        msg = OSC.OSCMessage()
        msg.setAddress("/a3")
        msg.append(EDA_uS)
        client.send(msg)

        # READ ECG
        ADC_ECG = fromBitalino[0][5]
        ECG = (((ADC_ECG / 2**6) * 3.3) / 1100) * 1000

        # Push ECG to OSC
        msg = OSC.OSCMessage()
        msg.setAddress("/a2")
        msg.append(ECG)
        client.send(msg)
        
        # READ EEG
        ADC_EEG = fromBitalino[0][7]
        EEG = ((((ADC_EDA / 2**6) - 0.5) * 3.3 )/ 40000) * 1000000

        # Push EEG to OSC
        msg = OSC.OSCMessage()
        msg.setAddress("/a4")
        msg.append(EEG)
        client.send(msg)

    except KeyboardInterrupt:
        # Stop BT acquisition
        device.stop()
        # Close BT connection
        device.close()
        # Close OSC connection
        client.close()
        break