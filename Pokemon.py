import time
import numpy as np
import sys

def delay_print(s):

  for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
