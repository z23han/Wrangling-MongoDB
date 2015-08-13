#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the "areaLand" field,
you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it has to return a float
representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you like, but changes to process_file
will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'


def fix_area(area):

    # YOUR CODE HERE
    if area == 'NULL':
        return None
    elif area.startswith('{'):
        area = area.replace('{', '')
        if area.endswith('}'):
            area = area.replace('}', '')
        dataList = area.split('|')
        retArea = ''
        for data in dataList:
            if len(data) > len(retArea):
                retArea = str(data)
        return float(retArea)
    else:
        return float(area)


global_name = ['areaLand', 'name', 'areaMetro', 'populationTotal', 'postalCode']

def process_file(filename, key):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra matadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if key in line:
                line[key] = fix_area(line[key])
            data.append(line)

    return data


def test():
    nameNum = 0
    data = process_file(CITIES, global_name[nameNum])

    print "Printing three example results:"
    for n in range(5,8):
        pprint.pprint(data[n][global_name[nameNum]])

    #assert data[8][global_name[1]] == 55166700.0
    #assert data[3][global_name[1]] == None


if __name__ == "__main__":
    test()