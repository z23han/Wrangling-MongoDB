#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.
In the first exercise we want you to audit the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and the datatypes that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.

"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
          "areaLand", "areaMetro", "areaUrban"]

def audit_file(filename, fields):
    fieldtypes = {}
    f = codecs.open(filename, "r")
    reader = csv.DictReader(f)
    header = reader.fieldnames
    citiesLines = []
    for row in reader:
        citiesLines.append(row)
    for field in fields:
        if field in header:
            typeList = []
            for row in citiesLines:
                if row[field] == "" or row[field] == "NULL":
                    typeList.append(type(None))
                elif row[field].startswith('{'):
                    typeList.append(type([]))
                elif isInt(row[field]):
                    typeList.append(type(1))
                elif isFloat(row[field]):
                    typeList.append(type(1.1))
                else:
                    typeList.append(type(""))
            fieldtypes[field] = set(typeList)

    return fieldtypes

def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False



def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None), type("")])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None), type("")])
    
if __name__ == "__main__":
    test()
