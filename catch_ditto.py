import time
from random import random
import pyautogui
import pydirectinput
import requests
from PIL import Image

import random_breaks

battle_done = Image.open(requests.get("https://raw.githubusercontent.com/"
                                      "T3tsuo/DittoFarm/main/location/battle_done.png", stream=True).raw)

battle_done_2 = Image.open(requests.get("https://raw.githubusercontent.com/"
                                        "T3tsuo/DittoFarm/main/location/battle_done_2.png", stream=True).raw)

at_left_cave = Image.open(requests.get("https://raw.githubusercontent.com/"
                                       "T3tsuo/DittoFarm/main/location/at_left_cave.png", stream=True).raw)

at_right_cave = Image.open(requests.get("https://raw.githubusercontent.com/"
                                        "T3tsuo/DittoFarm/main/location/at_right_cave.png", stream=True).raw)

fight_option = Image.open(requests.get("https://raw.githubusercontent.com/"
                                       "T3tsuo/DittoFarm/main/location/fight_option.png", stream=True).raw)

run_option = Image.open(requests.get("https://raw.githubusercontent.com/"
                                     "T3tsuo/DittoFarm/main/location/run_option.png", stream=True).raw)

ditto_png = Image.open(requests.get("https://raw.githubusercontent.com/"
                                    "T3tsuo/DittoFarm/main/location/ditto.png", stream=True).raw)

horde_png = Image.open(requests.get("https://raw.githubusercontent.com/"
                                    "T3tsuo/DittoFarm/main/battle_logs/horde.png", stream=True).raw)

right_left_move = "right"


def search_wild_pokemon():
    global right_left_move
    print("Searching for Pokemon")
    pydirectinput.keyDown(right_left_move)
    time.sleep(random_breaks.input_break())
    while True:
        if pyautogui.locateOnScreen(at_left_cave, confidence=0.8) is not None and right_left_move == "left":
            pydirectinput.keyUp(right_left_move)
            time.sleep(random_breaks.input_break())
            right_left_move = "right"
            pydirectinput.keyDown(right_left_move)
            print("Right")
        elif pyautogui.locateOnScreen(at_right_cave, confidence=0.8) is not None and right_left_move == "right":
            pydirectinput.keyUp(right_left_move)
            time.sleep(random_breaks.input_break())
            right_left_move = "left"
            pydirectinput.keyDown(right_left_move)
            print("Left")
        if pyautogui.locateOnScreen(battle_done, confidence=0.8) is None and \
                pyautogui.locateOnScreen(battle_done_2, confidence=0.8) is None:
            pydirectinput.keyUp(right_left_move)
            print("In Battle")
            time.sleep(random_breaks.input_break())
            return


def in_battle():
    # wait until battle
    while True:
        if pyautogui.locateOnScreen(fight_option, confidence=0.8) is not None:
            break
        else:
            time.sleep(0.1)
    # check first if it's a ditto, then horde, then others
    if pyautogui.locateOnScreen(ditto_png, confidence=0.8) is not None:
        print("Ditto")
    elif pyautogui.locateOnScreen(horde_png) is not None:
        print("Horde")
    else:
        print("Others")
    run_away()


def run_away():
    while True:
        if pyautogui.locateOnScreen(run_option, confidence=0.8) is not None:
            location = pyautogui.locateOnScreen(run_option,
                                                confidence=0.8)
            pyautogui.moveTo(location.left + random() * location.width,
                             location.top + random() * location.height)
            pydirectinput.click()
            print("Run Away")
        elif pyautogui.locateOnScreen(battle_done, confidence=0.8) is not None or \
                pyautogui.locateOnScreen(battle_done_2, confidence=0.8) is not None:
            # ran away successfully
            time.sleep(random_breaks.input_break())
            break
        else:
            time.sleep(0.1)


def run():
    while True:
        search_wild_pokemon()
        in_battle()
