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
from os.path import exists

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
    with open(file1, "r") as f:
        menssage = 0
        for r in f:
            count = 0

            if "#" in r:
                s = r
                for i in s:
                    if i == "#":
                        count += 1
            word = "<h{0}>{1}</h{0}>\n".format(count, r[count + 1:].
                                               replace("\n", ""))

            fe = open(file2, 'a', encoding="utf-8")
            fe.write(word)
            menssage += 1
    exit(0)
