import time
import os

import catch_ditto
import heal_return

os.environ['REQUESTS_CA_BUNDLE'] = "certifi/cacert.pem"


def run(ball_num=None):
    if ball_num is None:
        ball_num = input("How many dusk balls do you have (number): ")
    ball_num = int(ball_num)
    time.sleep(2)
    # loop forever
    while True:
        heal_return.run()
        ball_num = catch_ditto.run(ball_num)
