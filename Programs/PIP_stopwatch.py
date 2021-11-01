# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:47:42 2018

@author: SchmettowM
"""

STATE = "reset"
while True:
  
  print(STATE)
  key = raw_input("Press a key: ")
  
  # interactive transitionals
  
  if STATE == "reset" and key == " ":
    STATE = "run"
    continue
 
  if STATE == "run" and key == " ":
    STATE = "pause"
    continue
     

  if STATE == "pause" and key == " ":
    STATE = "run"
    continue
 
  if STATE == "run" and key == "r":
    STATE = "reset"
    continue

  if STATE == "pause" and key == "r":
    STATE = "reset"
    continue 

  if key == "x":
    STATE = "Exit"
    continue
    
  if STATE == "Exit":
    break
    
    
exit()