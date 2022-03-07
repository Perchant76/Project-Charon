![cmd_fuM5cfm7kK](https://user-images.githubusercontent.com/63096336/157034635-b058306a-6a8e-4c46-b68c-c4f42d6d1e54.png)

# Project-Charon
Anonymous chatting app using tor. You can chat with your friends anonymously. 

How to set up this private server:
(this  is tutorial for complete noobs)
Server setup:
CASUAL SETUP WITHOUT TOR
download the file for linux use git clone
`git clone https://github.com/Perchant76/Project-Charon`
change host to your IP.
change port to whatever you want but I would recommend something in this range: `1000-99999`

ANONYMOUS SETUP WITH TOR

SERVER SETUP:
download the file or if youre using linux use git
`git clone https://github.com/Perchant76/Project-Charon`
IF are you are using Linux server make sure you have tor installed on your device
Debian/Ubuntu:
`sudo apt-get install tor`
Arch:
`sudo pacman -S tor`
edit server.py file:
I would recomend to use custom port for your server bcs lot of servers are getting scanned everyday and some ports are well known :D
As port number you can use something in this range: `1000-99999`

TOR SETUP:

`nano /etc/tor/torrc`
look for `########################### This is section is just for location-hidden services ###`
here change this:
`#HiddenServiceDir /var/lib/tor/hidden_service/`
`#HiddenServicePort 80 127.0.0.1:80`
to this
`HiddenServiceDir /var/lib/tor/hidden_service/`
`HiddenServicePort <custom-port> 127.0.0.1:<custom-port>`
RUN THE TOR SERVICE:
`sudo tor`
if we want to stop this service just use `ctrl+c` or if its running in background use: 
`pidof tor`
copy id and use kill to kill the process:
`sudo kill <id>`
now open new screen/terminal and start server `python3 server.py`
Have fun!!!

Client setup:

Linux:
`git clone https://www.github.com/Perchant76/Project-Charon`
Windows:
just click on the `code` button and `Download ZIP`
Mac OS:
`git clone https://www.github.com/Perchant76/Project-Charon`
!!!Dont share client.py with random people.!!! Reason for that is that the IP of server is not hidden and someone experieced can do malicious stuff with your or the server IP.
If the server is running without tor just change the `127.0.0.1` to IP of the server.
If using the tor version change `127.0.0.1` to  
Use PyInstaller and encode it to .exe
`py -m PyInstaller client.py`
