'''
Usage:
    md2pdf <sourcefile> <outputfile> [options]

Options:
    -h --help     show help document.
    -v --version  show version information.
    -o --output   translate sourcefile into html file.
'''

import os, re
import sys, getopt
from enum import Enum
from functools import reduce

from docopt import docopt

__version__='1.0'

class TABLE(Enum):
	Init = 1
	Format = 2
	Table = 3

class ORDERLIST(Enum):
	Init = 1
	List = 2

class BLOCK(Enum):
	Init = 1
	Block = 2
	CodeBlock = 3

#global state
table_state = TABLE.Init
orderlist_state = ORDERLIST.Init
block_state = BLOCK.Init
is_code = False
is_normal = True

temp_table_first_line = []
temp_table_first_line_str = ""

need_mathjax = False

def run(source_file, output_file):

	#check source file format
    suffix = os.path.splitext(source_file)
    if suffix not in [".md", ".markdown", ".mdown", "mkd"]:
        print('Error: the sourcefile should be in markdown format')
        sys.exit(1)

    f = open(source_file, "r")
    f_o = open(output_file, "w")

    f_o.write("""<style type="text/css">div {display: block;font-family: "Times New Roman",Georgia,Serif}\
            #wrapper { width: 100%;height:100%; margin: 0; padding: 0;}#left { float:left; \
            width: 10%;  height: 100%;  }#second {   float:left;   width: 80%;height: 100%;   \
            }#right {float:left;  width: 10%;  height: 100%; \
            }</style><div id="wrapper"> <div id="left"></div><div id="second">""")
    f_o.write("""<meta charset="utf-8"/>""")

    #parse markdown file by line
    for line in f.readlines():
    	result = parse(line)
    	if result != "":
    		f_o.write(result)

    f_o.write("""</br></br></div><div id="right"></div></div>""")

    global need_mathjax
    if need_mathjax:
    	f_r.write("""<script type="text/x-mathjax-config">\
        MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});\
        </script><script type="text/javascript" \
        src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>""")

    #close file
    f.close()
    f_o.close()

def parse(input):
	global block_state,is_normal
	is_normal = True
	result = input

	#test state
	result = test_state(input)



def test_state(input):
	global table_state, orderlist_state, block_state, is_code, temp_table_first_line, temp_table_first_line_strs

	Code_List = ["python\n", "c++\n", "c\n"]

	result = input

	#match block
	pattern = re.compile(r'```(\s)*\n')
	a = pattern.match(input)

	if a:
		print("matched")
	else:
		print("not match")

	return input

#main func
def main():
    #default output html filename
    output_file = "output.html"

    #docopt
    args = docopt(__doc__, version=__version__)
    output_file = args['<outputfile>'] if args['--output'] else output_file

    #parse sourcefile
    run(args['<sourcefile>'],output_file)

if __name__=="__main__":
    main()