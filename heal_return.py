import time

import pyautogui
import pydirectinput
import requests
from PIL import Image

import random_breaks

outside_building = Image.open(requests.get("https://raw.githubusercontent.com/"
                                           "T3tsuo/DittoFarm/main/location/outside_building.png", stream=True).raw)

inside_house = Image.open(requests.get("https://raw.githubusercontent.com/"
                                       "T3tsuo/DittoFarm/main/location/inside_house.png", stream=True).raw)

inside_tunnel = Image.open(requests.get("https://raw.githubusercontent.com/"
                                        "T3tsuo/DittoFarm/main/location/inside_tunnel.png", stream=True).raw)

inside_cave = Image.open(requests.get("https://raw.githubusercontent.com/"
                                      "T3tsuo/DittoFarm/main/location/inside_cave.png", stream=True).raw)


def leave_building():
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.leave_building())
    pydirectinput.keyUp("down")
    # while cannot find outside, keep on waiting
    is_outside = False
    while is_outside is False:
        # if image recognition detects that we left the building
        if pyautogui.locateOnScreen(outside_building, confidence=0.8) is not None:
            # then we are outside
            print("Left Building")
            is_outside = True
            time.sleep(0.5)
        else:
            time.sleep(0.5)


def go_to_house():
    # hop on bike
    pydirectinput.press("1")
    print("Bicycle")
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("left")
    time.sleep(random_breaks.into_sign_break())
    pydirectinput.keyUp("left")
    time.sleep(random_breaks.input_break())
    # go down
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("down")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("down")
    pydirectinput.PAUSE = 0.1
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("left")
    time.sleep(random_breaks.align_house_break())
    pydirectinput.keyUp("left")
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.four_blocks())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    while True:
        if pyautogui.locateOnScreen(inside_house, confidence=0.8) is not None:
            # inside the house
            print("Inside House")
            time.sleep(random_breaks.input_break())
            break
        else:
            time.sleep(0.1)


def go_into_tunnel():
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.into_tunnel_break())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    while True:
        if pyautogui.locateOnScreen(inside_tunnel, confidence=0.8) is not None:
            # inside the house
            print("Inside Tunnel")
            time.sleep(random_breaks.input_break())
            break
        else:
            time.sleep(0.1)


def go_into_cave():
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.person_tunnel_break())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("left")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("left")
    pydirectinput.PAUSE = 0.1
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.three_blocks_break())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("right")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("right")
    pydirectinput.PAUSE = 0.1
    time.sleep(random_breaks.input_break())
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("up")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("up")
    pydirectinput.PAUSE = 0.1
    time.sleep(random_breaks.input_break())
    while True:
        if pyautogui.locateOnScreen(inside_cave, confidence=0.8) is not None:
            # inside the house
            print("Inside Cave")
            time.sleep(random_breaks.input_break())
            break
        else:
            time.sleep(0.1)


def run():
    leave_building()
    go_to_house()
    go_into_tunnel()
    go_into_cave()


time.sleep(2)
run()
