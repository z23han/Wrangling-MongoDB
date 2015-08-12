#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Let's assume that you combined the code from the previous 2 exercises
# with code from the lesson on how to build requests, and downloaded all the data locally.
# The files are in a directory "data", named after the carrier and airport:
# "{}-{}.html".format(carrier, airport), for example "FL-ATL.html".
# The table with flight info has a table class="dataTDRight".
# There are couple of helper functions to deal with the data files.
# Please do not change them for grading purposes.
# All your changes should be in the 'process_file' function
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

datadir = "data"


def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    # This is example of the data structure you should return
    # Each item in the list should be a dictionary containing all the relevant data
    # Note - year, month, and the flight data should be integers
    # You should skip the rows that contain the TOTAL data for a year
    # data = [{"courier": "FL",
    #         "airport": "ATL",
    #         "year": 2012,
    #         "month": 12,
    #         "flights": {"domestic": 100,
    #                     "international": 100}
    #         },
    #         {"courier": "..."}
    # ]
    data = []
    info = {}

    info["courier"], info["airport"] = f[:6].split("-")

    with open("{}/{}".format(datadir, f), "r") as html:

        soup = BeautifulSoup(html, "html.parser")
        data_list = []
        for table in soup.find_all("table"):
            #print(table.get('class'))
            if type(table.get('class')) == list and 'dataTDRight' in table.get('class'):
                for tr in table.find_all('tr'):
                    # Year, Month, DOMESTIC, INTERNATIONAL, TOTAL
                    innerList = []
                    for td in tr.find_all('td'):
                        if 'TOTAL' == td.text:
                            innerList = []
                            break
                        innerList.append(td.text)
                    data_list += innerList
        #print(data_list)

    #print(data_list)
    titles = ['YEAR', 'MONTH', 'DOMESTIC', 'INTERNATIONAL', 'TOTAL']
    info["courier"] = "FL"
    info["airport"] = "ATL"
    info["flights"] = {}
    for i in xrange(len(data_list)):
        if data_list[i].upper() not in titles:
            if i%5 == 0:
                info["year"] = int(data_list[i])
            elif i%5 == 1:
                info["month"] = int(data_list[i])
            elif i%5 == 2:
                digits = data_list[i].split(',')
                info["flights"]["domestic"] = int(''.join(digits))
            elif i%5 == 3:
                digits = data_list[i].split(',')
                info["flights"]["international"] = int(''.join(digits))
            else:
                pass
        if i%5 == 4:
            data.append(info)

    return data


def test():
    print "Running a simple test..."
    #open_zip(datadir)

    files = process_all(datadir)

    data = []
    for f in files:
        data += process_file(f)
    assert len(data) == 3
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    print "... success!"

if __name__ == "__main__":
    test()