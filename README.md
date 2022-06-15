# ScorpionBot 🦂
A Scorpion Robot powered by RPi zero/w.  The sctructure is 3D printed and mechanically assembled. Check out the script files in order to see the servo motor assignments to the legs joints. There are two scripts written in python.

### Script 1 (scorpion.py)
This script defines all the movements and camera features in the tail of the scorpion.  Just call the functions which are pretty much self explaining to move the scorpion around and about.  Feel free to tweak the movement parameters.

### Script 2 (scorpion_socket.py)
This script allows to coonect the scorpion to a remote computer running python and allows to send commands for movements and camera functions.  Again check the script file for the detailed commands. 

####NOTE: If you intend to build it remember to be mindful of the power consumption of the RPi zero.  It may influence the scripts running on it. I will post details of the build somewhere like the raspberryPi developers hub or a website soon if you may be interested in the build.

