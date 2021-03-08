import argparse

class CustomNumberType(object):
    """
    C checking email agains different patterns. The current available patterns is:
    RFC5322 (http://www.ietf.org/rfc/rfc5322.txt)
    """

    def __call__(self, value):
        try:
            val = int(value)
            
            if not isinstance(val, int):
                raise argparse.ArgumentTypeError("Only integers are allowed")

        except ValueError:
            raise argparse.ArgumentTypeError("Only integers are allowed")

        return val
