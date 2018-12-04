# audio-scheduler
### A small python program to schedule playing of lists of audio files (in .wav format) to multiple outputs on a Raspberry Pi

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

### Installation & Start:
1. Make sure you have Python 3.5 installed
2. Pull the repository into a directory on your device.
3. Put the .wav files that you want to use into the subfolders a, b, c & d 
4. run startup.sh
