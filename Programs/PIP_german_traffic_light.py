# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:47:42 2018

@author: SchmettowM
"""

from time import time


STATE = "Stop"
timestamp = time()

while True:
  
  print(STATE)
#  key = raw_input("Press a key: ")
  
  # interactive transitionals
  
  if STATE == "Stop" and time() - timestamp > 3:
    STATE = "Prep"
    timestamp = time()
    continue
 
  if STATE == "Prep" and time() - timestamp > 1:
    STATE = "Go"
    timestamp = time()
    continue


  if STATE == "Go" and time() - timestamp > 3:
    STATE = "Att"
    timestamp = time()
    continue

  if STATE == "Att" and time() - timestamp > 1:
    STATE = "Stop"
    timestamp = time()
    continue
    
    
exit()