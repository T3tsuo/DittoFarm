import time
import os

import catch_ditto
import heal_return

os.environ['REQUESTS_CA_BUNDLE'] = "certifi/cacert.pem"


def run():
    time.sleep(2)
    # loop forever
    while True:
        heal_return.run()
        catch_ditto.run()


run()

