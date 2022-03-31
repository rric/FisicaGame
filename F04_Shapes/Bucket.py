# Bucket.pde
# Copyright 2018-2022 Roland Richter

from fisica import FCompound, FPoly

# TOUR-5 Here, class Bucket is declared: it consists of several parts
#   (namely, the left, bottom, and right part, see below). Therefore,
#   Bucket extends the FCompound class: FCompound is a _composition_
#   of other FBody objects. Additionally, FCompound is a FBody itself,
#   so you can use compositions in the same way as single objects.
class Bucket(FCompound):

    # Lavender gray, see http://latexcolor.com/
    def __init__(self, clr = color(196, 195, 208)):
        FCompound.__init__(self)
        
        # TOUR-6 In the constructor of Bucket, the left, bottom, and right 
        #   part of the bucket are created: all parts are polygonal bodies,
        #   and can be created by adding vertices with the `vertex(x, y)` 
        #   method. Note that the last vertex must equal the first vertex
        #   to "close the cycle".
        #   I used https://www.geogebra.org/graphing to obtain all the 
        #   x- and y-coordinates of the three polygonal bodies.
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

        # TOUR-7 After creating the three parts, they are added to the object.
        #   Nothing further is to be done here; a FCompound object is just a
        #   composition of other FBody objects (here, three FPoly objects). 
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
