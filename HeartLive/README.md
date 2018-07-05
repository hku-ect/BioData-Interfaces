# HeartLive

About HeartLive
[TODO]

For Windows Users there is an application for the HeartLive, see http://heartlive.nl/downloads that can also send out OSC data (by right-clicking on the heart-icon in the windows-menu and initiate analysing mode with the HeartLive application running and in the foreground pressing ctrl+alt+h).

For other users, the HeartLive is recognised by the computer as an USB-audio interface.

# BasicMax-Patch

heartlive-minimal.maxpat is a simple, minimal Max/MSP script heart that translates the audio signal (via peak and trough analyses) to a mean bpm. 
bpm.maxpat is a max sub patcher that returns a mean bpm and a mean bpm with adaptable sigmoidal function, by default making the more recent bpm-values more important in the averaging.

1. Make sure you select the HeartLive as the input sound card, often recognised as a "Generic USB Audio Device"

2. start audio 

3. peaks and through are detected in the smoothed signal.
Troughs reset peak-detection and vice versa. The peaks and troughs are sent to a ranger sub patch for the range of visualisations. You can set the range manually or by clicking on "3. set range for visualisation".




