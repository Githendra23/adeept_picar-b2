import time
import sys

previous_time = 0

def delay(ms):
    global previous_time
    current_time = time.time() * 1000

    if current_time >= previous_time + ms:
        previous_time = current_time
        return True

    return False

sys.modules[__name__] = delay