import datetime
import os
start_time = datetime.datetime.now()

from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


  
print(start_time)
while True:
    if (datetime.datetime.now() - start_time).seconds == 1:
        
       start_time = datetime.datetime.now()
       print(start_time)
       clear()
