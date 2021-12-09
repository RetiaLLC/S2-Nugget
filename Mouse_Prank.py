import usb_hid # HID Mouse Prank Code To Make Computer Box Terrible To Use 
from adafruit_hid.mouse import Mouse
import time, random
minDelay = 1; maxDelay = 3 ## What is the minimum and maximum delay?
baseline = time.monotonic() ## Take a baseline time measurement to compare later
m = Mouse(usb_hid.devices) ## Create the mouse object

def slamCorner():
    print('Corner slam')
    for i in range(50): m.move(x=-1000, y=-1000) ## Move the mouse up and to the left

def randomClick():
    print('Double click')
    m.click(Mouse.LEFT_BUTTON); m.click(Mouse.LEFT_BUTTON)

def yeet():
    print('Grab & yeet')
    m.press(Mouse.LEFT_BUTTON); m.move(x=-1000, y=-1000); m.release_all()

def getRandomTime(): return (random.randint(minDelay, maxDelay)) ## Returns random time delay between min and max

def somethingBad(badThing): yeet() if badThing == 0 else randomClick() if badThing == 1 else slamCorner()

timeInterval = getRandomTime() ## Grab a random interval from our minimum to maximum possible delay

while True:
    if (time.monotonic() - baseline) > timeInterval: ## Check if the time is past our random delay
        somethingBad(random.randint(0,2)) ## Do a random bad thing
        baseline = time.monotonic(); timeInterval = getRandomTime() ## Reset our timer for the next delay and pick a new random time interval
        print('going again in', timeInterval)
