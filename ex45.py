#Import all the external functions from the respective modules
from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("I still don't understand what this is doing here")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()

class Death(Scene):

    quips = ["You are dead",
            "Capiche",
            "Bye bye asshole"]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class Casino(Scene):
    def enter(self):
        print(dedent(""" You are in the Casino trying to rob the vaults.
        There are 3 guards. You have a small micro gun. What do you do?
        a. Try to shoot the guards and rob the place.
        b. Sneak to the back
        c. Try to count cards and try to be smart.
        Pick a letter"""))
        choice = input('> ')
        if choice == 'a':
            print(dedent(""" Dumbass, you got shot. You watch too many movies"""))
            return 'death'
        elif choice == 'b':
            print(dedent(""" Smart, you get to the back. Crack the safe
            and fill your bag with money. You get into a van and start driving."""))
            return 'heist'
        else:
            print(dedent("""You earn a little money and lose it all when you loose concentration.
            Then you go home empty handed"""))
            print(dedent("Loser"))
            exit(0)
class Heist(Scene):
    def enter(self):
        print(dedent(""" You drive really fast but the cops are chasing. What do you do?
        a. High speed chase.
        b. Alleyway, and run
        c. Try to surrender.
        Pick a letter"""))
        choice = input('> ')
        if choice == 'a':
            print(dedent(""" You watch too many movies. They shoot you down"""))
            return 'death'
        elif choice == 'b':
            print(dedent(""" Smart, you get to an alleyway and hide. They lose you."""))
            return 'home'
        else:
            print(dedent("""You go to jail. Then later on break out of jail. Go to
            Mexico. Morgan Freeman joins you later"""))
            print(dedent("""You shouldn't really steal you know."""))

class Home(Scene):
    def enter(self):
        print(dedent(""" You pour yourself some lemonade and start
        counting the money. Then you realize they are all fucking counterfeit bills.
        Looooooser"""))
        exit(0)

class Map(object):
    scenes = {
    'casino': Casino(),
    'heist': Heist(),
    'home': Home(),
    'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('casino')
a_game = Engine(a_map)
a_game.play()
