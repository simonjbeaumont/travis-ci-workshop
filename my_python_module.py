"""
This is a dummy python module that sleeps and prints
"""
import time


def print_n(message, count, interval=None):
    """
    Print [message] [count] times at a given [interval]
    """
    while count > 0:
        print message
        if interval:
            time.sleep(interval)
        count -= 1


if __name__ == "__main__":
    print_n("Revolt!", 10, 0.5)
