# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.
import xlrd
import os
import csv
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = {}
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    TIME_index = sheet_data[0].index('Hour_End')
    COAST_index = sheet_data[0].index('COAST')
    EAST_index = sheet_data[0].index('EAST')
    FAR_WEST_index = sheet_data[0].index('FAR_WEST')
    NORTH_index = sheet_data[0].index('NORTH')
    NORTH_C_index = sheet_data[0].index('NORTH_C')
    SOUTHERN_index = sheet_data[0].index('SOUTHERN')
    SOUTH_C_index = sheet_data[0].index('SOUTH_C')
    WEST_index = sheet_data[0].index('WEST')

    coastList = []
    for i in xrange(1, len(sheet_data)):
        coastList.append(sheet_data[i][COAST_index])
    maxCoastIndex = coastList.index(max(coastList))+1
    maxCoastTime = xlrd.xldate_as_tuple(sheet_data[maxCoastIndex][TIME_index], 0)
    data['COAST'] = {
        'Max Load': str(max(coastList)),
        'Year': str(maxCoastTime[0]),
        'Month': str(maxCoastTime[1]),
        'Day': str(maxCoastTime[2]),
        'Hour': str(maxCoastTime[3])
    }

    eastList = []
    for i in xrange(1, len(sheet_data)):
        eastList.append(sheet_data[i][EAST_index])
    maxEastIndex = eastList.index(max(eastList))+1
    maxEastTime = xlrd.xldate_as_tuple(sheet_data[maxEastIndex][TIME_index], 0)
    data['EAST'] = {
        'Max Load': str(max(eastList)),
        'Year': str(maxEastTime[0]),
        'Month': str(maxEastTime[1]),
        'Day': str(maxEastTime[2]),
        'Hour': str(maxEastTime[3])
    }

    farWestList = []
    for i in xrange(1, len(sheet_data)):
        farWestList.append(sheet_data[i][FAR_WEST_index])
    maxFarWestIndex = farWestList.index(max(farWestList))+1
    maxFarWestTime = xlrd.xldate_as_tuple(sheet_data[maxFarWestIndex][TIME_index], 0)
    data['FAR_WEST'] = {
        'Max Load': str(max(farWestList)),
        'Year': str(maxFarWestTime[0]),
        'Month': str(maxFarWestTime[1]),
        'Day': str(maxFarWestTime[2]),
        'Hour': str(maxFarWestTime[3])
    }

    northList = []
    for i in xrange(1, len(sheet_data)):
        northList.append(sheet_data[i][NORTH_index])
    maxNorthIndex = northList.index(max(northList))+1
    maxNorthTime = xlrd.xldate_as_tuple(sheet_data[maxNorthIndex][TIME_index], 0)
    data['NORTH'] = {
        'Max Load': str(max(northList)),
        'Year': str(maxNorthTime[0]),
        'Month': str(maxNorthTime[1]),
        'Day': str(maxNorthTime[2]),
        'Hour': str(maxNorthTime[3])
    }

    northCList = []
    for i in xrange(1, len(sheet_data)):
        northCList.append(sheet_data[i][NORTH_C_index])
    maxNorthCIndex = northCList.index(max(northCList))+1
    maxNorthCTime = xlrd.xldate_as_tuple(sheet_data[maxNorthCIndex][TIME_index], 0)
    data['NORTH_C'] = {
        'Max Load': str(max(northCList)),
        'Year': str(maxNorthCTime[0]),
        'Month': str(maxNorthCTime[1]),
        'Day': str(maxNorthCTime[2]),
        'Hour': str(maxNorthCTime[3])
    }

    southList = []
    for i in xrange(1, len(sheet_data)):
        southList.append(sheet_data[i][SOUTHERN_index])
    maxSouthIndex = southList.index(max(southList))+1
    maxSouthTime = xlrd.xldate_as_tuple(sheet_data[maxSouthIndex][TIME_index], 0)
    data['SOUTH'] = {
        'Max Load': str(max(southList)),
        'Year': str(maxSouthTime[0]),
        'Month': str(maxSouthTime[1]),
        'Day': str(maxSouthTime[2]),
        'Hour': str(maxSouthTime[3])
    }

    southCList = []
    for i in xrange(1, len(sheet_data)):
        southCList.append(sheet_data[i][SOUTH_C_index])
    maxSouthCIndex = southCList.index(max(southCList))+1
    maxSouthCTime = xlrd.xldate_as_tuple(sheet_data[maxSouthCIndex][TIME_index], 0)
    data['SOUTH_C'] = {
        'Max Load': str(max(southCList)),
        'Year': str(maxSouthCTime[0]),
        'Month': str(maxSouthCTime[1]),
        'Day': str(maxSouthCTime[2]),
        'Hour': str(maxSouthCTime[3])
    }

    westList = []
    for i in xrange(1, len(sheet_data)):
        westList.append(sheet_data[i][WEST_index])
    maxWestIndex = westList.index(max(westList))+1
    maxWestTime = xlrd.xldate_as_tuple(sheet_data[maxWestIndex][TIME_index], 0)
    data['WEST'] = {
        'Max Load': str(max(westList)),
        'Year': str(maxWestTime[0]),
        'Month': str(maxWestTime[1]),
        'Day': str(maxWestTime[2]),
        'Hour': str(maxWestTime[3])
    }

    return data

def save_file(data, filename):
    f = open(filename, 'wb')
    try:
        writer = csv.writer(f, delimiter='|')
        writer.writerow(('Station', 'Year', 'Month', 'Day', 'Hour', 'Max Load'))
        for k,v in data.iteritems():
            writer.writerow((k, v['Year'], v['Month'], v['Day'], v['Hour'], v['Max Load']))
    finally:
        f.close()
    # YOUR CODE HERE

    
def test():
    #open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    ans = {'FAR_WEST': {'Max Load': "2281.2722140000024", 'Year': "2013", "Month": "6", "Day": "26", "Hour": "17"}}
    for k,v in ans['FAR_WEST'].iteritems():
        assert round(float(v), 5) == round(float(data['FAR_WEST'][k]), 5)

    
    fields = ["Year", "Month", "Day", "Hour", "Max Load"]
    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            s = line["Station"]
            if s == 'FAR_WEST':
                for field in fields:
                    assert round(float(ans[s][field]), 6) == round(float(line[field]), 6)


test()