# S2-Nugget
## Repo for the esp32s2-based S2 Wi-Fi Nugget

## You can buy an S2 Nugget and support our team here: https://retia.io/products/wi-fi-nugget-s2-nugget-esp32s2

Welcome to the Github repo for the S2 Nugget! The S2 Nugget is a Wi-Fi Nugget breakout board combined with an ESP32S2 based S2 Mini development board.

<img src="https://github.com/HakCat-Tech/S2-Nugget/blob/main/nug2.png?raw=true" alt="S2 Nugget" title="S2 Nugget" width="500"/>

Because the S2 Mini is pin-compatible with the D1 Mini, the original Wi-Fi Nugget breakout board can be used to make an S2 Nugget by swapping out the D1 mini for an S2 mini.

<img src="https://github.com/HakCat-Tech/S2-Nugget/blob/main/nug3.png?raw=true" alt="S2 Nugget" title="S2 Nugget" width="500"/>

You can learn more about the ESP32s2 here: :point_right: https://www.espressif.com/en/products/socs/esp32-s2

You can learn about the S2 Mini development board here: :point_right: https://www.wemos.cc/en/latest/s2/s2_mini.html

The ESP32s2 has many advantages over the ESP8266 used in the original Wi-Fi Nugget, such as:
1) USB support, allowing you to drag and drop code to a flash drive
2) HID support, allowing you to do USB rubber ducky style attacks
3) Wi-Fi monitor mode in Python
4) Support for CircuitPython

The S2 Nugget is supported by Arduino IDE and supports MicroPython and CircuitPython.

Get started working with the S2 Nugget on the Wiki: https://github.com/HakCat-Tech/S2-Nugget/wiki

## Quickstart CircuitPython Setup Guide

<img src="https://github.com/HakCat-Tech/S2-Nugget/blob/main/nug1.png?raw=true" alt="S2 Nugget" title="S2 Nugget" width="500"/>

CircuitPython is a Python based language for controlling hardware supported by Adafruit.
The S2 Nugget supports CircuitPython, allowing users to drag and drop code onto the board to program it.

The process for setting up CircuitPython is fast, easy, and requires only a browser and Mu Editor (https://codewith.mu/)

Learn more about using the S2 Mini with CircuitPython here: :point_right: https://circuitpython.org/board/lolin_s2_mini/

## Setting up CircuitPython

### See setup video here: https://youtu.be/8JJkAxRp8cw

Thank you to Adafruit for including excellent documentation for setting up CircuitPython, some of which is copied below.

### Step 1: Set up the bootloader to enable USB support

To set up CircuitPython on the S2 Nugget, navigate here: :point_right: https://circuitpython.org/board/lolin_s2_mini/

Go to the section that says "Install, Repair, or Update UF2 Bootloader" and click the purple "Download bootloader ZIP" at the bottom.

Plug board into a USB port on your computer using a data/sync cable. Make sure it is the only board plugged in, and that a charge-only cable is not being used.

Press and hold down the BOOT or 0 button, press and release the RESET or RST button, and then release the BOOT button.

In the Chrome browser, navigate to: :point_right: https://adafruit.github.io/Adafruit_WebSerial_ESPTool/

Select 460800 Baud from the pull-down menu (top-right).

Click Connect (top-right).

Select the COM or Serial port from the pop-up window.

After successful connection, click Erase.

After successful erase, click any Choose a file..., then locate and select the combined.bin file unzipped earlier.

After successfully choosing combined.bin, click Program.

After the TinyUF2 firmware update is complete, press the RESET button on the board. A new drive BOOT should be visible in your file browser.

### Step 2: Install CircuitPython

Go back to :point_right: https://circuitpython.org/board/lolin_s2_mini/ and download the .UF2 file for the latest stable version of CircuitPython

Once the .UF2 file downloads, drag and drop it into the drive that appears when you plug in your S2 Nugget

This should automatically install CircuitPython on your S2 Nugget!

### Step 3: Programming in CircuitPython

Download and install Mu Editor from here: :point_right: https://codewith.mu/

Open Mu editor and select CircuitPython editing mode.

Name your file code.py, this will be automatically run each time the board boots.

Save your code to the board, it will automatically re-run your code each time you save changes to it.

To add files, drag and drop them from your computer to the board.

## Using the neopixel

In Mu Editor, create a new file, name it "code.py", and save it to your CIRCUITPY drive.

Copy or download the following script into your file: https://github.com/HakCat-Tech/S2-Nugget/blob/main/NeoPixelTest_CircuitPy_Nugget.py

At the bottom of the script (on lines 55-58), uncomment the function you'd like to test. 

You can choose from:


1) SetAll(r,g,b) Uncomment this to test setting all neopixels to a single color (set your own values)
2) RandomColor() Uncomment this to test setting all neopixels to random colors
3) VividColor() Uncomment this to test setting all neopixels to vivid random colors using some math
4) RandomChase() Uncomment this to test creating a racing animation for neopixel strips or rings

## Reading Wi-Fi packets

To try out Wi-Fi packet parsing, download the Wifi_Deauth_Detector_Example.zip file here: https://github.com/HakCat-Tech/S2-Nugget/blob/main/Wifi_Deauth_Detector_Example.zip

Unzip the .ZIP file, and drag and drop the contents into your CircuitPy board, overwriting the existing /lib folder and code.py

Open Code.py to see the code under the hood, otherwise the code should run and detect deauth packets with a shocked anime face.

## Controlling the screen

To try loading a bitmap on the screen, download the OLED Bitmap example here: https://github.com/HakCat-Tech/S2-Nugget/blob/main/OLED_Bitmap_Example.zip

Unzip the .ZIP file, and drag and drop the contents into your CircuitPy board, overwriting the existing /lib folder and code.py

You can drag and drop black and white .BMP images that are 128X64 onto your board and display them by changing the file path in code.py

## HID Attack Examples

The S2 Nugget supports HID attacks! You can pretend to be a keyboard or mouse to send keystrokes or control mouse movements.

To try out the HID attack examples, download the ZIP file here: https://github.com/HakCat-Tech/S2-Nugget/blob/main/HID_Examples.zip

Unzip the .ZIP file, and drag and drop the contents into your CircuitPy board, overwriting the existing /lib folder and code.py

You'll find 3 examples, which include:
* MacOS_HID_Payload - Pretends to be a keyboard, when inserted into MacOS computer, opens a terminal window and injects a payload. Currently set to "curl parrot.live" which makes a dancing parrot appear. Uses the screen on the S2 Nugget to show the status of the payload.
* Simple_HID_Payload - Bare-bones HID payload to inject keystrokes, currently set for MacOS to "curl parrot.live" which makes a dancing parrot appear.
* Mouse_Jiggler - Turns the S2 Nugget into a mouse jiggler. When the right button is pressed, the mouse is moved randomly to keep the screen from locking.

You can easily add payloads for your own operating system! To run an example, make a copy of the script and rename it "code.py", overwriting the old "code.py" file.

Your S2 Nugget will automatically reload and run the current code.py script.
