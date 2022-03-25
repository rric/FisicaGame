# HighlightAble.py
# Copyright 2018-2022 Roland Richter

# TOUR-6 Most objects in our world (except Nails) should be highlighted when they
#   get in contact. It would be possible to add a highlight() method to each 
#   class, but that would be quite tedious. There's a better way to add new
#   methods to a large number of classes: implement it once (down here), ...
class HighlightAble:
    def __init__(self):
        pass
        
    def highlight(self, txtsize = 12):
        self.setStroke(192, 192, 192)
        if self.getName():
            textAlign(LEFT, BOTTOM)
            textSize(txtsize)
            text(self.getName(), self.getX(), self.getY())


    def undoHighlight(self):
        self.setStroke(0, 0, 0)


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
