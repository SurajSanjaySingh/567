import re
import sys

for line in sys.stdin:
    print(re.sub(r'\s', '', line))