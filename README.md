# Lucy AI Assistant

This is a project based on ML (Machine Learning) which automates your entire pc simply by your voice commands.

The program performs any of the mentioned specified tasks according to the input voice command:

- Automates entire Whatsapp
- Automates entire Chrome
- Automates entire Youtube
- Plays any Music of your choice
- Clarifies doubts related to education
- Specifies current temperature
- Specifies current date, day and time
- Takes screenshot
- Captures photos and videos
- Gives daily updates of top news
- Tells jokes and facts
- Displays current location
- Navigates to any location on maps
- Increase or decrease volume
- Increase or decrease brightness
- Gives the battery status of your pc
- Shutdown 
- Restart
- Remembers any note and remainds whenever asked
- Gives internet speed
- Downloads youtube videos
- Opens C drive, D drive, E drive, F drive
- Sets alarm
- Security system

The security system consists of two features

- Face Recognition (The program firstly tries to detect the user's face for verification)
- Password (If the user authentication fails then the user needs to enter the correct password to get access and use it)

After the security system is cracked, the user can access the program by giving any of the commands according to the above mentioned features and the task is performed automatically.

Before running the program, set your face for verification. Follow the below steps:

- Run sample generator.py file, which collects the sample images for verification and stores in the samples folder.
- Now, run Model Trainer.py file, which trains the collected sample and creates a training file in trainer folder.
- And finally you are done setting up your face as a password. 

Follow the below steps to run the Lucy program:   

- Install all the required packages present in the requirements.txt file.
- Enter API key of wolframalpha on line 37 and on line 375  
- Run the script.py file
- To start the project say "Wake up" or "hey Lucy"
- Then, verify by face or password and give commands.
- To exit the project, say "Sleep" or "you need a break"

The project will again get started by a command "Wake up" or "hey Lucy".

For input commands and password, refer the exe() and security() funtion in Lucy.py file. 
