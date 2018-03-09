# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
import click
from utils import *
click.disable_unicode_literals_warning=True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for led_tester."""
    print("input: ", input)
    print()
    info = parseFile(input)
    N=info[0]
    instructions=info[1]
    lighttest=LightTester(N)
    lighttest.apply(instructions)
    print('NO OF LIGHTS NOW ON IS: ', lighttest.count())


main()

# if __name__ == "__main__":
#     sys.exit(main()) # pragma: no cover 
