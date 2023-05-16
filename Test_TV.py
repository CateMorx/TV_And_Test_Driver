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
        self.volume_up_button = tkinter.Button(GUI, text="Volume Up", command=self.volume_up)
        self.volume_up_button.pack()
        self.volume_down_button = tkinter.Button(GUI, text="Volume Down", command=self.volume_down)
        self.volume_down_button.pack(pady=10)

        self.prints = tkinter.Button(GUI, text="Print", command=self.prints)
        self.prints.pack()

        self.number_of_enter_channel = 0
        self.number_of_enter_volume = 0

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
        try:
            if not self.tv.on:
                messagebox.showinfo("Error", "Please turn on Power")
            entry = self.channel_entry.get()
            if entry:
                entry=int(self.channel_entry.get()) 
                self.tv.set_Channel(entry)
                self.number_of_enter_channel= 1
            elif not isinstance (entry, int):
                raise TypeError
            else:
                messagebox.showinfo("Error", "Please enter a channel value")
        except:
            messagebox.showerror("TypeError", "Channel must be an integer")

    #def for channel up command
    def channel_up(self):
        self.tv.channel_Up()
        self.channel_entry.delete(0, tkinter.END)
        self.channel_entry.insert(0, str(self.tv.get_Channel()))

    #def for channel down command
    def channel_down(self):
        if not self.tv.on:
             messagebox.showinfo("Error", "Please turn on Power")
        elif self.number_of_enter_channel== 0:
            messagebox.showinfo("Error", "Please Enter Your Channel First")
        else: 
            self.tv.channel_Down()
            self.channel_entry.delete(0, tkinter.END)
            self.channel_entry.insert(0, str(self.tv.get_Channel()))

    #def for enter volume command
    def enter_volume (self):
        if not self.tv.on:
             messagebox.showinfo("Error", "Please turn on Power")
        elif self.number_of_enter_channel== 0:
            messagebox.showinfo("Error", "Please Enter Your Channel First")
        else:
            entry=int(self.volume_entry.get()) 
            self.tv.set_Volume_Level(entry)
            self.number_of_enter_volume= 1

    #def for volume up command
    def volume_up(self):
        self.tv.volume_Up()
        self.channel_entry.delete(0, tkinter.END)
        self.channel_entry.insert(0, str(self.tv.get_Volume_Level()))

    #def for volume down command
    def volume_down(self):
        self.tv.volume_Down()
        self.channel_entry.delete(0, tkinter.END)
        self.channel_entry.insert(0, str(self.tv.get_Volume_Level()))

    def prints(self):
         messagebox.showinfo("Volume and Channel","tv1's channel is "+ str(self.channel_entry.get())+ " and volume level is "+ str(self.volume_entry.get()))
#starts the event loop of the GUI application
GUI = tkinter.Tk()
GUI.title("TV Control Panel")
testTV = Test_TV(GUI)
GUI.mainloop()