# F02_Polymorphism.pyde
# Copyright 2018-2022 Roland Richter

add_library('fisica')
add_library('sound')

# TOUR-1 This sketch uses fisica, and, additionally, the Sound library which 
#   is provided by _The Processing Foundation_, the organization behind the
#   development of Processing, p5.js, etc. To learn more, visit their site
#   https://processingfoundation.org/
#   If you don't have the Sound library installed yet, do so now.

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


def setup():
    size(800, 550)

    Fisica.init(this)
    Fisica.setScale(150)  # scale: 150 pixel = 1 m
    
    global world
    world = FWorld()
    
    world.setGravity(0, 300)
    world.setGrabbable(True)
    world.setEdges()

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

    # TOUR-12 These three balls are now declared as _global variables_, which can be
    #   accessed not only from within setup(), but also from within keyPressed(), etc.
    #
    # Why? Have a look at HOMEWORK-2-b ... (You are now finished with the TOUR.)
    global redBall, greenBall, whiteBall

    redBall = SoccerBall(50, color(255, 40, 0))     # create a "Ferrari red" (#FF2800) ball ...
    redBall.setPosition(120, 40)                    # ... somewhere at top left ...
    redBall.setVelocity(random(-80, 80), 0)         # ... with random velocity.
    redBall.setName("Red soccer ball")
    world.add(redBall)
    
    greenBall = SoccerBall(50, color(57, 255, 20))  # create a "Neon green" (#39FF14) ball ...
    greenBall.setPosition(width/2, 40)              # ... somewhere at top centered ...
    greenBall.setVelocity(random(-80, 80), 0)       # ... with random velocity.
    greenBall.setName("Green soccer ball")
    world.add(greenBall)

    whiteBall = SoccerBall()                        # create a standard colored ball ...
    whiteBall.setPosition(width-120, 40)            # ... somewhere at top right ...
    whiteBall.setVelocity(random(-80, 80), 0)       # ... with random velocity.
    whiteBall.setName("Standard soccer ball")
    world.add(whiteBall)
    
    leftPingPong = PingPongBall()                   # create a ping pong ball ...
    leftPingPong.setPosition(width/3, 40)           # ... at top left ...
    leftPingPong.setVelocity(random(-80, 80), 0)    # ... with random velocity.
    leftPingPong.setName("Ping pong ball #1")
    world.add(leftPingPong)

    rightPingPong = PingPongBall()                  # create a ping pong ball ...
    rightPingPong.setPosition(2*width/3, 40)        # ... at top right ...
    rightPingPong.setVelocity(random(-80, 80), 0)   # ... with random velocity.
    rightPingPong.setName("Ping pong ball #2")
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
    
    # TOUR-7 Processing, in combination with fisica, works likes a flip book:
    #   it draws an image, then moves all objects a little bit, then draws an 
    #   image again, then moves the objects a little bit, then draws an image
    #   again ... and so on, for many times per second. This draw-update loop
    #   gives the impression of smooth motion; the drawing frequency is called
    #   frame rate. Processing provides a variable to inspect this value, see
    #   https://processing.org/reference/frameRate.html
    #   You see the fps rate in the lower right corner of the background.
    #
    #   As already mentioned, our world holds a list of all objects. Here, we
    #   try to call tick() for each object, and ignore exceptions (see TOUR-6).
    #   For instance, each BurstBall is "ticked()" 50 to 60 times per second; 
    #   with each tick, its lifespan is reduced, until it finally bursts.
    
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


def keyPressed():
    # b/B - change background color
    if key == 'b' or key == 'B':
        global bgcolor
        bgcolor = color(random(255), random(255), random(255))

    # n/N - create a new object
    if key == 'n' or key == 'N':
        # TOUR-2 Here, a new object is created at random. It might be a new 
        #   Brick, or PingPongBall, or SoccerBall, ... we do not know yet.
        #   What we *do* know, however, is this: 
        #     - Brick is-a FBox, and FBox is-a FBody
        #     - PingPongBall is-a FCircle, and FCircle is-a FBody
        #     - and so on ...
        #   Going up the class hierarchy, we find FBody to be the common
        #   ancestor of all things which could be created here. Hence,
        #   the new object is known to be an FBody here; later on, it is 
        #   allowed to be "many things"; this is called _polymorphism_.
        #   How is the common ancestor of *all* classes in Java called?
        
        thing = None
        wurfel = int(random(6)) + 1

        if wurfel == 1:
            thing = Brick()
        elif wurfel == 2:
            thing = PingPongBall()
        elif wurfel == 3:
            thing = SoccerBall()
        elif wurfel == 4:
            # TOUR-10 Freesound is a collaborative database of audio snippets, 
            #   samples, recordings, etc., all released under some permisive 
            #   Creative Commons license. 
            #   "CC 0" here is short for "Creative Commons Zero", and basically
            #   means "public domain"; that is, I am free to re-use this sound 
            #   without mentioning the author. I do mention her/him, anyway: 
            #
            # video game >> burst2.wav by ReadeOnly, used under CC 0, from
            # https://freesound.org/s/186927/
            sf = SoundFile(Fisica.parent(), "186927__readeonly__burst2.wav", False)
            thing = BurstBall(sf)
        else:
            randclr = color(random(255), random(255), random(255))
            thing = SoapBubble(38, randclr)
        
        thing.setPosition(int(random(80, width-80)), 30)
        global world
        world.add(thing)
        
    # TOUR-3 New as well: some objects are resizable now. Try it out first!
    #   ... funny, isn't it? Lets have a look how it works.
    
    # r/R - resize all objects which are resizable
    if key == 'r' or key == 'R':
        # resize all objects by the same random factor, between 66.67 % and 150 %
        factor = random(0.6667, 1.5)
        
        # TOUR-5 A central idea of object oriented programming is _polymorphism_
        #   (from the Greek words "poly" = many, "morph" = form, figure, shape).
        #   
        #   Our world holds a list of all objects which were created and added 
        #   so far. An item in that list might be a Brick, or PingPongBall, 
        #   or SoccerBall, ... we do not know yet.
        #   
        #   Python is called a dynamically-typed language (as opposed to, e.g., Java,
        #   which is statically-typed). Thus, a Python list can always hold items
        #   of arbitrary type; any list item is allowed to be one of "many forms".

        bodies = world.getBodies()

        for b in bodies:
            # TOUR-6 Here, we can resize all objects which provide the resize() 
            #   method. How can we know whether an object has the resize() method
            #   or not? Answer: we simply cannot, because items can be of any type
            #   (see above).
            #   Hence, we have to try to resize(): if it works, fine; if it
            #   does not, an exception is thrown, which is ignored here.
            try:
                b.resize(factor)
            except:
                pass

    # HOMEWORK-2-a If somebody presses 'c' or 'C' here, SoccerBalls (and, at your
    #   choice, other objects) should change their color.
    #   Hint: this might be quite similar to SoccerBall.resize() ...
    
    # HOMEWORK-2-b If a BurstBall bursts, display the word "BANG" or "BOOM", and/or
    #   an explosion picture such as https://openclipart.org/detail/284551/boom
    #   at the screen for some moments.
    
    # HOMEWORK-2-c Give the user some control over the red, green, and white ball:
    #   * Use special keys, such as the UP, DOWN, LEFT, and RIGHT keys,
    #     see also https://processing.org/reference/keyCode.html
    #   * redBall, greenBall, and whiteBall are now global variables which can be 
    #     accessed here; see TOUR-12
    #   * You might change the position, or the velocity of the balls; or add an
    #     impulse to an object (see SoapBubble.tick())
    global redBall, greenBall, whiteBall
    if key == CODED:
        if keyCode == UP:
            pass
            # ... your code here ...
        elif keyCode == DOWN:
            pass
        elif keyCode == LEFT:
            pass
        elif keyCode == RIGHT:
            pass

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

def mousePressed():
    if mousePressed and (mouseButton == RIGHT):
        nail = Nail()
        nail.setPosition(mouseX, mouseY)
        world.add(nail)


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
