import argparse
import glob
import re
import sys
from string import Template

import sgfmill

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("-r", "--recursive", action='store_true', help="Search folders recursively")
argument_parser.add_argument("-f", "--format", help="Renaming format")

options = vars(argument_parser.parse_args())

template = Template(options.format)

for file in glob.glob('*.sgf', recursive=options['recursive']):
    print(file)
