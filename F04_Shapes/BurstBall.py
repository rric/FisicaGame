# BurstBall.py
# Copyright 2018-2022 Roland Richter

from SoccerBall import *

class BurstBall(SoccerBall):
    # Rich electric blue #0892D0, see http://latexcolor.com/
    def __init__(self, diam = 40, clr = color(8, 146, 208), maxage = 300):
        SoccerBall.__init__(self, diam, clr)

        self.lifespan = maxage
        
        
    def setBang(self, soundfile):
        self.bang = soundfile


    def tick(self):
        self.lifespan -= 1
        if self.lifespan <= 0:
            self.burst()
            

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
