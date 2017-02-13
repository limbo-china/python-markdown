'''
Usage:
    md2pdf <sourcefile> <outputfile> [options]

Options:
    -h --help     show help document.
    -v --version  show version information.
    -o --output   translate sourcefile into html file.
    -p --print    translate sourcefile into pdf file and html file respectively.
    -P --Print    translate sourcefile into pdf file only.
'''

import os, re
import sys, getopt
from enum import Enum
from subprocess import call
from functools import reduce

from docopt import docopt

__version__='1.0'

#main func
def main():
    #default output html filename
    output_file = "output.html"
    
    #default output pdf filename
    output_pdf_file ="output.pdf"

    #pdf only
    only_pdf = False

    #docopt
    args = docopt(__doc__, version=__version__)
    output_file = args['<outputfile>'] if args['--output'] else output_file
    output_pdf_file = args['<outputfile>'] if args['--print'] or args['--Print'] else ""

    #parse sourcefile
    run(args['<sourcefile>'],output_file,output_pdf_file,args['--Print'])

if __name__=="__main__"
    main()