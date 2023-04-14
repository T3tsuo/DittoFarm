import time
import pyautogui
import pydirectinput
import requests
from PIL import Image

import random_breaks
from catch_ditto import in_battle

outside_building = Image.open(requests.get("https://raw.githubusercontent.com/T3tsuo/DittoFarm/"
                                           "main/images/location/outside_building.png", stream=True).raw)

inside_house = Image.open(requests.get("https://raw.githubusercontent.com/"
                                       "T3tsuo/DittoFarm/main/images/location/inside_house.png", stream=True).raw)

inside_tunnel = Image.open(requests.get("https://raw.githubusercontent.com/"
                                        "T3tsuo/DittoFarm/main/images/location/inside_tunnel.png", stream=True).raw)

battle_done = Image.open(requests.get("https://raw.githubusercontent.com/"
                                      "T3tsuo/DittoFarm/main/images/location/battle_done.png", stream=True).raw)

battle_done_2 = Image.open(requests.get("https://raw.githubusercontent.com/"
                                        "T3tsuo/DittoFarm/main/images/location/battle_done_2.png", stream=True).raw)

run_option = Image.open(requests.get("https://raw.githubusercontent.com/"
                                     "T3tsuo/DittoFarm/main/images/in_battle_options/run_option.png", stream=True).raw)


def wait_until_see(img, msg):
    while True:
        if pyautogui.locateOnScreen(img, confidence=0.8) is not None:
            # inside the house
            print(msg)
            break
        else:
            time.sleep(0.1)


def leave_building():
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.leave_building())
    pydirectinput.keyUp("down")
    # while cannot find outside, keep on waiting
    wait_until_see(outside_building, "Left Building")
    time.sleep(random_breaks.input_break())


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
    wait_until_see(inside_house, "Inside House")
    time.sleep(random_breaks.input_break())


def go_into_tunnel():
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.into_tunnel_break())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())
    wait_until_see(inside_tunnel, "Inside Tunnel")
    time.sleep(random_breaks.input_break())


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
    wait_until_see(battle_done, "Inside Cave")
    time.sleep(random_breaks.input_break())
    # hop on bike
    pydirectinput.press("1")
    print("Bicycle")
    time.sleep(random_breaks.input_break())
    # go up by two
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("up")
    time.sleep(3)
    # check to see if we're in a battle
    while True:
        if pyautogui.locateOnScreen(battle_done, confidence=0.8) is None and \
                pyautogui.locateOnScreen(battle_done, confidence=0.8) is None:
            in_battle()
            # ran away successfully
            time.sleep(random_breaks.input_break())
        else:
            break
    pydirectinput.press("up")
    pydirectinput.PAUSE = 0.1
    time.sleep(random_breaks.input_break())


def run():
    leave_building()
    go_to_house()
    go_into_tunnel()
    go_into_cave()
