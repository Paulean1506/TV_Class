# Test Driver program named TestTV that will create two objects from Class TV
# Import the class
from TV_Class import TV

# Import curses for visual
import curses
import sys
import npyscreen

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
Name=input("\n\033[95mHi! What's your name? ")
Power=input(str("\n\033[94mTo turn this TV on press 'O' "))
print('\n\033[93mThe current channel of this TV is (1-120)')
print('The current volume level of this TV is (1-7)')
Channel1=input("\n\033[96mWhat channel for tv1 do you want? ")
Volume1=input("What volume for tv1 do you prefer? ")
Channel2=input("\n\033[91mWhat channel for tv2 do you want? ")
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
            FigletText("Hello " + Name),
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

# Print the results using curses
def main():
    app = App()
    app.run()

class App(npyscreen.NPSApp):
    def main(self):
        form = npyscreen.FormBaseNew(name = "TELEVISION")
        column_height = terminal_dimensions()[0] - 9
        widget_tv1 = form.add(
            Column,
            name       = "TV 1",
            relx       = 2,
            rely       = 2,
            max_width  = 95,
            max_height = 27
        )
        widget_tv2 = form.add(
            Column,
            name       = "TV 2",
            relx       = 100,
            rely       = 2,
            max_height = 27
        )
        widget_settings = form.add(
            npyscreen.BoxTitle,
            name       = "Information",
            max_height = 15
        )
        widget_settings.resize
        widget_tv1.values  = [tv1.getStatus(), "tvl's channel is:", tv1.getChannel(), "and volume level is:", tv1.getVolume()]
        widget_tv2.values  = [tv2.getStatus(), "tv2's channel is:", tv2.getChannel(), "and volume level is:", tv2.getVolume()]
        widget_settings.values = ['In this program:', '\nThe current channel (1 to 120) of this TV.', '\nThe current volume level (1 to 7) of this TV.', '\nIndicates whether this TV is on/off.', '\nConstructs a default TV object.', '\nTurns on this TV.', '\nTurns off this TV.', '\nSets a new channel for this TV.', '\nSets a new volume level for this TV.', '\nIncreases the channel number by 1.', '\nDecreases the channel number by 1.', '\nIncreases the volume level by 1.', '\nDecreases the volume level by 1.']
        widget_tv1.max_height = 5
        form.edit()

class Column(npyscreen.BoxTitle):
    def resize(self):
        self.max_height = int(0.73 * terminal_dimensions()[0])

class ExitButton(npyscreen.ButtonPress):
    def whenPressed(self):
        sys.exit(0)

def terminal_dimensions():
    return curses.initscr().getmaxyx()

if __name__ == "__main__":
    main()
