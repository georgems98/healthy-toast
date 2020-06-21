# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 18:07:09 2020

Program to help healthy working habits - reminders are displayed using 
Windows 10 toast notifications.

The reminders are:
    > Every 30 minutes look away from the screen for 30 seconds.
    > Every hour stand up for a few minutes

@author: georgems
"""

import sched
import time
from win10toast import ToastNotifier


# Initialise toaster and scheduler
toaster = ToastNotifier()
s = sched.scheduler(time.time, time.sleep)


# 30 minute notification
def notify_eyes(sc):
    """
    Display the "rest your eyes" notification and recursively schedule the 
    next notification.
    
    N.B. this is set to occur 30 mins after initial program run, and then 
    every 60 mins (since the "stand up" notification occurs hourly and 
    encompasses "rest your eyes").
    
    Input is the amount of time (in seconds) to wait before displaying the 
    next notification.
    """
    
    toaster.show_toast("Rest your eyes!", "Look away from the screen for 30 seconds.")
    
    # Re-schedule event for 3600 secs later
    s.enter(3600, 2, notify_eyes, (sc,))
    
    # Notify when 30 seconds is up
    time.sleep(30)
    toaster.show_toast("Back to work!", "That was 30 seconds.")


# Hourly notification
def notify_stand(sc):
    """
    Display the "stand up" notification and recursively schedule the next
    notification.
    
    Input is the amount of time (in seconds) to wait before displaying the 
    next notification.
    """
    
    toaster.show_toast("Stand up!", "Get out of the chair for a few minutes.")
    
    # Re-schedule event
    s.enter(3600, 1, notify_stand, (sc,))    
    
    
# Schedule first instances
s.enter(1800, 2, notify_eyes, (s,))
s.enter(3600, 1, notify_stand, (s,))    

s.run()
