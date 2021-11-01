# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:47:42 2018

@author: SchmettowM
"""


STATE = "Go"

while True:
  
  print(STATE)
  key = raw_input("Press a key: ")
  
  # interactive transitionals
  
  if STATE == "Go" and key == " ":
    STATE = "Att"
    continue

  if STATE == "Att" and key == " ":
    STATE = "Stop"
    continue

  if STATE == "Stop" and key == " ":
    STATE = "Prep"
    continue

  if STATE == "Prep" and key == " ":
    STATE = "Go"
    continue 
exit()