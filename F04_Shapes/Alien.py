# Alien.pde
# Copyright 2018-2022 Roland Richter

from fisica import FCircle, FCompound, FLine

# TOUR-9 An Alien object is, again, a composition of other FBody objects:
#   - the head, of type FCircle
#   - the mouth, of type FLine
#   - left and right eye, of type FCircle
#   - left and right tentacle, of type FLine
class Alien(FCompound):

    def __init__(self, name):
        FCompound.__init__(self)
        
        self.setName(name)
        
        # TOUR-10 In a previous comment (TOUR 2), I claimed that our sketch
        #   must obey the laws of physics, and that only one object can be
        #   at a given position at a given time.
        #   That's not completely true: the Fisica library allows an object 
        #   to be a "sensor body". From the docs:
        #   "Sensor bodies act as normal bodies in the sense that they notify
        #    about contacts, however they do not collide with other bodies 
        #    (they act like ghost bodies)."
        #   The two tentacles of an Alien are, in this sense, "sensor bodies".
        leftTentacle = FLine(0, 0, -30, -30)
        leftTentacle.setStrokeColor(color(124, 252, 0))   # Lawn green, see http://latexcolor.com/
        leftTentacle.setStrokeWeight(2)
        leftTentacle.setSensor(True)
        
        rightTentacle = FLine(0, 0, +30, -30)
        rightTentacle.setStrokeColor(color(124, 252, 0))  # Lawn green
        rightTentacle.setStrokeWeight(2)
        rightTentacle.setSensor(True)
        
        head = FCircle(40)
        head.setName(name + "s head")
        head.setFillColor(color(124, 252, 0))   # Lawn green
        
        mouth = FLine(-6, 10, 6, 10)
        mouth.setStrokeColor(color(16, 12, 8))  # Smoky black
        mouth.setStrokeWeight(1)
        
        leftEye = FCircle(12)
        leftEye.setFillColor(color(135, 206, 235))  # Light sky blue
        leftEye.setPosition(-10, -10)
        
        rightEye = FCircle(12)
        rightEye.setFillColor(color(135, 206, 235))  # Light sky blue
        rightEye.setPosition(+10, -10)
        
        self.addBody(leftTentacle)
        self.addBody(rightTentacle)
        self.addBody(head)
        self.addBody(mouth)
        self.addBody(leftEye)
        self.addBody(rightEye)
        
        self.setDamping(0.2)
        self.setDensity(2000.0)
        self.setRestitution(0.1)


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
