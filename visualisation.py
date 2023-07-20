import pygame
import Crypto.Random.random as random

# Constant for the maximum coordinate value
MAX_NUM = 24

# Function to scale points based on window size and zoom level
def scale_point(point, window_size, zoom_level):
    x, y = point
    max_width, max_height = window_size
    scaled_x = int((x / MAX_NUM) * max_width * zoom_level)
    scaled_y = int((y / MAX_NUM) * max_height * zoom_level)
    return scaled_x, scaled_y

# Function to limit the zoom level within a range
def limit_zoom(zoom_level):
    return max(1.0, min(5.0, zoom_level))

# Function to limit panning within the array bounds
def limit_panning(pan_offset, window_size, zoom_level):
    max_x = int((MAX_NUM / MAX_NUM) * window_size[0] * zoom_level)
    max_y = int((MAX_NUM / MAX_NUM) * window_size[1] * zoom_level)
    min_x = window_size[0] - max_x
    min_y = window_size[1] - max_y

    pan_offset[0] = max(min_x, min(0, pan_offset[0]))
    pan_offset[1] = max(min_y, min(0, pan_offset[1]))
    return pan_offset

def main():
    # Initialize pygame
    pygame.init()

    # Set the initial window dimensions
    initial_width, initial_height = 800, 600

    # Create the window
    window = pygame.display.set_mode((initial_width, initial_height), pygame.RESIZABLE)
    pygame.display.set_caption("Resizable Window with Dots")

    # List comprehension to generate the specific dots' coordinates
    dots_coordinates = [[x, MAX_NUM - x] for x in range(0, MAX_NUM)]

    # Zoom level variable
    zoom_level = 1.0

    # Initial panning offset
    pan_offset = [0, 0]

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                # Handle window resize event
                window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Zoom in and out with the mouse wheel
                if event.button == 4:  # Mouse wheel up
                    zoom_level += 0.1
                elif event.button == 5:  # Mouse wheel down
                    zoom_level -= 0.1
                    zoom_level = limit_zoom(zoom_level)
            elif event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                # Pan the content while left mouse button is held down
                pan_offset[0] += event.rel[0]
                pan_offset[1] += event.rel[1]
                pan_offset = limit_panning(pan_offset, (window.get_width(), window.get_height()), zoom_level)

        # Clear the window
        window.fill((255, 255, 255))

        # Draw the scaled dots on the window with panning offset
        for dot_coords in dots_coordinates:
            scaled_dot = scale_point(dot_coords, (window.get_width(), window.get_height()), zoom_level)
            scaled_dot = (scaled_dot[0] + pan_offset[0], scaled_dot[1] + pan_offset[1])
            pygame.draw.circle(window, (0, 0, 0), scaled_dot, 5)

        # Update the display
        pygame.display.flip()

    # Quit pygame when the loop is finished
    pygame.quit()

if __name__ == "__main__":
    main()
