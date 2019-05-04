# Romulus - Space apps 2018 Waterloo ON
## Challenge Description
We proposed our own problem combining CSA's challenge in finding Near Earth Objects (NEO's)
from Canada's very own satellite, NEOSSAT. Additionally, we took the concepts from
 NASA's Moon rover mission challenge to plan rover/probe missions to NEO's given their trajectory.
 
 ## Build
 
Run the provided script on linux: `sudo setup_linux.sh`

## Usage

Running `python3 neoview.py` opens a connection to the Canadian Space Agency's data from the NEOSSAT satellite. 
Running `help` in the dialog will list the few basic commands.
There are several days to choose from. Once you have chosen which data set you like to use, simply call 'use' with
the directory as an argument or call `use` while in the directory. This will download all `*clean.fits` files in the 
input data directory.

<br>

Then, in the `dep/A-Track` directory, use `python3 atrack.py inputs_used` to run an analysis on the data. 
