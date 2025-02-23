# BioData-Interfaces

Here you will find information about different BioData-Interfaces and how you can use them.
Keep an eye on the ECT Blog as well : https://pong.hku.nl/blog/ 
The different BioData interface that we are in the process of researching are:

* Bitalino
* Heartlive
* Vernier Breath Sensor 
* Muse brain-computer interface
* BrainWave brain-computer interface with BrainOSC 
* Myo (See Myo-OSC)
* Webcam for heartbeat detection (webcam pulse detector)
* Eye tracking
* Manus VR

## Using (web)Cam for heartbeat detection

Using https://thearn.github.io/webcam-pulse-detector/ as starting point we researched how you could use this in a live interactive installation.

* The webcam-pulse-detector works with Python3
* As dependencies you need to install: 
  * openCV2 `pip3 install opencv-python`  
  * Matplotlib `python3 -mpip install matplotlib` (https://matplotlib.org/faq/installing_faq.html)
* You need to keep your head still for calibrating
* It is unclear how accurate it is

Using [this](https://github.com/ikbenmacje/webcam-pulse-detector) fork you can also send out the pulse as OSC message.

## Eye tracking

We tested eyetracking using the [Tobii eyeX](https://tobiigaming.com/product/tobii-eyex/). First thing to note is that this tracker **ONLY** works with Windows. So you need to use it with a Windows computer.
To start install the [Tobii Eye Tracking Core Software](https://tobiigaming.com/getstarted/) you can then play around with the suplied software to see how the tracking works. 

To use the eyetracking data in other software you can use:
* Processing library: https://github.com/AugustoEst/gazetrack
* Openframeworks addon: https://github.com/TatsuyaOGth/ofxTobiiEyeX

You can then either use the data in Processing or OpenFrameworks(OF) or sent it from Processing/OF via [OSC](https://en.wikipedia.org/wiki/Open_Sound_Control) to the software of your choice that supports OSC.

For Open Source (but not free) eye tracking take a look here: https://pupil-labs.com/

## Vernier Breath Sensor 
well documented and maintained sensors, in this case a (thorax stretch) breath sensor
https://vernierst.github.io/godirect-examples/python/

## Manus VR

To use Manus VR you need to have a software license to integrate the gloves for example with Unity. At the moment we do not have access to this so we could do not further tests with the device.

## MYO

The possibilities of using a Myo are well documented.
* You can take a look ate the official developer portal here: https://developer.thalmic.com/ (deprecated)
* You can find a simple MYO to OSC tool here: https://github.com/hku-ect/Myo
* You can find the github of the Thalmic Labs Myo here: https://github.com/thalmiclabs

* Update 2024: we succesfully connected Myo via https://github.com/iomz/dl-myo (Dongle-less Myo : Python script)


## Getting in Bitalino data and sending it over OSC

A Python script to get in the Bitalino data, and send it over OSC.

Tested on Mac OS Sierra, and with Python 3.7 and libraries mentioned here:
https://github.com/BITalinoWorld/revolution-python-api

Code from there is updated to work with Python 3.7, and an example + Max OSC receiver example is included.

