Methods to create a parser


Using sys.argv
Using getopt
Using argparse


Understand argument parsing


## Understand argpraser


Positional arguments
Optional arguments


positional arguments


## Actions

- store stores the input value to the Namespace object. (This is the default action.)
- store_const stores a constant value when the corresponding optional arguments are specified.
- store_true stores the Boolean value True when the corresponding optional argument is specified and stores a False elsewhere.
- store_false stores the Boolean value False when the corresponding optional argument is specified and stores True elsewhere.
append stores a list, appending a value to the list each time the option is provided.
append_const stores a list appending a constant value to the list each time the option is provided.
count stores an int that is equal to the times the option has been provided.
help shows a help text and exits.
version shows the version of the program and exits.

