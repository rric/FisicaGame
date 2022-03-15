# SoccerBall.py
# Copyright 2018-2022 Roland Richter

from fisica import FCircle

class SoccerBall(FCircle):
    # Anti-flash white #F2F3F4, see http://latexcolor.com/
    def __init__(self, diam = 50, clr = color(242, 243, 244)):
        FCircle.__init__(self, diam)
        
        self.setFillColor(clr)
        
        self.setDamping(0.2)
        self.setDensity(3000.0)
        self.setRestitution(0.5)
        
    # TOUR-4 SoccerBall now has one additional method, resize(); it is 
    #   implemented here, and resizes the self object by factor; e.g.
    #     factor = 2.5 -> resize self to 250 %, i.e. 150 % larger
    #     factor = 0.7 -> resize self to 70 %, i.e. 30 % smaller
    #     factor = 1.0 -> resize self to 100 %, i.e. do not resize at all
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
