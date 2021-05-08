#!/usr/bin/python3
"""Script that takes an argument 2 strings

    - First argument is the name ot the Markdown file
    - Second argumenst is the output file name

    RequrimSents:
        - if the number of arguments is less than 2:
          print in STDERR "Usage: ./markdown2html.py README.md
          README.html and exit 1"
        - if the Markdown file doesn't exist: print in STDERR
         "Missing <filename>" and exit 1
        - otherwise, print nothing and exit 0.
"""

from sys import argv, exit, stderr
import re
from os.path import exists

def expresion(read_line, menssage):
    temp = "(0)+".replace("0", menssage)
    expr = re.match(temp, read_line)
    if expr:
        return str(expr.group())
    return None

def heading(expr1, value1, read_line1):
    level = str(len(expr1))
    op_value = value1[0].replace("0", level)
    cl_value = value1[1].replace("0", level)
    cont = "" + read_line1.replace(expr1 + " ", "")
    return op_value + cont + cl_value + "\n"

if __name__ == "__main__":

    if len(argv) <= 2:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    file1 = argv[1]
    file_exists = exists(file1)

    if file_exists is False:
        stderr.write("Missing {}\n".format(file1))
        exit(1)

    file2 = argv[2]
    menssage = {"#": ["<h0>", "</h0>"]}
    word = ''
    expr = None

    with open(file1, "r") as f:
        for read_line in f:
            for key, value in menssage.items():
                expr = expresion(read_line, key)
                if expr is None:
                    word += read_line
                    continue
                word += heading(expr, value, read_line.replace("\n", ""))

    with open(file2, "w") as new_f:
        new_f.write(word)

    exit(0)
