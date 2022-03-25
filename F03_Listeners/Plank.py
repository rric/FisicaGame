# Plank.py
# Copyright 2018-2022 Roland Richter

from fisica import FBox
from HighlightAble import *

# TOUR-7 ... then reuse it everywhere where needed: Plank now inherits from FBox
#   (as before), and additionally from HighlightAble. As a consequence, Plank
#   now provides the methods highlight() and undoHighlight(), as implemented
#   in HighlightAble. This technique is called _multiple inheritance_; some
#   languages (such as Python) allow it, some (such as Java) do not.
class Plank(FBox, HighlightAble):

    def __init__(self, w = 350, h = 15, clr = color(128, 70, 27)):
        FBox.__init__(self, w, h)
        
        self.setFillColor(clr)
        
        self.setDamping(0.2)
        self.setDensity(7000.0)
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
