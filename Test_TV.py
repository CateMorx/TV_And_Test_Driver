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

tv1 = TV()
tv2 = TV()
#Create class Test_TV
class Test_TV:
    #Def for GUI
    def __init__(self, tv1, tv2, GUI):
        self.GUI = GUI
        self.tv1 = tv1
        self.tv2 = tv2

    #Power button
        self.tv1.power_button = tkinter.Button(GUI, text="Power: Off", command=self.toggle_power)
        self.tv1.power_button.grid(row=0, column=0, padx=5, pady=5)

    #Power button of Tv2
        self.tv2.power_button = tkinter.Button(GUI, text="Power: Off", command=self.toggle_power_tv2)
        self.tv2.power_button.grid(row=0, column=1, padx=5, pady=5)

    # Channel Label and Entry
        self.tv1.channel_label = tkinter.Label(GUI, text="Channel of Tv 1")
        self.tv1.channel_label.grid(row=1, column=0, padx=5, pady=5)
        self.tv1.channel_entry = tkinter.Entry(GUI)
        self.tv1.channel_entry.grid(row=2, column=0, padx=5, pady=5)
        self.tv1.channel_enter= tkinter.Button(GUI, text="Enter", command=self.enter_channel)
        self.tv1.channel_enter.grid(row=3, column=0, padx=5, pady=5)

    # Channel Up and Down Buttons
        self.tv1.channel_up_button = tkinter.Button(GUI, text="Channel Up", command=self.channel_up)
        self.tv1.channel_up_button.grid(row=4, column=0, padx=5, pady=5)
        self.tv1.channel_down_button = tkinter.Button(GUI, text="Channel Down", command=self.channel_down)
        self.tv1.channel_down_button.grid(row=5, column=0, padx=5, pady=5)

    # Volume Label and Entry
        self.volume_label = tkinter.Label(GUI, text="Volume")
        self.volume_label.grid(row=6, column=0, padx=5, pady=5)
        self.volume_entry = tkinter.Entry(GUI)
        self.volume_entry.grid(row=7, column=0, padx=5, pady=5)
        self.channel_enter= tkinter.Button(GUI, text="Enter", command=self.enter_volume)
        self.channel_enter.grid(row=8, column=0, padx=5, pady=5)
    # Volume Up and Down Buttons
        self.volume_up_button = tkinter.Button(GUI, text="Volume Up", command=self.volume_up)
        self.volume_up_button.grid(row=9, column=0, padx=5, pady=5)
        self.volume_down_button = tkinter.Button(GUI, text="Volume Down", command=self.volume_down)
        self.volume_down_button.grid(row=10, column=0, padx=5, pady=5)

     # Channel Label and Entry of TV2
        self.tv2.channel_label = tkinter.Label(GUI, text="Channel of TV 2")
        self.tv2.channel_label.grid(row=1, column=1, padx=5, pady=5)
        self.tv2.channel_entry = tkinter.Entry(GUI)
        self.tv2.channel_entry.grid(row=2, column=1, padx=5, pady=5)
        self.tv2.channel_enter= tkinter.Button(GUI, text="Enter", command=self.enter_channel_tv2)
        self.tv2.channel_enter.grid(row=3, column=1, padx=5, pady=5)
    
    # Channel Up and Down Buttons of TV 2
        self.tv2.channel_up_button = tkinter.Button(GUI, text="Channel Up", command=self.channel_up_tv2)
        self.tv2.channel_up_button.grid(row=4, column=1, padx=5, pady=5)
        self.tv2.channel_down_button = tkinter.Button(GUI, text="Channel Down", command=self.channel_down_tv2)
        self.tv2.channel_down_button.grid(row=5, column=1, padx=5, pady=5)

    #Print button
        self.prints = tkinter.Button(GUI, text="Print", command=self.prints)
        self.prints.grid(row=11, column=0, padx=5, pady=5)

        self.number_of_enter_channel_tv1 = 0
        self.number_of_enter_volume_tv1  = 0
        self.number_of_enter_channel_tv2 = 0
        self.number_of_enter_volume_tv2  = 0


#Def for button functions
    #def for power button command
    def toggle_power(self):
        if self.tv1.on:
            self.tv1.turn_Off()
            self.tv1.power_button.config(text="Power: Off")
        else:
            self.tv1.turn_On()
            self.tv1.power_button.config(text="Power: On")

    #def for power button command
    def toggle_power_tv2(self):
        if self.tv2.on:
            self.tv2.turn_Off()
            self.tv2.power_button.config(text="Power: Off")
        else:
            self.tv2.turn_On()
            self.tv2.power_button.config(text="Power: On")
    
    #def for enter channel command
    def enter_channel (self):
        try:
            if not self.tv1.on:
                messagebox.showinfo("Error", "Please turn on Power")
            entry = self.tv1.channel_entry.get()
            if entry:
                entry=int(self.tv1.channel_entry.get()) 
                self.tv1.set_Channel(entry)
                self.number_of_enter_channel_tv1 = 1
            elif not isinstance (entry, int):
                raise TypeError
            else:
                messagebox.showinfo("Error", "Please enter a channel value")
        except:
            messagebox.showerror("TypeError", "Channel must be an integer")


    def enter_channel_tv2 (self):
        try:
            if not self.tv2.on:
                messagebox.showinfo("Error", "Please turn on Power")
            entry = self.tv2.channel_entry.get()
            if entry:
                entry=int(self.tv2.channel_entry.get()) 
                self.tv2.set_Channel(entry)
                self.number_of_enter_channel_tv2 = 1
            else:
                messagebox.showinfo("Error", "Please enter a channel value")
        except ValueError:
            messagebox.showerror("TypeError", "Channel must be an integer")

    #def for channel up command
    def channel_up(self):
        if not self.tv1.on:
             messagebox.showinfo("Error", "Please turn on Power")
        elif self.number_of_enter_channel_tv1 == 0:
            messagebox.showinfo("Error", "Please Enter Your Channel First")
        else: 
            self.tv1.channel_Up()
            self.tv1.channel_entry.delete(0, tkinter.END)
            self.tv1.channel_entry.insert(0, str(self.tv1.get_Channel()))

    #def for channel down command
    def channel_down(self):
        if not self.tv1.on:
             messagebox.showinfo("Error", "Please turn on Power")
        elif self.number_of_enter_channel_tv1 == 0:
            messagebox.showinfo("Error", "Please Enter Your Channel First")
        else: 
            self.tv1.channel_Down()
            self.tv1.channel_entry.delete(0, tkinter.END)
            self.tv1.channel_entry.insert(0, str(self.tv1.get_Channel()))

    #def for channel up command for TV 2
    def channel_up_tv2(self):
        if not self.tv2.on:
             messagebox.showinfo("Error", "Please turn on Power")
        elif self.number_of_enter_channel_tv2 == 0:
            messagebox.showinfo("Error", "Please Enter Your Channel First")
        else: 
            self.tv2.channel_Up()
            self.tv2.channel_entry.delete(0, tkinter.END)
            self.tv2.channel_entry.insert(0, str(self.tv2.get_Channel()))

    #def for channel down command for Tv2
    def channel_down_tv2(self):
        if not self.tv2.on:
             messagebox.showinfo("Error", "Please turn on Power")
        elif self.number_of_enter_channel_tv2 == 0:
            messagebox.showinfo("Error", "Please Enter Your Channel First")
        else: 
            self.tv2.channel_Down()
            self.tv2.channel_entry.delete(0, tkinter.END)
            self.tv2.channel_entry.insert(0, str(self.tv2.get_Channel()))


    #def for enter volume command for Tv2
    def enter_volume (self):
        try:
            if not self.tv.on:
                messagebox.showinfo("Error", "Please turn on Power")
            entry = self.volume_entry.get()
            if entry:
                entry=int(self.volume_entry.get()) 
                self.tv.set_Volume_Level(entry)
                self.number_of_enter_volume_tv1 = 1
            elif not isinstance (entry, int):
                raise TypeError
            else:
                messagebox.showinfo("Error", "Please enter a volume value")
        except:
            messagebox.showerror("TypeError", "Volume must be an integer")

    #def for volume up command
    def volume_up(self):
        if not self.tv.on:
             messagebox.showinfo("Error", "Please turn on Power")
        elif self.number_of_enter_volume_tv1 == 0:
            messagebox.showinfo("Error", "Please Enter Your Volume First")
        else: 
            self.tv.volume_Up()
            self.volume_entry.delete(0, tkinter.END)
            self.volume_entry.insert(0, str(self.tv.get_Volume_Level()))

    #def for volume down command
    def volume_down(self):
        if not self.tv.on:
             messagebox.showinfo("Error", "Please turn on Power")
        elif self.number_of_enter_volume_tv1 == 0:
            messagebox.showinfo("Error", "Please Enter Your Volume First")
        else:
            self.tv.volume_Down()
            self.volume_entry.delete(0, tkinter.END)
            self.volume_entry.insert(0, str(self.tv.get_Volume_Level()))

    #def for print command
    def prints(self):
        if not self.tv.on:
             messagebox.showinfo("Error", "Please turn on Power")
        elif self.number_of_enter_volume_tv1 == 0 or self.number_of_enter_channel_tv1 == 0:
            messagebox.showinfo("Error", "Please Enter Your Volume or Channel First")
        else:
            messagebox.showinfo("Volume and Channel","tv1's channel is "+ str(tv1.channel_entry.get())+ " and volume level is "+ str(self.volume_entry.get()) +"\ntv2's channel is "+ str(tv2.channel_entry.get())+ " and volume level is "+ str(self.volume_entry.get()))


#starts the event loop of the GUI application
GUI = tkinter.Tk()
GUI.title("TV Control Panel")
testTV = Test_TV(tv1, tv2, GUI)
GUI.mainloop()