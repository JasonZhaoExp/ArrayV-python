"""

    ArrayV Python - Python program to visualise sorting algorithms
    Copyright (C) 2023  Jason Zhao

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

import random

def generate_random_sequenced_array(min_num=0, max_num=2048):
    array = [a for a in range(min_num, max_num)]
    array = array_randomizer(array)
    return array

def generate_random_array(size=2048, min_num=0, max_num=2048):
    array = []
    for _ in range(size):
        array.append(random.randint(min_num, max_num))
    return array

def array_randomizer(array=None):
    if array is None:
        array = [a for a in range(0, 1024)]
    random.shuffle(array)
    return array
