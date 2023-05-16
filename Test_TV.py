#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 6
# Create a Python Code for creating the Class named TV and a Test Driver program named TestTV that will create 
#two objects from Class TV and will produce the following output:
#Tv1's channel is 30 and volume level is 3
#Tv2's channel is 3 and volume level is 2

#Imports necessary modules and elements
import tkinter as tkinter
from tkinter import messagebox
from TV import TV
#Create class Test_TV
class Test_TV:
    tv1 = TV()
    tv2 = TV()
    #Def for GUI
    def __init__(self, GUI):
        self.GUI = GUI
        GUI.title("TV Control Panel")\
        
        self.tv = TV()
        
    #Power button
    # Channel Label and Entry
    # Channel Up and Down Buttons
    # Volume Label and Entry
    # Volume Up and Down Buttons
#Def for button functions