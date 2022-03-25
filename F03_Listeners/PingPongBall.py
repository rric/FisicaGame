# PingPongBall.py
# Copyright 2018-2022 Roland Richter

from fisica import FCircle
from HighlightAble import *
from Sounding import *

class PingPongBall(FCircle, HighlightAble, Sounding):
    def __init__(self):
        FCircle.__init__(self, 16)
        self.setFillColor(color(255, 255, 255)) # white
        
        self.setDamping(0.2)
        self.setDensity(300.0)
        self.setRestitution(0.9)

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
