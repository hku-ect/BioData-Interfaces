# BioData-Interfaces

Here you will find information about different BioData-Interfaces and how you can use them.
The different BioData interface that we are in the process of researching are:

* Bitalino
* Heartlive
* Muse brain-computer interface
* BrainWave brain-computer interface with BrainOSC 
* Myo (See Myo-OSC)
* Webcam for heartbeat detection (webcam pulse detector)
* Eye tracker
* Manus VR

## Using (web)Cam for heartbeat detection

Using https://thearn.github.io/webcam-pulse-detector/ as starting point we researchd how you could use this in a live interactive installation.

* The webcam-pulse-detector works with Python3
* As dependencies you need to install opencv2 and Matplotlib

Using [this](https://github.com/ikbenmacje/webcam-pulse-detector) fork you can also send out the pulse as OSC message.

## Getting in Bitalino data and sending it over OSC

A Python script to get in the Bitalino data, and send it over OSC.

Tested on Mac OS Sierra, and with Python 3.7 and libraries mentioned here:
https://github.com/BITalinoWorld/revolution-python-api

Code from there is updated to work with Python 3.7, and an example + Max OSC receiver example is included.

