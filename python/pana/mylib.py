import sys


def get_time_stamp():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
