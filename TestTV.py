# Import the class
from TV_Class import TV

# Import asciimatics for design
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, BannerText, Stars, Matrix, Mirage, Wipe
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen

# Ask user for input
Power=input(str("\nTo turn this TV on press 'y' "))
print('\nThe current channel of this TV is (1-120)')
print('The current volume level of this TV is (1-7)')
Channel1=input("\nWhat channel for tv1 do you want? ")
Volume1=input("What volume for tv1 do you prefer? ")
Channel2=input("\nWhat channel for tv2 do you want? ")
Volume2=input("What volume for tv2 do you prefer? ")

def input(screen):
    scenes = []

    effects = [
        Matrix(screen, stop_frame=200),
        Mirage(
            screen,
            FigletText("Loading"),
            screen.height // 2 - 3,
            Screen.COLOUR_GREEN,
            start_frame=100,
            stop_frame=200),
        Wipe(screen, start_frame=150),
        Cycle(
            screen,
            FigletText("Hello"),
            screen.height // 2 - 3,
            start_frame=200)
    ]
    scenes.append(Scene(effects, 250, clear=False))

    effects = [
        BannerText(
            screen,
            Rainbow(screen, FigletText(
                "Welcome, hope you enjoy! Please press x", font='slant')),
            screen.height // 2 - 3,
            Screen.COLOUR_GREEN)
    ]
    scenes.append(Scene(effects))
    screen.play(scenes, stop_on_resize=True)


    effects = [
        Cycle(screen,
              FigletText('Turning the TV on\nPress x to continue', font= 'banner3-d'),
              int(screen.height / 2-8)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects,500)])
Screen.wrapper(input)

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
print(tv1.getStatus(), "tvl's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
print(tv2.getStatus(), "tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())