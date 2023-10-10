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

import pygame

MAX_NUM = 24
def scale_point(point, window_size, zoom_level):
    x, y = point
    max_width, max_height = window_size
    scaled_x = int((x / MAX_NUM) * max_width * zoom_level)
    scaled_y = int((y / MAX_NUM) * max_height * zoom_level)
    return scaled_x, scaled_y

def limit_zoom(zoom_level):
    return max(1.0, min(5.0, zoom_level))

def limit_panning(pan_offset, window_size, zoom_level):
    max_x = int((MAX_NUM / MAX_NUM) * window_size[0] * zoom_level)
    max_y = int((MAX_NUM / MAX_NUM) * window_size[1] * zoom_level)
    min_x = window_size[0] - max_x
    min_y = window_size[1] - max_y

    pan_offset[0] = max(min_x, min(0, pan_offset[0]))
    pan_offset[1] = max(min_y, min(0, pan_offset[1]))
    return pan_offset

def main():
    pygame.init()
    initial_width, initial_height = 800, 600
    window = pygame.display.set_mode((initial_width, initial_height), pygame.RESIZABLE)
    pygame.display.set_caption("Resizable Window with Dots")
    dots_coordinates = [[x, MAX_NUM - x] for x in range(0, MAX_NUM)]
    zoom_level = 1.0
    pan_offset = [0, 0]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    zoom_level += 0.1
                elif event.button == 5:
                    zoom_level -= 0.1
                    zoom_level = limit_zoom(zoom_level)
            elif event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                pan_offset[0] += event.rel[0]
                pan_offset[1] += event.rel[1]
                pan_offset = limit_panning(pan_offset, (window.get_width(), window.get_height()), zoom_level)
        window.fill((255, 255, 255))
        for dot_coords in dots_coordinates:
            scaled_dot = scale_point(dot_coords, (window.get_width(), window.get_height()), zoom_level)
            scaled_dot = (scaled_dot[0] + pan_offset[0], scaled_dot[1] + pan_offset[1])
            pygame.draw.circle(window, (0, 0, 0), scaled_dot, 5)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
