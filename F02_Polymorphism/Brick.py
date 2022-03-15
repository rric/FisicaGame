# Brick.py
# Copyright 2018-2022 Roland Richter

from fisica import FBox

class Brick(FBox):
    # Brick red #CB4154, see http://latexcolor.com/
    def __init__(self, w = 45, h = 20, clr = color(203, 65, 84)):
        
        FBox.__init__(self, w, h)
        
        self.setFillColor(clr)
        
        self.setDamping(0.2)
        self.setDensity(200000.0)
        self.setRestitution(0.0)

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
