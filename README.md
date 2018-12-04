# audio-scheduler
### A small python program to randomly play audio files (in .wav format) to multiple outputs on a Raspberry Pi
### If you connect a motion sensor (or whatever else you want) it alters the playback frequency based on detected motions (more detections -> faster frequency

This is a work in progress! There are very obvious issues that need to be (and will get) improved, such as:
- fixed naming of folders and channels
- no proper stopping method
- incomplete instructions :-)

## Usage: 

### Prerequisites:
1. I made this to work on a RaspberryPi with an external USB sound card. It has not been tested on anything else.
2. Set up and test your sound card.
3. Make sure you have four (virtual) stereo sound channels named Stereo1, Stereo2, Stereo3 and Stereo4. I did this by editing "asound.conf" as explained here: https://wiki.archlinux.org/index.php/Advanced_Linux_Sound_Architecture/Configuration_examples
4. Install aplay if it isn't present
5. Connect a motionSensor to a Power pin , a Ground pin and it's output to GPIO pin 23. You can skip this if you want but since the frequency of the triggered audio files is altered by this, as of now, your playback rate will go down to starting one file per channel roughly every 30sec (if that channel is free). 
6. If you want, connect a LED to GIO Pin 17 and a GND pin to receive a visual signal whenever a detection event is triggered

### Installation & Start:
1. Make sure you have Python 3.5 installed
2. Pull the repository into a directory on your device.
3. Put the .wav files that you want to use into the subfolders a, b, c & d 
4. run startup.sh
