# SoapBubble.py
# Copyright 2018-2022 Roland Richter

from fisica import FCircle

class SoapBubble(FCircle):
    # Bubbles #E7FEFF, see http://latexcolor.com/
    def __init__(self, diam = 38, clr = color(231, 254, 255)):
        FCircle.__init__(self, diam)
        
        self.setFillColor(clr)
        
        self.setDamping(0.2)
        self.setDensity(1.0)
        self.setRestitution(0.0)
        
    # TOUR-11 With every tick, i.e. every 1/60 sec or so, SoapBubbles gets
    #   a little impulse: random in horizontal dirction, but always upwards.
    #   This lets SoapBubbles float through the air; otherwise, they would
    #   fall downward like anything else! (Try it out ...)  
    def tick(self):
        self.addImpulse(random(-0.3, 0.3), -0.25)
        
    
    def resize(self, factor):
        mySize = self.getSize()
        newSize = factor * mySize
        self.setSize(newSize)
        
        
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
