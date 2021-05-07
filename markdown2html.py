#!/usr/bin/python3
from sys import argv, exit, stderr
from os.path import exists

file1 = argv[1]
file_exists = exists(file1)


if len(argv) <= 2:
    stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    exit(1)

elif file_exists == False:
    stderr.write("Missing {}\n".format(file1))
    exit(1)

else:
    exit(0)

