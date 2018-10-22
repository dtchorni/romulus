# Romulus - Space apps 2018 Waterloo ON
## Challenge Description
We proposed our own problem combining CSA's challenge in finding Near Earth Objects
from Canada's very own satellite, NEOSSAT. Additionally, we took the concepts from
 NASA's Moon rover mission challenge to plan rover/probe missions to NEO's given their trajectory.
 
 ## Build
 
 1. **Install python3, pip4, imagemagick, git, and SExtractor**

`sudo apt-get install python3 python3-dev python3-pip imagemagick sextractor libxt-dev git build-essential`

2. **Install python libraries:**

`sudo pip3 install scipy pandas numpy pyfits pillow`

3. **Install dep/astroasciidata:**

`sudo  python3 setup.py install`

4. **Install dep/alipy:**

`sudo python3 setup.py install`

5. **Install dep/A-Track/f2n:**

`sudo python3 setup.py install`


## Usage

Running `python3 neoview.py` opens a connection to the Canadian Space Agency's data from the NEOSSAT satellite. 
Running `help` in the dialog will list the few basic commands.
There are several days to choose from. Once you have chosen which data set you like to use, simply call 'use' with
the directory as an argument or call `use` while in the directory. This will download all `*clean.fits` files in the 
input data directory.

<br>

Then use `python3 atrack.py inputs_used` to run an analysis on the data. 
