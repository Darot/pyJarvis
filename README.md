# speechControll

On Ubuntu / Debian (Never tried on a other System!):


Pre-Requirements:

from: https://pypi.python.org/pypi/SpeechRecognition/

The Linux audio stack is pretty fickle. There are a few things that can cause these issues.

First, make sure JACK is installed - to install it, run sudo apt-get install multimedia-jack

You will then want to configure the JACK daemon correctly to avoid that “Cannot allocate memory” error. Run sudo dpkg-reconfigure -p high jackd2 and select “Yes” to do so.

Now, you will want to make sure your current user is in the audio group. You can add your current user to this group by running sudo adduser $(whoami) audio.

Unfortunately, these changes will require you to reboot before they take effect.

After rebooting, run pulseaudio --kill, followed by jack_control start, to fix the “jack server is not running or cannot be started” error.


Short description(follow these commands):

sudo apt-get install flac

sudo apt-get install multimedia-jack
sudo dpkg-reconfigure -p high jackd2 and select “Yes”
sudo adduser $(whoami) audio
pulseaudio --kill
jack_control start

Python Requirements(pip install:
- Python3
- SpeechRecognition: https://pypi.python.org/pypi/SpeechRecognition/


For troubleshooting see.

https://pypi.python.org/pypi/SpeechRecognition/