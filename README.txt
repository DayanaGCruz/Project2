Dayana Gonzalez Cruz 
CST-305: Principles of Modeling
WF1100A Citro
Project 2
This read me will show to how to set up your computer to run the Project1.py program. 

How to install and run Runge-Kutta.py:

Install Linux subserver throught terminal commands
- Open terminal
- Install Wsl
	- Enter wsl --install into terminal
- Launch Ubuntu
	- Go to start menu
	- Search "Ubuntu" and click on result 
- Set Username and Password following terminal prompts
- Update Ubuntu
	- Enter in terminal: sudo apt update
Ubuntu 20.04 and forward come with python3 installed
- Check python version
	- Enter in terminal: python3 -V
- Install pip, a package manager for python
	- Enter in terminal: sudo apt install -y python3-pip
- Install numpy, matplotlib, and scipy
	-Enter in terminal: 
	- pip install numpy
	- pip install matplotlib
	- pip install scipy
- Go to file explorer
- Go Linux > Ubuntu > home > yourusername >
- Create a folder for your python files (e.g. Python_Files)
- Move or Paste Project1.py inside
__________________________________________________________________________ Run Program Here

Run Program: 
- Launch Ubuntu from start menu or shortcut
- Enter in terminal:
	- cd YourFolderName 
	(e.g. cd Python_Files)
	- python3 Runge-Kutta.py
	
Use program:
	- Follow input prompts:
	- Enter 1 to see graphical representation of RK4 method solutions
	- Enter 2 to see graphical representation of odeint method solutions
	- Enter 3 to see both
	- Enter 0 or other to exit
View graphical representation of ODE solutions!
Close graph and re-enter - python3 Runge-Kutta.py command in console to see another.