# Import the class
from TV_Class import TV

# Create the first TV object
tv1 = TV()
tv1.turnOn()
tv1.setChannel(30)
tv1.setVolume(3)

# Create the Second TV object
tv2 = TV()
tv2.turnOn()
tv2.setChannel(3)
tv2.setVolume(2)

# Print the results
print(tv1.getStatus(),"tvl's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
print(tv2.getStatus(),"tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())