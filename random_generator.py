# random_generator.py

import random

def generate_random_numbers(count, start, end):

    random_numbers = [random.randint(start, end) for _ in range(count)]
    return random_numbers