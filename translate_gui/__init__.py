import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

print(BASE_DIR)

sys.path.append(BASE_DIR)
print(sys.path)