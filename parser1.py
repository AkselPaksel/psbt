import argparse

parser = argparse.ArgumentParser(
    prog = 'Name of program',
    description= 'Describing the program',
    epilog= 'Text at the bottom of program'
)

parser.add_argument('filename')
parser.add_argument('-c', '--count')
parser.add_argument('-v', '--verbose', action= 'store_true')

args = parser.parse_args()
print(args.filename, args.count, args.verbose)
