#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

import xml.etree.ElementTree as ET
PATENTS = 'patent.data'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def split_file(filename):
    # we want you to split the input file into separate files
    # each containing a single patent.
    # As a hint - each patent declaration starts with the same line that was causing the error
    # The new files should be saved with filename in the following format:
    # "{}-{}".format(filename, n) where n is a counter, starting from 0.
    f = open(filename, "r")

    n = 0
    newFileName = "{}-{}".format(filename, n)
    f1 = open(newFileName, "w")
    start = 0
    for line in f:
        if line.startswith("<?xml") and start == 1:
            f1.close()
            n += 1
            newFileName = "{}-{}".format(filename, n)
            f1 = open(newFileName, "w")
        f1.write(line)
        if start == 0:
            start = 1
    f1.close()
    f.close()

    return


def test():
    #get_root(PATENTS)
    split_file(PATENTS)

    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)



test()