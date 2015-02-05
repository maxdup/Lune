Lune
====

a cross-platform music player for Windows, linux and mac aiming to provide the widest possible support of audio formats and the best user experience.

Technologies used
====
python 3 with Qt4 and the VLC api.

Setting up your environment
====

you should have Python3, qt-sdk, Python3-Pyside, pyside-tools and vlclib

next you need to compile qt resources with: sh compile_resources.sh

...and you should be good to run the lune.py

Automated ressource compilling with grunt
====
if you want style files to be automaticly compiled into ressources, you may want to use grunt.

in the root folder, run "npm install -g grunt-cli" and "npm isntall" and you should be good. from now on you can use "grunt shell", to compile resources manually or "grunt watch", to automatically compile resources when a stylesheet is changed.