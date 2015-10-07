#!/usr/bin/env/python3
#
# Demonstrates simple use of the arg parse library
#
# #

import argparse
import sys
import random


# Validate the number passed in to ensure it's reasonable and > 0
def validate_number(number):
    if number <= 0:
        return False

    return number <= 500

# Validate a min/max range
def validate_range(min,max):
    return min != max


# Print an error message and exit the program
def print_help(msg, parser):
    print(msg)

    # Print a help / usage from the arg
    parser.print_help()

    # End the the program with an exit code
    sys.exit(1)


#Determine maximum value width
def get_max_width(max):
    return len(str(max)) + 1


# Main application starting point
def main():

    # Initialize the arg parser object
    parser = argparse.ArgumentParser(description="Anthony's boilerplate script demonstrating the user of argument parsing")

    # To make this optional, set a default=blah argument
    # In this case, we're requirng a single number
    parser.add_argument('--number', '-n',
        type=int, action='store', dest='number', required=True,
        help='Number of values to generate (Max: 500)')
    parser.add_argument('--min', '-a', type=int, action='store', dest='minimum', default=0,
        help='minimum possible random integer')
    parser.add_argument('--max', '-b', type=int, action='store', dest='maximum', default=9,
        help='maximum possible random integer')

    # Parse the args!
    args = parser.parse_args()

    # Ensure the number provided is valid
    if not validate_number(args.number):
        print_help('\n\t -- Invalid number: {}\n'.format(args.number))

    # ENsure the min/max range is valid
    if not validate_range(args.minimum, args.maximum):
        print_help('\n\t -- Invalid min/max range provided!:\n\t\tMin: %d, Max: %d' % (args.minimum, args.maximum))

    # Figure out how wide to make the output
    width = get_max_width(max(abs(args.minimum),abs(args.maximum)))

    generate_numbers(args.number,args.minimum, args.maximum, width)


# Generates random numbers
def generate_numbers(count,min,max,width):
    pattern='{{:>{}}}'.format(width)

    for i in range(count):


        # "{:>5}.format(15) - results in '   15'"

        print(pattern.format(random.randint(min,max)))



# Execute the main function if called directly
if __name__ == '__main__':
    main()
