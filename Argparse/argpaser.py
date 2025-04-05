import argparse

# creating parse object
parser = argparse.ArgumentParser()

# Adding arguments 1 - help description will displayed with -h ot --help flag -> *required
parser.add_argument("path", help="Path of the file")

# Adding arguments 2 - short cmd, full cmd and action parameters
parser.add_argument("-v","--verbose",help="Verbose thingy",action="store_true")

# Adding arguments 2 - type parameters
parser.add_argument("-s",help="Square num",type= int)

# receiving arguments
arg = parser.parse_args()

# printing arg
print(arg.path)
if arg.verbose:
    print(f"{arg.path} -> {arg.v} -> {arg.s**2}")
else:
    print(f"{arg.path} -> {arg.s**2}")