# Sounding.py
# Copyright 2018-2022 Roland Richter

# TOUR-10 Use multiple inheritance to add sounding methods to several classes;
#   each class which derives from Sounding will be able to playSound().
class Sounding:
    def __init__(self):
        pass
    
    def setSound(self, soundfile):
        self.sound = soundfile
        
    def playSound(self, amplitude = 1.0):
        self.sound.amp(amplitude)
        self.sound.play()


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
