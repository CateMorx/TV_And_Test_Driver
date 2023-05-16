#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 6
# Create a Python Code for creating the Class named TV and a Test Driver program named TestTV that will create 
#two objects from Class TV and will produce the following output:
#Tv1's channel is 30 and volume level is 3
#Tv2's channel is 3 and volume level is 2

#Create class TV
class TV:
    #Create def for attributes
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False
    #Create def for Turn on
    def turn_On(self):
        self.on = True
    #Create def for Turn off
    def turn_Off(self):
        self.on = False
    #Create def that retrieves the value of channel
    def get_Channel(self):
        return self.channel
    #Create def for setting channel value
    def set_Channel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel
            return self.channel

    #Create def that retrieves the value of volume
    def get_Volume_Level(self):
        return self.volumeLevel
    #Create def for setting volume value
    def set_Volume_Level(self, volumeLevel):
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel
            return self.volumeLevel
    #Def that increases channel level by 1
    def channel_Up(self):
        if self.on and 1<=self.channel < 120:
            self.channel += 1

    #Def that decreases channel level by 1
    def channel_Down(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    #Def that increases volume level by 1
    def volume_Up(self):
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1
    #Def that decreases volume level by 1
    def volume_Down(self):
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1