# Paulean Marguerette F. Parrish
# BSCPE 1-4
# Create a Python Code for creating the Class named TV and a Test Driver program named TestTV that will create two objects from Class TV

# Class for TV
class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.on = False

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def setChannel(self, channel):
        if self.on:
            self.channel = channel

    def setVolume(self, volume):
        if self.on:
            self.volume = volume

    def channelUp(self):
        if self.on:
            self.channel += 1
            if self.channel > 120:
                self.channel = 1

    def channelDown(self):
        if self.on:
            self.channel -= 1
            if self.channel < 1:
                self.channel = 120

    def volumeUp(self):
        if self.on:
            self.volume += 1
            if self.volume > 7:
                self.volume = 7

    def volumeDown(self):
        if self.is_on:
            self.volume -= 1
            if self.volume < 1:
                self.volume = 1

    def getStatus(self):
        if self.on:
            return "TV is ON"
        else:
            return "TV is OFF"

    def getChannel(self):
        return self.channel

    def getVolume(self):
        return self.volume
