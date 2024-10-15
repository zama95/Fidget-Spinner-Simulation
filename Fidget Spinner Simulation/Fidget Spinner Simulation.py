import pygame
import sys
from math import *

# Initialization of Pygame Window
pygame.init()

width = 900
height = 700

display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Fidget Spinner Simulation")

# Colors
background = (51, 51, 51)
white = (240, 240, 240)
red = (176, 58, 46)
dark_red = (120, 40, 31)
dark_gray = (23, 32, 42)
blue = (40, 116, 166)
dark_blue = (26, 82, 118)
yellow = (183, 149, 11)
dark_yellow = (125, 102, 8)
green = (29, 131, 72)
dark_green = (20, 90, 50)
orange = (230, 126, 34)
dark_orange = (126, 81, 9)

# Close the Pygame Window
def close():
    pygame.quit()
    sys.exit()

# Function to display custom instructions
def show_instructions():
    # Create a regular font
    font_regular = pygame.font.SysFont("Times New Roman", 18)
    # Create a bold font
    font_bold = pygame.font.SysFont("Times New Roman", 18, bold=True, italic=True)

    # Render the instruction text with bold for the first two instructions
    instruction1 = font_bold.render("Starting in 10 seconds. Please read this message.", True, white)
    instruction2 = font_bold.render("Dear, this is a mini project I created in my FY BSc CS to learn Python.", True, white)
    
    # Render the remaining instructions with the regular font
    instruction3 = font_regular.render("Use the LEFT and RIGHT arrow keys to spin.", True, red)
    instruction4 = font_regular.render("Press SPACE to change color", True, red)
    
    # Calculate y positions for centering vertically
    y_positions = [100, 130, 160, 190]  # Adjust vertical spacing as needed

    # Center and display each instruction
    display.blit(instruction1, ((width - instruction1.get_width()) // 2, y_positions[0]))
    display.blit(instruction2, ((width - instruction2.get_width()) // 2, y_positions[1]))
    display.blit(instruction3, ((width - instruction3.get_width()) // 2, y_positions[2]))
    display.blit(instruction4, ((width - instruction4.get_width()) // 2, y_positions[3]))

    pygame.display.update()
    pygame.time.delay(10000)  # Display instructions for 10 seconds


# Drawing of Fidget Spinner on Pygame Window
def show_spinner(angle, color, dark_color):
    d = 80
    innerd = 50
    x = width / 2 - d / 2
    y = height / 2
    l = 200
    r = l / (3**0.5)
    lw = 60

    # Calculate positions of the spinner arms
    centre = [x, y, d, d]
    centre_inner = [x + d / 2 - innerd / 2, y + d / 2 - innerd / 2, innerd, innerd]

    top = [x + r * cos(radians(angle)), y + r * sin(radians(angle)), d, d]
    top_inner = [x + d / 2 - innerd / 2 + r * cos(radians(angle)),
                 y + d / 2 - innerd / 2 + r * sin(radians(angle)), innerd, innerd]

    left = [x + r * cos(radians(angle - 120)), y + r * sin(radians(angle - 120)), d, d]
    left_inner = [x + d / 2 - innerd / 2 + r * cos(radians(angle - 120)),
                  y + d / 2 - innerd / 2 + r * sin(radians(angle - 120)), innerd, innerd]

    right = [x + r * cos(radians(angle + 120)), y + r * sin(radians(angle + 120)), d, d]
    right_inner = [x + d / 2 - innerd / 2 + r * cos(radians(angle + 120)),
                   y + d / 2 - innerd / 2 + r * sin(radians(angle + 120)), innerd, innerd]

    # Draw spinner arms
    pygame.draw.line(display, dark_color, (top[0] + d / 2, top[1] + d / 2), (centre[0] + d / 2, centre[1] + d / 2), lw)
    pygame.draw.line(display, dark_color, (left[0] + d / 2, left[1] + d / 2), (centre[0] + d / 2, centre[1] + d / 2), lw)
    pygame.draw.line(display, dark_color, (right[0] + d / 2, right[1] + d / 2), (centre[0] + d / 2, centre[1] + d / 2), lw)

    # Draw spinner circles
    pygame.draw.ellipse(display, color, tuple(centre))
    pygame.draw.ellipse(display, dark_color, tuple(centre_inner))
    pygame.draw.ellipse(display, color, tuple(top))
    pygame.draw.ellipse(display, dark_gray, tuple(top_inner), 10)
    pygame.draw.ellipse(display, color, tuple(left))
    pygame.draw.ellipse(display, dark_gray, tuple(left_inner), 10)
    pygame.draw.ellipse(display, color, tuple(right))
    pygame.draw.ellipse(display, dark_gray, tuple(right_inner), 10)

# Displaying Information on Pygame Window
def show_info(friction, speed):
    font = pygame.font.SysFont("Times New Roman", 18)
    frictionText = font.render(f"Friction : {friction:.2f}", True, white)
    speedText = font.render(f"Rate of Change of Angle : {speed:.2f}", True, white)
    display.blit(speedText, (15, 15))
    display.blit(frictionText, (15, 45))

# The Main Function
def spinner():
    spin = True
    angle = 0
    speed = 0.0
    friction = 0.03
    rightPressed = False
    leftPressed = False
    direction = 1

    color = [[red, dark_red], [blue, dark_blue], [yellow, dark_yellow], [green, dark_green], [orange, dark_orange]]
    index = 0

    # Show instructions at the beginning
    show_instructions()

    while spin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_RIGHT:
                    rightPressed = True
                    direction = 1
                if event.key == pygame.K_LEFT:
                    leftPressed = True
                    direction = -1
                if event.key == pygame.K_SPACE:
                    index = (index + 1) % len(color)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    rightPressed = False
                if event.key == pygame.K_LEFT:
                    leftPressed = False

        # Update speed based on input
        if rightPressed:
            speed += 0.3
        elif leftPressed:
            speed -= 0.3
        else:
            speed -= friction * direction
            if speed * direction < 0:
                speed = 0.0

        # Update the rotation angle
        angle += speed

        # Clear the display
        display.fill(background)

        # Display the spinner and information
        show_spinner(angle, color[index][0], color[index][1])
        show_info(friction, speed)

        pygame.display.update()
        clock.tick(90)

# Run the spinner simulation
spinner()
