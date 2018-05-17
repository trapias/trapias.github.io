---
layout: post
title: How to install Ghost on your Raspberry Pi
permalink: /blog/How-to-install-Ghost-on-your-Raspberry-Pi
poster: https://ununsplash.imgix.net/reserve/LJIZlzHgQ7WPSh5KVTCB_Typewriter.jpg
tags: node.js ghost raspberrypi
---
Here's how I installed Ghost on my Raspberry Pi with a standard [raspbmc](https://www.raspbmc.com/) installation.

<div class="row">
<div class="col-md-6">
    <img src="{{ page.poster }}" alt="{{title}}" />
</div>
<div class="col-md-6 blog">
    <i><a href="https://unsplash.com/">Image by Unsplash</a></i>
</div>
</div>
Setting it up was not so difficult, but a problem with sqllite3 installation required some additional steps.

As reported in this forum post [https://ghost.org/forum/installation/2583-install-failure-due-to-sqlite3/](https://ghost.org/forum/installation/2583-install-failure-due-to-sqlite3/), you have to...

You need the SQLite development files: 
    apt-get install libsqlite3-dev 
(on Debian/Ubuntu). Also make sure you have build-essential installed. 

So installing Ghost on my Raspberri Pi (Raspbmc) required these steps:

* Install node.js
* Install SqlLite
* Install build-essential and libsqlite3-dev
* Install Ghost

##1. Install node.js

	$ sudo apt-get install node 
    
##2. Install SqlLite3

	$ sudo apt-get install sqlite3 
    
##3. Install build-essential and libsqlite3-dev

	$ sudo apt-get install build-essential 
    $ sudo apt-get install libsqlite3-dev 

Note this will take a while to complete, grab a coffee!

##4. Install Ghost

Install following instructions at https://docs.ghost.org/installation/linux/:

	$ curl -L https://ghost.org/zip/ghost-latest.zip -o ghost.zip $ unzip -uo ghost.zip -d ghost 
    $ cd /path/to/ghost $ npm install --production $ npm start 

To automate running I used forever as documented inhttps://docs.ghost.org/installation/deploy/, and it works perfectly.
