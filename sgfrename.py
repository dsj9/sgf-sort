import argparse
import glob
import re
import sys

import sgfmill

"""
-r
-f format
"""

recursive = False
customFormat = False

argument_parser = argparse.ArgumentParser()

argument_parser.add_argument("-r", "--recursive", help="Recursive")
argument_parser.add_argument("-f", "--format", help="Renaming format")

arguments = argument_parser.parse_args()

print(arguments)

for file in glob.glob('*.sgf', recursive=recursive):
    print(file)
