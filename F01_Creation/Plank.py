# Plank.py
# Copyright 2018-2022 Roland Richter

from fisica import FBox

# TOUR-3 Here, a _class_ called Plank is declared.
#   Lets inspect each of the words in the _declaration_ below:
#
#   - class is a keyword; it is used to declare a class
#   - Plank is the class name; you can use almost any name here.
#     It's good practice to declare class Plank in a file also called Plank.
#   - FBox is a class which is already declared in the fisica library;
#     see http://www.ricardmarxer.com/fisica/reference/fisica/FBox.html
#   - thy syntax Plank(FBox) means that Plank is _derived from_ another
#     class, namely, FBox. Plank _inherits_ all the data fields and methods
#     of FBox. In short, Plank _is-a_ FBox

#   Plank is said to be a _subclass_ of FBox; and FBox is said to be the
#   _superclass_ of Plank. Note that a subclass can have only one superclass;
#   but that a superclass can have many different subclasses.
#   As a consequence, Plank and FBox both are part of a _class hierarchy_,
#   or class tree, which you can see here:
#   http://www.ricardmarxer.com/fisica/reference/fisica/package-tree.html

class Plank(FBox):
    
    # TOUR-5 To create an object of class Plank, one needs a special 
    #   method which is named __init__; such a method is called _constructor_.
    # 
    #   The constructor takes three arguments to initialize this object:
    #   `w` is the width, `h` is the height of the plank; `clr` is the color
    #   of the plank. All these arguments have default values.
    #
    #   The default color of a plank is 'Russet'. Processing has a color selector
    #   in the Tools menu, but I find http://latexcolor.com/ more useful.
    
    def __init__(self, w = 350, h = 15, clr = color(50, 27, 11)):
    
        # TOUR-6
        #   - first, call the constructor of the superclass of Plank, i.e. FBox
        #   - self means "use the current object"; it must be the first parameter 
        #     of any function in the class.

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
