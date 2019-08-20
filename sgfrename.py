import sgfmill
import glob
import sys

"""
-r
-f format
"""

for argument in sys.argv:
    print(argument)

for file in glob.glob('*.sgf'):
    print(file)
