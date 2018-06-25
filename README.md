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


### 2.2 Google Image Vision
We use Google Cloud Vision on the Raspberry Pi to take a picture with the Raspberry Pi Camera and classify it with the Google Cloud Vision API. The first step is to set up a Google Cloud Account. You can create an account here with either your Google or Gmail login. Google offers the first 60 days for free. Create a new project with the required name. You will need to enable billing for your account (you won’t be charged).  Go to the Cloud Platform Console. Select the project “ProjectName” and click the hamburger in the upper left hand corner of the page, Then enable the API.  

Now we want to get a JSON key to put on our Raspberry Pi.  This JSON key will handle all the authentication to use our Google Cloud Account.  Instead of a password, we can use the file to authenticate our account on the Raspberry Pi. Create a service account key and autherise the account and create a role.  Give it full access, so select “Project” and “Owner” to give the Pi Full access to all resources.
Next, upgrade Pip.  Pip is a package manager for python language installations.
Note, you should have Pip installed (it comes installed on Raspbian for Robots); if you don’t upgrade, you will get an error on installation!
  	`sudo pip install --upgrade pip`       				 			
 	`sudo apt-get install libjpeg8-dev` 				 							
Next, install Google API Python Client.   Again in the command line, run:
 	`sudo pip install --upgrade google-api-python-client`		 			  
Next, install Python Imaging Library.  Again in the command line, run:
 	`sudo pip install --upgrade Pillow`  						
Install Python Picamera:
	`sudo apt-get install python-picamera`						 	
Turn on Super User.  In the command line, type the command “su”:
 	`su` 										
You’ll be prompted for your password; this is the password you used to login to your Raspberry Pi. In the home directory, we will make the JSON file available to any application we’re running.  Run the command:
 	`export GOOGLE_APPLICATION_CREDENTIALS=filename.json`	
Be sure to substitute your JSON filename in this command with the name of the file you have on your Raspberry Pi.


First, we’ll try to get the Raspberry Pi to detect the Raspberry Pi Logo.  We’ll use the big Raspberry Pi label on the Raspberry Pi Box.  Set the Pi box about 1 ft from the camera.  We’ll be propping up the camera with a Raspberry Pi Robot, the GoPiGo.  It holds the camera in place with the acrylic body, and we will use it later for some fun projects!
You might want to take a test picture to make sure the label is visible.  In the command line, run
 	`raspistill -o cam.jpg` 								
We’ll go into super user mode on the Pi.
 	`sudo su`									
We’ll make our JSON credentials available.  In the command line, type:
 	`export GOOGLE_APPLICATION_CREDENTIALS=filename.json`	
And now, in the example directory, run:
 	`python camera-vision-logo.py`						
You should get “Raspberry Pi” back, your setup is complete.

7.3	Google Assistant Library
The Google Assistant Library for Python is a turnkey solution for anyone who wants to quickly integrate the Assistant into a prototype device. The library is written in Python and is supported on popular prototyping devices such as the Raspberry Pi 3.
A Google Cloud Platform project, managed by the Actions Console, gives your device access to the Google Assistant API. The project tracks quota usage and gives you valuable metrics for the requests made from your device. To enable access to the Google Assistant API, do the following: 
1.	Open the Actions Console.
2.	Click on Add/import project.

3.	To create a new project, type a name in the Project name box and click CREATE PROJECT.
4.	Click the Device registration box.
5.	Enable the Google Assistant API on the project you selected (see the Terms of Service). You need to do this in the Cloud Platform Console.
In order for the Google Assistant to respond to commands appropriate to your device and the given context, the Assistant needs information about your particular device. You provide this information, which includes fields like device type and manufacturer, as a device model. You can think of this model as a general class of device - like a light, speaker, or toy robot.
This information is then accessible to the Google Assistant and is associated with your Actions Console project. No other projects have access to your model and device information. After regestration create model and regester the device, download the credentials.json file and store it in the Raspberry Pi
Make sure this file is located in /home/pi. Use a Python virtual environment to isolate the SDK and its dependencies from the system Python packages.
Install Python 3 by entering the following commands
 	sudo apt-get update								 
 	sudo apt-get install python3-dev python3-venv				
 	python3 -m venv env 								
 	env/bin/python -m pip install --upgrade pip setuptools wheel 		
Acivate the python virtual environment by entering the foolwing command
 	source env/bin/activate 							
Download the the Google Assistant SDK package that contains all the code required to get the Google Assistant running on the device.
Install the package's system dependencies:
 	sudo apt-get install portaudio19-dev libffi-dev libssl-dev libmpg123-dev	
 	python -m pip install --upgrade google-assistant-library			
 	python -m pip install --upgrade google-assistant-sdk[samples] 		

Install or update the authorization tool: 	
 	python -m pip install --upgrade google-auth-oauthlib[tool] 				
Generate credentials to be able to run the sample code and tools. Reference the JSON file you downloaded in a previous step; you may need to copy it the device. Do not rename this file.
 	google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype\--scope https://www.googleapis.com/auth/gcm\--save --headless --client-secrets /path/to/credentials.json		
Copy the URL and paste it into a browser (this can be done on any machine). The page will ask you to sign in to your Google account. Sign into the Google account that created the developer project in the previous step. After you approve the permission request from the API, a code will appear in your browser, such as "4/XXXX". Copy and paste this code into the terminal to activate. 
When the instaltion process is over you can run the code by entering the following command
 googlesamples-assistant-hotword --project_id my-dev-project --device_model_id my-model    
where “my-dev-project” is the project id you have specifed while regestring and “my-model” is the name of your model.
7.4 	Flask
Flask is a micro web framework written in Python and based on the Werkzeug toolkit and Jinja2 template engine. It is BSD licensed. The latest stable version of Flask is 1.0 as of April 2018.[19] Flask is called a micro framework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools. Extensions are updated far more regularly than the core Flask program.[20]


For for system-wide installation run  pip with root privileges:
 	sudo pip install Flask								
7.5 	Ngrok
ngrok creates a tunnel from the public internet to a port on your local machine. You can give this URL to anyone to allow them to try out a web site you're developing without doing any deployment. It captures all traffic through the tunnel. It displays information about the HTTP traffic for your inspection. Raw request/response bytes, parsed headers and form data, JSON/XML syntax checking and more are included. It can also replay requests[21].
By default, ngrok will use ngrok.com as a third-party relay. This service is provided at no-cost and without registration but it is possible to get additional features by signing up in the service (which is pay-as-you-want kind). However, it is possible to setup and use its own server. This package installs the client part of ngrok. It can be used directly with ngrok.com service or with your own server if you install the ngrok-server package.
Download the single binary with zero run-time dependencies, unzip ngrok from a terminal with the following command. 
 	unzip /path/to/ngrok.zip 								
Running this command will add your account's authtoken to your ngrok.yml file. This will give you more features and all open tunnels will be listed here in the dashboard.
 	./ngrok authtoken 2sMXEyU67vG9DTBNepgFp_5o5GaTrNhuLWHuesEFewX  
To start a HTTP tunnel on port 80
 	./ngrok http 80										
7.6 	IFFT
If This Then That, also known as IFTTT, is a free web-based service to create chains of simple conditional statements, called applets. An applet is triggered by changes that occur within other web services such as Gmail, Facebook, Telegram, Instagram, or Pinterest. For example, an applet may send an e-mail message if the user tweets using a hashtag, or copy a photo on Facebook to a user's archive if someone tags a user in a photo.

In addition to the web-based application, the service runs on iOS and Android. In February 2015, IFTTT renamed their original application to IF, and released a new suite of apps called Do which lets users create shortcut applications and actions.[22] As of 2015, IFTTT users created about 20 million recipes each day.[23] All of the functionalities of the Do suite of apps have since been integrated into a redesigned IFTTT app.
