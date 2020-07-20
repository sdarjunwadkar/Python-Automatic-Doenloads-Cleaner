# Python-Automatic-Downloads-Cleaner
An Automatic Downloads Cleaner to sort the downloads folder by making directories like Media, Text etc which contain subfolders eg; Media contains subfolders Images, Videos etc. Any file that gets added to downloads folder gets automatically moved to its respective filetype folder. 

This is a downloads cleaner for MAC. This script is inspired and coded with the help of Kalle Hallden - A YouTuber. Following is the link to his channel and video which I referred:
Channel:
https://www.youtube.com/channel/UCWr0mx597DnSGLFk1WfvSkQ
Video:
https://www.youtube.com/watch?v=HcZ3gS1Rgcs

Install Watchdog Library

pip install Watchdog 

Following are the libraries used:
watchdog.observers
watchdog.events
time
os

For MAC users to run this script continuously in background use Automator in MacOS and create a shell script in it. Save it and in System Preferences>Users & Groups>Login Items add this automator created shell script.
 
To use in Windows please change the PATH accordingly.
