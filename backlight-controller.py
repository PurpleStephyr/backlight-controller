#!/usr/bin/env python3

# Copyright 2024 Steph Kraemer <purple.stephyr@proton.me>

# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.

import time
import random

def clamp(x, low, high):
    return max(low, min(high, x))

def pick_random_colour(current_colour):
    choices = [
        [255,255,255],
        [255,255,0],
        [255,0,255],
        [0,255,255],
        [255,0,0],
        [0,255,0],
        [0,0,255]]
    choices.remove(current_colour)
    return random.choice(choices)

FILE='/sys/class/leds/system76_acpi::kbd_backlight/color'

f = open(FILE, 'w')

colour = [255,255,255]
next_colour = pick_random_colour(colour)
while True:
    f = open(FILE, 'w')
    colour_str = f"{colour[0]:02X}{colour[1]:02X}{colour[2]:02X}"
    print(colour_str)
    f.write(colour_str)
    for i in range(len(colour)):
        if colour[i] < next_colour[i]:
            colour[i] += 10
        elif colour[i] > next_colour[i]:
            colour[i] -= 10
        colour[i] = clamp(colour[i], 0, 255)
    if colour == next_colour:
        next_colour = pick_random_colour(colour)
    time.sleep(0.05)
    f.close()
