# F04_Shapes.pyde
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
# Update: under Linux, everything seems to work.

from Alien import *
from Brick import *
from Bucket import *
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
    
    global world, worldBodyCount
    world = FWorld()
    
    world.setGravity(0, 300)
    world.setGrabbable(True)
    world.setEdges()
    
    world.setContactListener(ContactListener())
    
    # create a global dictionary of sound files
    global sounds
    sounds = {}

    #   soccer ball hit ground 01.wav by volivieri, used under CC BY 3.0
    #   https://freesound.org/s/37154/
    sounds['soccer'] = SoundFile(Fisica.parent(), "37154__volivieri__soccer-ball-hit-ground-01.wav")

    # Brick dropped on other bricks by jackmurrayofficial used under CC 0
    # https://freesound.org/s/429402/
    sounds['brick'] = SoundFile(Fisica.parent(), "429402__jackmurrayofficial__brick-dropped-on-other-bricks_cut.wav")

    # Dropping ping pong ball on table by giddster, used under CC 0
    # https://freesound.org/s/414460/
    sounds['pingpong'] = SoundFile(Fisica.parent(), "414460__giddster__dropping-ping-pong-ball-on-table_cut.wav")
    
    # video game >> burst2.wav by ReadeOnly, used under CC 0, from
    # https://freesound.org/s/186927/
    sounds['bang'] = SoundFile(Fisica.parent(), "186927__readeonly__burst2.wav")

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

    global redBall, greenBall, whiteBall

    redBall = SoccerBall(50, color(255, 40, 0))     # create a "Ferrari red" (#FF2800) ball ...
    redBall.setPosition(120, 40)                    # ... somewhere at top left ...
    redBall.setVelocity(random(-80, 80), 0)         # ... with random velocity.
    redBall.setName("Red soccer ball")
    redBall.setSound(sounds['soccer'])
    world.add(redBall)
    
    greenBall = SoccerBall(50, color(57, 255, 20))  # create a "Neon green" (#39FF14) ball ...
    greenBall.setPosition(width/2, 40)              # ... somewhere at top centered ...
    greenBall.setVelocity(random(-80, 80), 0)       # ... with random velocity.
    greenBall.setName("Green soccer ball")
    greenBall.setSound(sounds['soccer'])
    world.add(greenBall)

    whiteBall = SoccerBall()                        # create a standard colored ball ...
    whiteBall.setPosition(width-120, 40)            # ... somewhere at top right ...
    whiteBall.setVelocity(random(-80, 80), 0)       # ... with random velocity.
    whiteBall.setName("Standard soccer ball")
    whiteBall.setSound(sounds['soccer'])
    world.add(whiteBall)
    
    leftPingPong = PingPongBall()                   # create a ping pong ball ...
    leftPingPong.setPosition(width/3, 40)           # ... at top left ...
    leftPingPong.setVelocity(random(-80, 80), 0)    # ... with random velocity.
    leftPingPong.setName("Left ping pong ball")
    leftPingPong.setSound(sounds['pingpong'])
    world.add(leftPingPong)

    rightPingPong = PingPongBall()                  # create a ping pong ball ...
    rightPingPong.setPosition(2*width/3, 40)        # ... at top right ...
    rightPingPong.setVelocity(random(-80, 80), 0)   # ... with random velocity.
    rightPingPong.setName("Right ping pong ball")
    rightPingPong.setSound(sounds['pingpong'])
    world.add(rightPingPong)
    
    global bucket
    bucket = Bucket()
    bucket.setPosition(width/2-60, 50)
    bucket.setName("Eimer")
    world.add(bucket)
    
    # create Ellen, the (hopefully) friendly alien
    global ellen
    ellen = Alien("Ellen")

    ellen.setPosition(int(random(width/2-30, width/2+30)), 250)
    world.add(ellen)
    
    # I expected that redBall, greenBall, etc. are in the getBodies() list, but ...
    # worldBodyCount = len(world.getBodies())
    # ... only returns 4 objects. Hence, set worldBodyCount manually here: 
    worldBodyCount = 17


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
    text("FisicaGame\n[lesson: shapes]", 0.99*width, 0.95*height)
    
    
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
    
    # TOUR-8 It's a bit senseless, but funny anyway: 
    #   Print how many things there are in the world, and how many are in the 
    #   bucket; or, more precisely: how many objects are touching the bucket.
    #
    #   Note that this is not really precise: e.g. if a Plank touches the Bucket,
    #   it's more likely that the Bucket stands on the Plank instead of the 
    #   Plank being in the Bucket, so do not count Planks. Also, counting does
    #   *not* work correctly with compund objects such as Alien.

    if (frameCount % 60) == 0:
        print(bodies.size(), "things here are. ")

        inBucket = bucket.getTouching()
        count = 0

        for e in inBucket:
            if not e.isStatic() and not e.__class__.__name__ == "Plank":
                count += 1

        # TOUR-9 REMOVED
        if count == 1:
            print("One thing in the bucket is. ")
        else:
            print(count, "things in the bucket are. ")

        if count < 3:
            print("Many things you must collect.")
        else:
            print("Many things you have collected.")
    
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
        # create a new thing at random, ...
        thing = None
        wurfel = int(random(6)) + 1

        if wurfel == 1:
            thing = Brick()
            thing.setSound(sounds['brick'])
        elif wurfel == 2:
            thing = PingPongBall()
            thing.setSound(sounds['pingpong'])
        elif wurfel == 3:
            thing = SoccerBall()
            thing.setSound(sounds['soccer'])
        elif wurfel == 4:
            thing = BurstBall()
            thing.setBang(sounds['bang'])
        else:
            clr = color(random(255), random(255), random(255))
            thing = SoapBubble(38, clr)
        
        # set thing name to some meaningful text
        thing.setPosition(int(random(80, width-80)), 30)
        thing.setName("Object #" + str(worldBodyCount) + ": a " + thing.__class__.__name__)
        
        global world, worldBodyCount
        world.add(thing)
        worldBodyCount += 1
        
    # let the user steer Ellen by pressing UP, DOWN, LEFT, or RIGHT
    if key == CODED:
        if keyCode == UP:
            ellen.addImpulse(0, -3000)

        if keyCode == DOWN:
            ellen.addImpulse(0, +500)

        if keyCode == LEFT:
            ellen.addImpulse(-1500, 0)

        if keyCode == RIGHT:
            ellen.addImpulse(+1500, 0)

    # TOUR-12 In Fisica, there's yet another way to create "compound" objects,
    #   i.e. objects that consist of other objects: it provides a number of
    #   different Joint classes, see
    #   http://www.ricardmarxer.com/fisica/reference/fisica/FJoint.html
    #   A joint establishes some kind of relation between two or more bodies. 
    #
    #   Here, first we create 20 small circles, all positioned along a line.
    #   Then, a FDistanceJoint is used to connect the first circle with the
    #   second circle, the second circle with the third one, and so on.
    #   The result is something like a chain of 20 joint objects. Note that
    #   distance joints are both elastic (to some degree), and not solid: i.e.
    #   other objects may pass through.
    if key == 'j' or key == 'J':
        # create 20 chain elements, and join them
        chain = []
        for k in range(20):
            chain.append(FCircle(12))
            chain[-1].setDensity(1000.0)
            chain[-1].setFillColor(color(70, 130, 180))  # Steel blue, see http://latexcolor.com/
            chain[-1].setPosition(lerp(300, width-300, k/20.), 30)
            world.add(chain[-1])

        for k in range(1, 20):
            joint = FDistanceJoint(chain[k-1], chain[k])
            joint.setFrequency(10.0)
            joint.setDamping(5.0)
            world.add(joint)     

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
        
        # TOUR-2 Until now, one could place a new nail *anywhere*, even
        #   if there already was another object at the very same position.
        #   However, our sketch must obey the basic laws of physics: at 
        #   any given time, only *one* object can be at a given position.
        #   
        #   Lets change the behaviour if the right mouse button is pressed:
        #   first, obtain the object at mouse position via the getBody() 
        #   function. If it returns "None", it's Pythons way of saying that
        #   there's no object there, and we can add a nail; otherwise, i.e.
        #   if there *is* some object, we change a property of that object ...
        underneath = world.getBody(mouseX, mouseY, True)

        if (underneath == None):
            nail = Nail()
            nail.setPosition(mouseX, mouseY)
            world.add(nail)
        else:           
            # TOUR-3 Go have a look at Fisica's documentation, at
            #   www.ricardmarxer.com/fisica/reference/fisica/FBody.html
            #
            #   There, it says that `setStatic()` sets "whether the body is
            #   static. Static bodies do not move or rotate, unless done
            #   manually [...]"
            #
            #   This means static bodies can still be dragged: press the left
            #   mouse button, and move the object around. If you dislike that,
            #   you have to change the object's "grabbable" property as well.

            underneath.setStatic(True)
            # underneath.setGrabbable(False)

            # TOUR-4 Another property of an object is its name. I use it
            #   sometimes: e.g. all balls get names, but nails do not ... 
            #   It is a tiny feature and makes debugging more convient.
            print("At (", mouseX, ",", mouseY, "), there\'s", underneath.getName())
            
            # HOMEWORK-4-a Go have a look at Fisica's documentation (again), at
            #   www.ricardmarxer.com/fisica/reference/fisica/FBody.html
            #   and note how many "set<SomeProperty>" functions every object has
            #   (some not documented, unfortunately.)
            #
            #   Turn your mouse into a magic wand: if one right-clicks an object,
            #   change some property of that object.


class ContactListener(FContactAdapter):
    def __init__(self):
        pass

    def contactStarted(self, contact):
        b1 = contact.getBody1()
        b2 = contact.getBody2()
        # uncomment the next line to see which contacts are processed
        # print(b1.getName(), " <-> ", b2.getName())
        
        # soap bubbles burst with every contact
        if b1.__class__.__name__ == "SoapBubble":
            world.remove(b1)
    
        if b2.__class__.__name__ == "SoapBubble":
            world.remove(b2)

        # let objects make sounds if they bang against solid things
        isSolid1 = (b1.getDensity() > 2000)
    
        if isSolid1:
            try:
                b2.playSound()
            except:
                pass

        isSolid2 = (b2.getDensity() > 2000)
    
        if isSolid2:
            try:
                b1.playSound()
            except:
                pass

    
        # HOMEWORK-4-b Implement the following behaviour:
        # If Ellen, the alien, touches a SoccerBall, the ball changes its color.
        # The contact is not with the alien itself, but only with its head.
        # Hence, determine whether b1 (or b2) is the head of the alien.
        # Hint: use getName()
    
        # HOMEWORK-4-c+ (bonus homework): create your own compound object.

    def contactPersisted(self, contact):
        pass


    def contactEnded(self, contact):
        pass


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
