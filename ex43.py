#basic imports for the game, dedent is to strip whitespace from beginning of
#strings
#dedent: This can be used to make triple-quoted strings line up with the left edge of the display, while still presenting them in the source code in indented form.
#Explain how returning the next word works

#Each scene- child class returns the next scene,

from sys import exit
from random import randint
from textwrap import dedent

#Place holder for commonalities of all scenes. Base scene
class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)
#You pass an instance of Map when you call Engine
#I still dont fully get this
class Engine(object):

    #The init method of the class Engine takes in the param scene_map
    #This is just the map instance as seen in the body at the end
    #a_map in the body code is the scene_map
    def __init__(self, scene_map):
        self.scene_map = scene_map
        #Method play of Engine class takes only self as a param. so that's why take as .play()
#******************************************************************************************************************
    def play(self):
        print(">>> play")
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
#If the current scene isn't the final one, this is what happens

        print("^^^ before while: current scene = ", current_scene, "last_scene = ", last_scene)
        while current_scene != last_scene:
            print("^ top of while: current scene = ", current_scene, "last_scene = ", last_scene)
            #This is where it is run 
            next_scene_name = current_scene.enter()
            #Here the jump to the next scene takes place
            #IMHO, a very convoluted way of doing this really
            #So essentially, you set the current scene here, which is set to the next scene at the top of
            #the loop
            current_scene = self.scene_map.next_scene(next_scene_name)
            print("^ end of while: current scene = ", current_scene, "last_scene = ", last_scene, "next_scene_name = ", next_scene_name)

        #be sure to print out the last scene
        current_scene.enter()
#*********************************************************************************************************************


class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud.... If she were smarter.",
        "Such a looser.",
        "I have a small puppy that's better at this.",
        "You're worse than your dad's jokes."
            ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):
    #This enter method inside each scene is what counts, this overrides the previous ones
    def enter(self):
        print(dedent("""
            The Gothons of planet Percal #27 have invaded your ship and destroyed your
            entire crew. You are the last survicing member and it is your last mission
            to get he neutron destruct bomb from the Weapons Armory, put it in the bridge,
            and blow the ship up after getting into an escape pod.

            You are running down the central corridor to the Weapons Armory when a Gothon jumps
            out, red scaly skin, dark grimy teeth, and evil clown costume flowing around his hate filled body.
            He's blocking the door to the Armory about to pull a weapon to blast you.
        """))


        action  = input("Please enter the letter you prefer\na: shoot!\nb: dodge!\nc: tell a joke\n> ")

        if action == 'a':
            #This is a fight scene, really has no effect but this is combat I guess
            print(dedent("""" You get into a gun fight with this dastardly Gothon """))
            print(dedent("The gothon shoots: blam"))
            for i in range(3):
                shoot = input("Insert a shoot sound:\n> ")
                if shoot == 'Kablam':
                    print("Kablam, Major destruction. You are a born fighter")
                    break
                else:
                    print("Gothon shoots: blam")
            print(dedent("""
                  Gothon crown costume is flowing and moving around his body, which throws off his aim.
                  Your laser hits his costume but misses him entirely. This completely ruins his
                  brand new costume his mother bought him, which makes him fly into an insane range and
                  blast you repeatedly in the face until you are dead. Then he eats you.
            """))
            #The next scene is returned at every step
            return 'death'

        elif action == 'b':
            print(dedent("""
                    Like a world class boxer you dodge, weave, slip and slide right
                    as the Gothon's blaster cranks a laser past your head. In the
                    middle of your artful dodge your foot slips and you bang your head on
                    the metal wall and pass out. You wake up shortly after only to
                    die as the Gothon stomps on your head and eats you.
            """))
            return 'death'

        elif action == 'c':
            print(dedent("""
                  Lucky for you they made you learn Gothon insults in the academy.
                  You tell the one Gothon joke you know:fagk glkkl lkjgapoi vnafl ipqjre
                  ajflfn glr agb nrg gur. The Gothon stops, tries to hold back laughter, unltimately
                  to only burst out in a fit of laughter and can't move. While he's running you run out and
                  shoot him sqare in th head putting him down, then jump through the Weapon Armory door.
            """
            ))
            return 'laser_weapon_armory'
        elif action == 'ImaCheat':
            print(dedent("""You are quite the jumper"""))
            return 'escape_pod'
        else:
            print('DOES NOT COMPUTE')
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent(""" You do a dive roll into the Weapon Armory, crouch and scan the room for
        more Gothons that might be hiding. It's dead quiet, too quiet. You stand up and run to
        the far side of the room and find the neutron bomb in it's container. There's a key pad
        lock on the obox and you need the code to get the bomb out. If you get the code wrong 10
        times then the lock closes forever and you can't get the bomb. The code is 3-digits.
        """))
        #The bug here is that, the counter starts at 0 and the loop runs 10 times
        #when guess < 0. You have another input inside the loop so 11 times
        code = f"{randint(0,9)}{randint(0,9)}{randint(1,9)}"
        print(f"This is cheating but I have to: {code}")
        guess = input("[keypad]>")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZEDD!")
            guesses +=1
            guess = input("[keypad]>")

        if guess == code:
            print(dedent("""
                  The container clicks open and the seal breaks, letting gas out.
                  You grab the neutron bomb and run as fast as you can to the bridge
                  where you must place it in the right spot.
            """))
            return 'the_bridge'
        elif action == 'ImaCheatagain':
            print(dedent("""You are quite the jumper"""))
            return 'escape_pod'
        else:
            print(dedent("""
            The lock buzzez on last time and hear a melting sound. The mechanism is fused
            together the Gothon's blow up the ship from the ship
            from the insde, resulting in your death.
            """))
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print(dedent("""
        You burst onto the Bridge with the neutron destruct bomb under your arm
        and surprise 5 Gothons who are trying to take control of the ship. Each
        of them has an even uglier clown costume than the last. They haven't pulled
        their weapons out yet, as they see the active bomb under your arm and don't
        want to set it off.
        """))
        action = input("Choose a letter\n a: Throw the bom\nb: Slowly place the bomb\n> ")
        if action == 'a':
            print(dedent("""In a panic you throw the bomb at the group of Gothons
            and make a leap for the door. Right as you drop it a Gothon shoots you
            righ in the back killing you. As you die, you see another Gothon frantically try to
            disarm the bomb. You die knowing they will probably blow up when it goes off.
            """))
            return 'death'
        elif action == 'b':
            print(dedent("""
                You point your blaster at the bomb at the bomb under your arm and
                the Gothons put their hands up and start to sweat. You inch backward to the
                door, open it, and then carefully place the bomb on the floor, pointing your
                blaster at it. You then jump back through the door, punch the close button and
                blast the lock so the Gothon's can't get out. Now that the bomb is placed
                you run to the escape pod to get off this tin can.
                """))
            #should pass as string
            return 'escape_pod'
        else:
            print("Does not compute")
            return the_bridge
class EscapePod(Scene):
    def enter(self):
        print(dedent("""
              You rush through the ship desparately trying to get to the escape
              pod before the whole ship explodes. It seems like there are hardly
              any Gothons on the ship so your  run is clear of any interference.
              You get to the chamber with the escape pods, and now need to pick one to
              take. Some of them could be damaged but you don't have time to look.
              There are 5 pods, which one do you take?
        """))
        good_pod = randint(1,5)
        print(f"This is cheating but I have to: {good_pod}")

        guess = input("[pod #]>")

        if int(guess) != good_pod:
            #Note that with the triples no format string stuff
            print(dedent("""You jumo into pod {guess} and hit the eject buttton.
            The pod escapes out into the void of space, then implodes as the hull
            ruptures, crushing your body into jam jelly.
            """))
            return 'death'
        else:
            print(dedent(""" You jump into pod {guess} and hit the eject button.
            The pod easily slides out into space heading to the planet below. As
            it flies to the plant, you look back and see your ship implode like
            a bright star, taking out the Gothon ship at the same time.\nYou won!"""))
            return 'finished'

class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        return 'finished'

class Map(object):
    #A dictionary of scenes, with the scene classes as the values
    #This is also a has-many relationship
    #Since this is not in __init__, it is created once and attached to the class
    scenes = {
    'central corridor': CentralCorridor(),
    'laser_weapon_armory':LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'finished':Finished(),
    'death': Death(),
    }
    #init takes in self, start_scene as params
    def __init__(self, start_scene):
        self.start_scene = start_scene
        #next scene method takes in scene_name as param
    def next_scene(self, scene_name):
        #.get method: get() returns a value for the given key.
        # If key is not available then returns default value None
        val = Map.scenes.get(scene_name)
        #returns the value, i.e. the class for the scene_name key
        return val
        #Opening scene method, is the next_scene function that takes in the start_scene as the param
        #So just returns the class for the opening scene
    def opening_scene(self):
        return self.next_scene(self.start_scene)
#This creates an instance of Map Class with the param 'central_corridor', named a_map
#I wasted 2 fucking days because I put an underscore between central and corrdor. Fuck me
a_map = Map('central corridor')
#pass this instance/ object to class Engine an create an instance of Engine called a_game
a_game = Engine(a_map)
#in instance a_game, call method play
a_game.play()
