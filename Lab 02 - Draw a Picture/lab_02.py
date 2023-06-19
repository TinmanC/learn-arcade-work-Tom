# import the arcade library

import arcade
import arcade.color

# open up a window
# From the "arcade" library, use a function called "open_window"
# set the window title to "Drawing Example"
# set the dimensions (width and height)
arcade.open_window(800, 800, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 799
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 799, 300, 0, arcade.csscolor.GREEN)


# Turtle Shell
# Draw an Arc
# a center of (300, 340) with a width of 240 and height of 250
# The starting angle is 0, The ending angle is 180.
arcade.draw_arc_filled(300, 340, 240, 250, arcade.csscolor.DARK_GREEN, 0, 180)

# Turtle Back Legs
# Draw Turtle Back Legs
arcade.draw_line(200, 290, 240, 345, arcade.csscolor.SADDLE_BROWN, line_width=7)

arcade.draw_line(270, 290, 240, 345, arcade.csscolor.SADDLE_BROWN, line_width=7)

# Turtle Front Legs
# Draw Turtle Front Legs

arcade.draw_line(320, 290, 360, 345, arcade.csscolor.SADDLE_BROWN, line_width=7)

arcade.draw_line(390, 290, 360, 345, arcade.csscolor.SADDLE_BROWN, line_width=7)

# Turtle Head
# Draw a Circle
arcade.draw_circle_filled(460, 340, 25, arcade.csscolor.SADDLE_BROWN)

# Turtle Neck
# Draw a Circle
arcade.draw_line(400, 350, 480, 330, arcade.csscolor.SADDLE_BROWN, line_width=16)

# Draw a Sun
arcade.draw_circle_filled(700, 750, 115, arcade.color.YELLOW)



# Rays to the left, right, up, and down


# Diagonal rays
# Diagonal rays
arcade.draw_line(700, 750, 650, 500, arcade.color.YELLOW, 3)
arcade.draw_line(700, 750, 600, 500, arcade.color.YELLOW, 3)
arcade.draw_line(700, 750, 700, 500, arcade.color.YELLOW, 3)
arcade.draw_line(700, 750, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(450, 700, 700, 700, arcade.color.YELLOW, 3)
arcade.draw_line(450, 600, 650, 700, arcade.color.YELLOW, 3)
arcade.draw_line(535, 575, 650, 700, arcade.color.YELLOW, 3)
arcade.draw_line(475, 750, 600, 730, arcade.color.YELLOW, 3)

# Finish Drawing
arcade.finish_render()

# Keep window open until it's closed
arcade.run()
