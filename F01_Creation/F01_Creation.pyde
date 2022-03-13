# F01_Creation.pyde
# Copyright 2018-2022 Roland Richter

add_library('fisica')

# TOUR-1 This sketch uses fisica, a 2D physics library by Ricard Marxer.
#   The documentation of fisica is at http://www.ricardmarxer.com/fisica/,
#   and the source code is at https://github.com/rikrd/fisica
#
#   fisica provides a world where all objects exist in. I will use the term 
#   _object_; in the online documentation, an object is often called a _body_.

from Brick import *
from Nail import *
from PingPongBall import *
from Plank import *
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

    # TOUR-2 Lets create some objects, and add them to the world. In the tabs
    #   above, you see which kind of objects there are: Brick, Nail, PingPongBall,
    #   Plank, and SoccerBall. First, some nails ...

    for i in range(1, 6):
        nail = Nail()
        nail.setPosition(i * width/6, 200)
        world.add(nail)

    for i in range(2, 5):
        nail = Nail()
        nail.setPosition(i * width/6, 350)
        world.add(nail)
        
    # TOUR-4 Here, an object called `plank` of class `Plank` is created.
    #   Note the subtle difference: `Plank` (with uppercase P) is the name 
    #   of the class, `plank` (with lowercase p) is one object of class Plank.
    #   By convention, class names start with uppercase letters, whereas 
    #   object names start with lowercase letters.
    
    plank = Plank(350, 15)
    
    # TOUR-7 Now that the object plank has been created, we can set some
    #   further properties of it; e.g., its position, and its name.
    #   Classes typically have many methods called getXYZ() and setXYZ()
    
    plank.setPosition(width/2, 300)
    plank.setName("Wooden plank")
    world.add(plank)

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
    
    # HOMEWORK-1-b The world as populated above -- with eight nails, a plank, and
    #   soccer and ping pong balls -- is not very creative; it's not really a "game".
    #   Think of some other world, and populate it with a number of objects.


bgcolor = color(239, 222, 205) # start with a decent background color, "Almond" (#EFDECD)

paused = False
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
    text("FisicaGame\n[lesson: creation]", 0.99*width, 0.95*height)
    
    
def draw():
    if paused:
        return
    
    drawBackground()
    
    world.step()
    
    if debug:
        world.drawDebug()
    else:
        world.draw()


# TOUR-9 `keyPressed()` is called whenever a key is pressed -- you might have
#   guessed ... Since I do not care whether the key is lower- or uppercase,
#   my code always tests whether the lowercase or uppercase key was pressed.
#   Just try what happens if you press 'b' or 'D' or 'N' ...
#   
# You are now finished with the TOUR. Go and start to look for HOMEWORK-1!

def keyPressed():
    # b/B - change background color
    if key == 'b' or key == 'B':
        global bgcolor
        bgcolor = color(random(255), random(255), random(255))

    # n/N - create a new object
    if key == 'n' or key == 'N':
        # HOMEWORK-1-a Write a new class TennisBall, and create a tennis ball
        #   instead of a brick here.
        # Hint: start by copying SoccerBall. Wait a minute ...
        #   Are you allowed to copy SoccerBall, or even modify it?! 
        #   Read on at TOUR-10
        
        thing = Brick()
        thing.setPosition(int(random(80, width-80)), 30)
        global world
        world.add(thing)
        
    # d/D - switch debug mode on or off
    if key == 'd' or key == 'D':
        global debug
        debug = not debug

    # p/P - switch between paused and not paused
    if key == 'p' or key == 'P':
        global paused
        paused = not paused


# TOUR-8 You already found out what happens if you right-click with the mouse,
#   didn't you? If not, just try it ...

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
