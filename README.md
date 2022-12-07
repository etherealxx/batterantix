# batterantix
Low battery notification script for antiX 22

sudo apt update
sudo apt-get install git
sudo apt-get install zenity
git clone https://github.com/etherealxx/batterantix
cd batterantix
chmod +x $PWD/*
geany ~/.bashrc
	export PATH=$PATH:/home/ethereal/batterantix
geany /home/ethereal/.desktop-session/startup
	batterantix.py &
sudo geany /etc/rc.local
	batterantixcrit.py &
