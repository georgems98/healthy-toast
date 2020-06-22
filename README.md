# Healthy Toast

A program to help keep healthy working habits - reminders are displayed using Windows 10 toast notifications.

The reminders are:
* every 30 minutes look away from the screen for 30 second;
* every hour stand up for a few minutes.


## Getting started
Install the win10toast library to the desired Python environment. The program can be called easily with the following batch file:

```
@<directory location of Python executable> <directory location of toaster.py file> %*
pause
```

It is also possible to call the program without a cmd window opening by changing python.exe for pythonw.exe in the above batch file.


### Prerequesites
The package_list.txt file contains all packages installed into the working environment and which versions are used. The key libraries are:
* sched
* time
* win10toast
