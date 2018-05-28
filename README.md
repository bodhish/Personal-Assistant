# Personal Assistant 
### A mix of Google Assistant and Google Image Vision

“Personal Assistant “the word itself means assistant working exclusively for one particular person. The major purpose of any automation system or artificial system is to reduce human labour, effort, time and errors due to his/her intelligence. The major goal of this project is to design and implement an Integrated Virtual Personal Assistant using IOT, which gives the ability to perform task or service for an individual. These tasks or may be services are based on user input, on location and also the ability to access information from variety of online sources.

## 1. Hardware and Software Requirments
The system proposed here is a multifunctional Integrated virtual assistant based on field of artificial intelligence using google assistant and google cloud vision for image recognition. The hardware set up to build the robot is very simple .The hardware requirements for the system are as follows.

### 1.1 Hardware Required
Raspberry Pi, Server Motors, SD Card, Power Supply, Raspberry Pi Camera, Ethernet Cable, Connecting wires, Audio jack, Speakers, Mike

### 1.2 Software Stack
Python, Raspbian (Raspberry OS), Google Assistant SDK, IFTTT, Ngrok, Flask, Google cloud vision API, Google developer account

## 2. Installation
The system runs of raspbian OS, we are using google cloud vision for image regignition and processing which is suplimented with google assistant sdk for voice command processing. The system runs the python the program using flask server. IFFT acts as the medium of connection between google assistant and flask server. Ngork is used to expose the local server online for tunneling processes.

### 2.1 Raspbian OS
Raspbian is a Debian-based computer operating system for Raspberry Pi. There are several versions of Raspbian including Raspbian Stretch and Raspbian Jessie. Since 2015 it has been officially provided by the Raspberry Pi Foundation as the primary operating system for the family of Raspberry Pi single-board computers.[16] Raspbian was created by Mike Thompson and Peter Green as an independent project.[17] The initial build was completed in June 2012.[18] The operating system is still under active development. Raspbian is highly optimized for the Raspberry Pi line's low-performance ARM CPUs.
Using NOOBS is the easiest way to install Raspbian on your SD card. To get hold of a copy of NOOBS, The steps are listed below:
 
Download NOOBS by clicking on the Noobs icon Fig 7.1. The simplest option is to download the zip archive of the files. Extract the downloaded files on to the SD Card and eject the SD card. 
Once the files have been copied over, insert the micro SD Card into your Raspberry Pi, and plug the Pi into a power source. You will be offered a choice as shown in fig 7.2, when the installer has loaded. You should check the box for Raspbian, and then click Install.
 
Click Yes at the warning dialog, and then sit back and relax. It will take a while, but Raspbian will install. Boot the Raspbeery Pi to use the Raspbian OS
