# S2 Nugget Neopixel Test Sketch
# This sketch is written to test the built-in neopixel on the S2 Nugget, or an attached neopixel strip
import board
import neopixel
import random
import time
import math

## Setup section: Here we create a pixel object, define the number of pixels, and set a delay for our animations

pixel_pin = board.IO12    # Specify the pin that the neopixel is connected to (GPIO 12)
num_pixels = 1 # Set number of neopixels (1 if just using the built in neopixel)
delay = .3   # & delay between color changes in seconds
pixel = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.10)   # Create neopixel and set brightness to 10%

## Let's create a function to set all neopixels to whatever color we want!

def SetAll(color):   # Define function with one input (color we want to set)
    for i in range(0, num_pixels):   # Addressing all neopixels in a loop
        pixel[i] = (color)   # Set all neopixels a color

## Next, let's create a random color using the random function

def RandomColor():   # First, we create a function to turn all pixels a random color. This works with one pixel or a strip of them.
    for i in range(0, num_pixels):   # Addressing all neopixels one by one in a loop
        color = (random.randint(0,100), random.randint(0,100), random.randint(0,100))   # Create a random color, set max to 100 to avoid super bright pixels
        pixel[i] = (color)   # Set the neopixel to the random color
        time.sleep(delay) # Set a short delay between color changes

## Cool, but the colors are a little dull. Let's use sine & cosine to create super saturated colors!

def VividColor():  # We define the function
    for i in range(0, num_pixels):  # Go over all neopixels in a loop one by one
        x = random.randint(0, 100)  # Set a random number from 0 to 100
        colors = [0, int(255*math.cos(x)), int(255*math.sin(x))] # Create a group of color values to pick from randomly
        r = colors.pop(random.randint(0, len(colors)-1)) # Pick the value for red from a random position in the group of colors
        g = colors.pop(random.randint(0, len(colors)-1)) # Pick the value for green from a random position in the group of colors
        b = colors.pop() # Pick the value for blue from the last remaining value in the group of colors we created
        pixel[i] = ([r, g, b]) # Set the current neopixel to the random color we created
        time.sleep(delay) # Set a short delay between color changes

## Looks great! If we have a neopixel strip, let's make a racing animation with random colors

def RandomChase():   # First we define the function
    for i in range(0, num_pixels):   # Addressing all neopixels in a loop
        color = (random.randint(0,100), random.randint(0,100), random.randint(0,100))   # Create a random color
        pixel[i] = (color)   # Set the neopixel to the random color
        pixel[(i-1)] = (0,0,0)   # Turn the neopixel before the random colored one off
        time.sleep(delay)   # Make a brief delay before running the loop again
        SetAll((0, 0, 0))



while True:
    #SetAll([0,255,0])  # Uncomment this to test setting all neopixels to a single color
    #RandomColor() # Uncomment this to test setting all neopixels to random colors
    VividColor() # Uncomment this to test setting all neopixels to vivid random colors using some math
    #RandomChase() # Uncomment this to test creating a racing animation for neopixel strips
