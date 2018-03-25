#encoding=utf-8

"""Naval Fate
Create *beautiful* command-line interfaces with python

Usage:
    naval_fate.py ship new <name>...
    naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
    naval_fate.py ship shoot <x> <y>
    naval_fate.py mine (set|remove) <x> <y> [--moored | --drifting]
    naval_fate.py (-h | --help)
    naval_fate.py --version
Options:
    -h --help       Show this screen.
    --version       Show version.
    --speed=<kn>    Speed in knots [default:10].
    --moored        Moored (anchred) mine.
    --drifting      Drifting mine.

"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)