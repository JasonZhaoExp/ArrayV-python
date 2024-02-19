import pygame
import colorsys

MAX_NUM = 2048
dots_coordinates = [[x, MAX_NUM - x] for x in range(0, MAX_NUM)]

def scale_point(point, window_size, zoom_level):
    x, y = point
    max_width, max_height = window_size
    scaled_x = int((x / MAX_NUM) * max_width * zoom_level)
    scaled_y = int((y / MAX_NUM) * max_height * zoom_level)
    return scaled_x, scaled_y

def limit_zoom(zoom_level):
    return max(1.0, min(100.0, zoom_level))

def limit_panning(pan_offset, window_size, zoom_level):
    max_x = int((MAX_NUM / MAX_NUM) * window_size[0] * zoom_level)
    max_y = int((MAX_NUM / MAX_NUM) * window_size[1] * zoom_level)
    min_x = window_size[0] - max_x
    min_y = window_size[1] - max_y

    # Limit panning to stay within the visible area boundaries
    pan_offset[0] = max(min_x, min(pan_offset[0], 0))
    pan_offset[1] = max(min_y, min(pan_offset[1], 0))

    return pan_offset


def get_color(index, total_dots):
    hue = (360 / total_dots) * index
    rgb = colorsys.hsv_to_rgb(hue / 360, 1.0, 1.0)
    scaled_rgb = tuple(int(c * 255) for c in rgb)
    return scaled_rgb

def main():
    pygame.init()
    initial_width, initial_height = 800, 600
    window = pygame.display.set_mode((initial_width, initial_height), pygame.RESIZABLE)
    pygame.display.set_caption("Visualisation")
    font = pygame.font.SysFont(None, 30)
    global dots_coordinates
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
                if event.button == 4:  # Scroll up to zoom in
                    old_zoom = zoom_level
                    zoom_level += 0.1
                    zoom_level = limit_zoom(zoom_level)
                    # Adjust the panning offset based on cursor position before and after zooming
                    pan_offset[0] = event.pos[0] - (event.pos[0] - pan_offset[0]) * (zoom_level / old_zoom)
                    pan_offset[1] = event.pos[1] - (event.pos[1] - pan_offset[1]) * (zoom_level / old_zoom)
                    # Update the panning limits after zooming
                    pan_offset = limit_panning(pan_offset, (window.get_width(), window.get_height()), zoom_level)
                elif event.button == 5:  # Scroll down to zoom out
                    old_zoom = zoom_level
                    zoom_level -= 0.1
                    zoom_level = limit_zoom(zoom_level)
                    # Adjust the panning offset based on cursor position before and after zooming
                    pan_offset[0] = event.pos[0] - (event.pos[0] - pan_offset[0]) * (zoom_level / old_zoom)
                    pan_offset[1] = event.pos[1] - (event.pos[1] - pan_offset[1]) * (zoom_level / old_zoom)
                    # Update the panning limits after zooming
                    pan_offset = limit_panning(pan_offset, (window.get_width(), window.get_height()), zoom_level)
            elif event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                pan_offset[0] += event.rel[0]
                pan_offset[1] += event.rel[1]
                pan_offset = limit_panning(pan_offset, (window.get_width(), window.get_height()), zoom_level)

        window.fill((255, 255, 255))

        total_dots = len(dots_coordinates)
        rainbow_colors = [get_color(idx, total_dots) for idx in range(total_dots)]

        # Calculate the center of the window in the original coordinate system
        center_window_original = (
            (window.get_width() // 2 - pan_offset[0]) // zoom_level,
            (window.get_height() // 2 - pan_offset[1]) // zoom_level
        )

        # Update the scaled center based on the latest center of the window
        scaled_center_window = scale_point(center_window_original, (window.get_width(), window.get_height()), zoom_level)
        scaled_center_window = (scaled_center_window[0] + pan_offset[0], scaled_center_window[1] + pan_offset[1])

        for idx, dot_coords in enumerate(dots_coordinates):
            scaled_dot = scale_point(dot_coords, (window.get_width(), window.get_height()), zoom_level)
            scaled_dot = (scaled_dot[0] + pan_offset[0], scaled_dot[1] + pan_offset[1])
            colour = rainbow_colors[idx]
            pygame.draw.circle(window, colour, scaled_dot, 5)

        # Display the zoom percentage and center coordinates relative to the points
        zoom_text = f"Zoom: {zoom_level:.2f}x"
        zoom_surface = font.render(zoom_text, True, (0, 0, 0))
        window.blit(zoom_surface, (10, 10))

        center_text = f"Center Coords: ({center_window_original[0]}, {center_window_original[1]})"
        center_surface = font.render(center_text, True, (0, 0, 0))
        window.blit(center_surface, (10, 40))

        # Render a small 'x' in the middle of the screen
        x_size = 10
        x_color = (255, 0, 0)  # Red color
        pygame.draw.line(window, x_color, (window.get_width() // 2 - x_size, window.get_height() // 2),
                         (window.get_width() // 2 + x_size, window.get_height() // 2), 2)
        pygame.draw.line(window, x_color, (window.get_width() // 2, window.get_height() // 2 - x_size),
                         (window.get_width() // 2, window.get_height() // 2 + x_size), 2)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()