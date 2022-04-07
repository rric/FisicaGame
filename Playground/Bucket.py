# Bucket.pde
# Copyright 2018-2022 Roland Richter

from fisica import FCompound, FPoly

class Bucket(FCompound):

    # Lavender gray, see http://latexcolor.com/
    def __init__(self, clr = color(196, 195, 208)):
        FCompound.__init__(self)

        left = FPoly()
        left.vertex(-38, +16)
        left.vertex(-46, -48)
        left.vertex(-30, -48)
        left.vertex(-24,   0)
        left.vertex(-38, +16)   # same as first vertex
        left.setFillColor(clr)
        
        bottom = FPoly()
        bottom.vertex(-24,   0)
        bottom.vertex(+24,   0)
        bottom.vertex(+38, +16)
        bottom.vertex(-38, +16)
        bottom.vertex(-24,   0)
        bottom.setFillColor(clr)
        
        right = FPoly()
        right.vertex(+24,   0)
        right.vertex(+30, -48)
        right.vertex(+46, -48)
        right.vertex(+38, +16)
        right.vertex(+24,   0)
        right.setFillColor(clr)

        self.addBody(bottom)
        self.addBody(left)
        self.addBody(right)

        self.setDamping(0.2)
        self.setDensity(3000.0)
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
