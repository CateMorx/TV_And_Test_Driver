#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 6
# Create a Python Code for creating the Class named TV and a Test Driver program named TestTV that will create 
#two objects from Class TV and will produce the following output:
#Tv1's channel is 30 and volume level is 3
#Tv2's channel is 3 and volume level is 2

#Imports necessary modules and elements
import tkinter
from tkinter import messagebox
from TV import TV
#Create class Test_TV
class Test_TV:
    tv1 = TV()
    tv2 = TV()
    #Def for GUI
    def __init__(self, GUI):
        self.GUI = GUI
        
        self.tv = TV()

    #Power button
        self.power_button = tkinter.Button(GUI, text="Power: Off", command=self.toggle_power)
        self.power_button.pack(pady=10)

    # Channel Label and Entry
        self.channel_label = tkinter.Label(GUI, text="Channel")
        self.channel_label.pack()
        self.channel_entry = tkinter.Entry(GUI)
        self.channel_entry.pack()
        self.channel_enter= tkinter.Button(GUI, text="Enter", command=self.enter_channel)
        self.channel_enter.pack(pady=10)
    
    # Channel Up and Down Buttons
        self.channel_up_button = tkinter.Button(GUI, text="Channel Up", command=self.channel_up)
        self.channel_up_button.pack()
        self.channel_down_button = tkinter.Button(GUI, text="Channel Down", command=self.channel_down)
        self.channel_down_button.pack(pady=10)

    # Volume Label and Entry
        self.volume_label = tkinter.Label(GUI, text="Volume")
        self.volume_label.pack()
        self.volume_entry = tkinter.Entry(GUI)
        self.volume_entry.pack()
        self.channel_enter= tkinter.Button(GUI, text="Enter", command=self.enter_volume)
        self.channel_enter.pack(pady=10)
    # Volume Up and Down Buttons


#Def for button functions
    #def for power button command
    def toggle_power(self):
        if self.tv.on:
            self.tv.turn_Off()
            self.power_button.config(text="Power: Off")
        else:
            self.tv.turn_On()
            self.power_button.config(text="Power: On")
    
    #def for enter channel command
    def enter_channel (self):
        entry=int(self.channel_entry.get()) 
        self.tv.set_Channel(entry)

    #def for channel up command
    def channel_up(self):
        self.tv.channel_Up()
        self.channel_entry.delete(0, tkinter.END)
        self.channel_entry.insert(0, str(self.tv.get_Channel()))

    #def for channel down command
    def channel_down(self):
        self.tv.channel_Down()
        self.channel_entry.delete(0, tkinter.END)
        self.channel_entry.insert(0, str(self.tv.get_Channel()))

    #def for enter volume command
    def enter_volume (self):
        entry=int(self.volume_entry.get()) 
        self.tv.set_Volume_Level(entry)
#starts the event loop of the GUI application
GUI = tkinter.Tk()
GUI.title("TV Control Panel")
testTV = Test_TV(GUI)
GUI.mainloop()