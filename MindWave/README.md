+ Mindwave Mobile to Max/MSP met BrainOSC
With thanks to Matthee Bruin : https://github.com/kinpatsu

download:
- [Thinkgear connector](http://developer.neurosky.com/docs/doku.php?id=thinkgear_connector_tgc)
- [MindWaveMobile Tutorial](http://mindwavemobileplus.neurosky.com/tutorial/)
- [BrainWaveOSC](https://github.com/trentbrooks/BrainWaveOSC)

install:
- install Thinkgear connector
- install MindWaveMobile Tutorial
- un-ZIP BrainWaveOSC download and place map in desired running location

connect Mindwave:
- open Thinkgear connector 
- open MindWaveMobile Tutorial
- turn on Mindwave Mobile(hardware sensor) and wait to connect

- when connected close MindWaveMobile Tutorial and Thinkgear connector

set-up BrainWaveOSC:
- find device name using the terminal with terminal command: ls /dev/*
- device should be called something like this: /dev/cu.MindWaveMobile-DevA

- open settings of BrainWaveOSC: /data/settings.xml
- change default device(COM5) to real device: /dev/cu.MindWaveMobile-DevA
- example:
<value>COM5</value> change to <value>/dev/cu.MindWaveMobile-DevA</value>
- safe settings.xml

- open BrainWaveOSC (check Mindwave Mobile(hardware sensor) is still on(blue light flashing)
- Wait for connection (blue light on)

- Use Max-patch - BrainWaveOSC_receiver.maxpat - to receive data

troubleshoot:
- when connecting a second Mindwave mobile, devicename is set to /dev/cu.MindWaveMobile-DevA-1
