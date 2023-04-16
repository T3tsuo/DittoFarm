from random import random


def three_blocks_break():
    # 0.5 - 0.52
    return random() * 0.02 + 0.5


def person_tunnel_break():
    # 3.5 - 3.52
    return random() * 0.02 + 3.5


def into_tunnel_break():
    # 1 - 1.02
    return random() * 0.02 + 1


def four_blocks():
    # 0.29 - 0.31
    return random() * 0.02 + 0.29


def align_house_break():
    # 1.45 to 1.47
    return random() * 0.02 + 1.45


def into_sign_break():
    # 0.65 to 0.67
    return random() * 0.02 + 0.65


def leave_building():
    # 1.1 seconds to 1.2 seconds to leave building
    return random() * 0.1 + 1.1


def paying_attention_break():
    # timer between 0.25 seconds to 0.50 seconds
    return random() * 0.25 + 0.25


def heal_up_break():
    # dialogue of nurse healing break from 4 seconds to 5 seconds
    return random() * 1 + 4


# break from 0.1 - 0.25 seconds
def input_break():
    return random() * 0.15 + 0.1
