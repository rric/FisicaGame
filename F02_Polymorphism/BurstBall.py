# BurstBall.py
# Copyright 2018-2022 Roland Richter

from SoccerBall import *

class BurstBall(SoccerBall):
    # Rich electric blue #0892D0, see http://latexcolor.com/
    def __init__(self, sf, diam = 40, clr = color(8, 146, 208), maxage = 300):
        SoccerBall.__init__(self, diam, clr)

        self.bang = sf
        self.lifespan = maxage
        
    # TOUR-8 Another tick reduces a BurstBalls life span by 1. When its life
    #   span reaches 0, it bursts ...        
    def tick(self):
        self.lifespan -= 1
    
        if self.lifespan <= 0:
            self.burst()
            
    # TOUR-9 ... it bursts with a loud bang, and is removed from our world.
    #   
    #   Each and every FBody contains a reference to the world it was added, called 
    #   m_world. By convention, an "m_" prefix indicates a member field.
    #   This is kind of a hack, since m_world is not mentioned in the documentation.
    def burst(self):
        self.bang.play()
        self.m_world.remove(self)

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
