# Import the class
from TV_Class import TV

# Ask user for input
Power=input(str("\nTo turn this TV on press 'y' "))
print('\nThe current channel of this TV is (1-120)')
print('The current volume level of this TV is (1-7)')
Channel1=input("\nWhat channel for tv1 do you want? ")
Volume1=input("What volume for tv1 do you prefer? ")
Channel2=input("\nWhat channel for tv2 do you want? ")
Volume2=input("What volume for tv2 do you prefer? ")

# Create the first TV object
tv1 = TV()
tv1.turnOn()
tv1.setChannel(Channel1)
tv1.setVolume(Volume1)

# Create the Second TV object
tv2 = TV()
tv2.turnOn()
tv2.setChannel(Channel2)
tv2.setVolume(Volume2)

# Print the results
print("tvl's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())