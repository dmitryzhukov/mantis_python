import string
import random


def random_string(prefix: string, max_length: int) -> string:
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])
