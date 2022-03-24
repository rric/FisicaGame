# F03_Listeners.pyde
# Copyright 2018-2022 Roland Richter

add_library('fisica')
add_library('sound')

# TOUR-1 This sketch uses fisica, a 2D physics library by Ricard Marxer,
#   and the Sound library, provided by The Processing Foundation.

# ATTENTION There's a severe restriction (read "bug") of the Sound
#   library in Processing.py: as pointed out by The_Math_Maniac1 at
#   https://discourse.processing.org/t/python-sound-library/35034/6,
#   "it runs properly the first time, then any time after that I have
#   to relaunch processing :frowning:"

from Brick import *
from BurstBall import *
from Nail import *
from PingPongBall import *
from Plank import *
from SoapBubble import *
from SoccerBall import *


# TOUR-4 What happenes when two objects of the fisica world, say, a Brick and 
#   a SoccerBall, hit each other? ... they send out a message!
#   Here, the message is an object of type FContact, and the receiver is again
#   our program. An FContact message holds several details about the contact:
#   for instance, which two bodies have contact, where the contact happened,
#   at which velocity, and so on. See all the details at
#   http://www.ricardmarxer.com/fisica/reference/fisica/FContact.html

class ContactListener(FContactAdapter):
    def __init__(self):
        pass

    def contactPersisted(self, contact):
        pass

    def contactEnded(self, contact):
        pass

    def contactStarted(self, contact):
        b1 = contact.getBody1()
        b2 = contact.getBody2()
        
        print(b1.getName(), " <-> ", b2.getName())
    
        # TOUR-5 Objects should make sounds if they bang against hard things.
        #   I decided, somehow arbitrarily, that Nails, Planks, and Bricks are hard,
        #   because they have a density greater than 2000.
        #   A sound is played if the first object is hard, and the second object can
        #   make a sound. Once again, we find out the type of an object by using
        #   the _instanceof_ keyword.
        isHard1 = (b1.getDensity() > 2000)
    
        if isHard1:
            try:
                b2.playSound()
            except:
                pass
    
        # TOUR-8 If, say, a Brick and a SoccerBall hit each other, we do not know
        #   in which order they appear in the FContact message: either b1 is the
        #   Brick, and b2 the SoccerBall, or vice versa. Hence, we have to repeat
        #   the code from above, only with b1 and b2 switched.
        isHard2 = (b2.getDensity() > 2000)
    
        if isHard2:
            try:
                b1.playSound()
            except:
                pass
        
        # HOMEWORK-3-b Remove a soap bubble as soon as it has contact with any other object.
        # Hint: http://www.ricardmarxer.com/fisica/reference/fisica/FWorld.html#remove(fisica.FBody)
        
        # HOMEWORK-3-c+ (bonus homework): Implement the following behaviour:
        #   As soon as a SoccerBall has contact with a Nail, it starts to loose air; that is,
        #   it gets smaller and smaller, probably makes a hissing sound, until it disappears
        #   and is removed from this world ...



def setup():
    size(800, 550)

    Fisica.init(this)
    Fisica.setScale(150)  # scale: 150 pixel = 1 m
    
    global world
    world = FWorld()
    
    world.setGravity(0, 300)
    world.setGrabbable(True)
    world.setEdges()
    
    world.setContactListener(ContactListener())

    # Lets create some objects, and add them to the world

    for i in range(1, 6):
        nail = Nail()
        nail.setPosition(i * width/6, 200)
        world.add(nail)

    for i in range(2, 5):
        nail = Nail()
        nail.setPosition(i * width/6, 350)
        world.add(nail)
    
    plank = Plank(350, 15)
    
    plank.setPosition(width/2, 300)
    plank.setName("Wooden plank")
    world.add(plank)

    global soccersf, bricksf, pingpongsf

    # TOUR-7 Sound files must be located in the /data folder of the sketch;
    #   go have a look: our sketch now uses four sound files! ... See also 
    #   https://processing.org/reference/libraries/sound/SoundFile.html
    #
    #   The soccer ball sound is used under the "CC BY 3.0" license;
    #   CC = Creative Commons, BY = attribution, 3.0 = version of the license.
    #   It means that now I *have to* mention the author:
    # 
    #   soccer ball hit ground 01.wav by volivieri, used under CC BY 3.0
    #   https://freesound.org/s/37154/
    soccersf = SoundFile(Fisica.parent(), "37154__volivieri__soccer-ball-hit-ground-01.wav")

    # Brick dropped on other bricks by jackmurrayofficial used under CC 0
    # https://freesound.org/s/429402/
    bricksf = SoundFile(Fisica.parent(), "429402__jackmurrayofficial__brick-dropped-on-other-bricks_cut.wav")

    # Dropping ping pong ball on table by giddster, used under CC 0
    # https://freesound.org/s/414460/
    pingpongsf = SoundFile(Fisica.parent(), "414460__giddster__dropping-ping-pong-ball-on-table_cut.wav")

    global redBall, greenBall, whiteBall

    redBall = SoccerBall(50, color(255, 40, 0))     # create a "Ferrari red" (#FF2800) ball ...
    redBall.setPosition(120, 40)                    # ... somewhere at top left ...
    redBall.setVelocity(random(-80, 80), 0)         # ... with random velocity.
    redBall.setName("Red soccer ball")
    redBall.setSound(soccersf)
    world.add(redBall)
    
    greenBall = SoccerBall(50, color(57, 255, 20))  # create a "Neon green" (#39FF14) ball ...
    greenBall.setPosition(width/2, 40)              # ... somewhere at top centered ...
    greenBall.setVelocity(random(-80, 80), 0)       # ... with random velocity.
    greenBall.setName("Green soccer ball")
    greenBall.setSound(soccersf)
    world.add(greenBall)

    whiteBall = SoccerBall()                        # create a standard colored ball ...
    whiteBall.setPosition(width-120, 40)            # ... somewhere at top right ...
    whiteBall.setVelocity(random(-80, 80), 0)       # ... with random velocity.
    whiteBall.setName("Standard soccer ball")
    whiteBall.setSound(soccersf)
    world.add(whiteBall)
    
    leftPingPong = PingPongBall()                   # create a ping pong ball ...
    leftPingPong.setPosition(width/3, 40)           # ... at top left ...
    leftPingPong.setVelocity(random(-80, 80), 0)    # ... with random velocity.
    leftPingPong.setName("Ping pong ball #1")
    leftPingPong.setSound(pingpongsf)
    world.add(leftPingPong)

    rightPingPong = PingPongBall()                  # create a ping pong ball ...
    rightPingPong.setPosition(2*width/3, 40)        # ... at top right ...
    rightPingPong.setVelocity(random(-80, 80), 0)   # ... with random velocity.
    rightPingPong.setName("Ping pong ball #2")
    rightPingPong.setSound(pingpongsf)
    world.add(rightPingPong)


bgcolor = color(239, 222, 205)  # start with a decent background color, "Almond" (#EFDECD)

paused = 0
debug = False


# draws background, and displays name and version of this game
def drawBackground():
    # have black background in debug mode
    background(color(0, 0, 0) if debug else bgcolor)
    
    # determine font color; see https://stackoverflow.com/a/1855903
    luminance = (0.299 * red(bgcolor) + 0.587 * green(bgcolor) + 0.114 * blue(bgcolor))/255.0
    
    # bright background - black font; dark background - white font
    if luminance > 0.5:
       fill(color(0, 0, 0))
    else:                 
       fill(color(255, 255, 255))
    
    textSize(12)
    textAlign(RIGHT)
    text("FisicaGame @" + nf(frameRate, 1, 1) + "fps\n[lesson: polymorphism]", 
         0.99*width, 0.95*height)
    
    
def draw():
    global paused
    
    if paused > 0:
        paused -= 1
        return
    
    drawBackground()
    
    # inform all objects about the next tick
    bodies = world.getBodies()
    for b in bodies:
        try:
            b.tick()
        except:
            pass
    
    world.step()
    
    if debug:
        world.drawDebug()
    else:
        world.draw()


# TOUR-2 Lets have another look at the keyPressed() method. The documentation
#   at https://processing.org/reference/keyPressed_.html talks about "mouse and
#   keyboard events". An _event_ is some kind of _message_ which is created by
#   the _sender_, transmitted over a _channel_, and received by a _receiver_, or
#   several receivers. This _pattern_ is so common that it has many names, e.g.,
#   - event handling: event source, control -> event handler
#   - publish–subscribe: publisher -> subscriber
#   - observer pattern: subject -> observer, listener
#   In the sequel, I will use the words "sender", "message", and "receiver".
def keyPressed():
    # b/B - change background color
    if key == 'b' or key == 'B':
        global bgcolor
        bgcolor = color(random(255), random(255), random(255))

    # n/N - create a new object
    if key == 'n' or key == 'N':
        # create a new thing at random, ...
        thing = None
        wurfel = int(random(6)) + 1

        if wurfel == 1:
            thing = Brick()
            thing.setSound(bricksf)
        elif wurfel == 2:
            thing = PingPongBall()
            thing.setSound(pingpongsf)
        elif wurfel == 3:
            thing = SoccerBall()
            thing.setSound(soccersf)
        elif wurfel == 4:
            sf = SoundFile(Fisica.parent(), "186927__readeonly__burst2.wav")
            thing = BurstBall()
            thing.setBang(sf)
        else:
            randclr = color(random(255), random(255), random(255))
            thing = SoapBubble(38, randclr)
        
        thing.setPosition(int(random(80, width-80)), 30)
        global world
        world.add(thing)

    # d/D - switch debug mode on or off
    if key == 'd' or key == 'D':
        global debug
        debug = not debug

    # p/P - pause for approx. 24 hours (at 60 fps), or re-start
    if key == 'p' or key == 'P':
        global paused
        paused = 0 if paused > 0 else 24*60*60*60

    # s/S - save the current frame, and pause for approx. 0.5 sec
    if key == 's' or key == 'S':
        saveFrame("fisica-###.jpg")
        global paused
        paused = 30


# TOUR-3 Lets examine what happens when the user presses a mouse button:
#   the mouse, as the "sender", generates a new "message", and sends it
#   to anyone who is listening; here, the "receiver" is our FisicaGame 
#   program; it receives a message, which contains information about
#   - whether or not a mouse button is currently pressed (mousePressed)
#   - which mouse button is pressed, if any (mouseButton)
#   - where the mouse is currently located (mouseX, mouseY)
#   
#   Note that the sender often does not know which, or how many, receivers
#   are listening; however, the sender must create messages which each 
#   receiver can understand; in other words, sender and receiver have to 
#   use a common _protocol_.
def mousePressed():
    if mousePressed and (mouseButton == RIGHT):
        nail = Nail()
        nail.setPosition(mouseX, mouseY)
        world.add(nail)
        
        # HOMEWORK-3-a Play a hammering sound whenever a nail is added here.
        # Hint: https://processing.org/reference/libraries/sound/SoundFile.html


# ----------------------------------------------------------------------
# This file is part of FisicaGame.
#
# FisicaGame is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
