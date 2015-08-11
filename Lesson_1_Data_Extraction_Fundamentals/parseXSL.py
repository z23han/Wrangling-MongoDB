#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"
import os

def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        #myzip.extractall()
        for name in myzip.namelist():
            new_dir = os.getcwd()+"\\ERCOT_DATA"
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            myzip.extract(name, new_dir)


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    # start from sheet_data[1]
    coast_data = []
    for i in xrange(1, sheet.nrows):
        coast_data.append(sheet_data[i][1])
    maxValue = max(coast_data)
    minValue = min(coast_data)
    avgValue = float(sum(coast_data))/len(coast_data)
##    time_data = []
##    yearList = []
##    for i in xrange(1, sheet.nrows):
##        time = xlrd.xldate_as_tuple(sheet_data[i][0], 0)
##        time_data.append(time)
##        yearList.append(time[0])
##    maxYear = max(yearList)
##    minYear = min(yearList)
##    underMaxYear = filter(lambda x:x[0]==maxYear, time_data[:])
##    underMinYear = filter(lambda x:x[0]==minYear, time_data[:])
##    monthList1 = []
##    monthList2 = []
##    for i in xrange(len(underMaxYear)):
##        monthList1.append(underMaxYear[i][1])
##    for i in xrange(len(underMinYear)):
##        monthList2.append(underMinYear[i][1])
##    underMaxMonth = filter(lambda x:x[0]==maxYear and x[1]==max(monthList1), time_data[:])
##    underMinMonth = filter(lambda x:x[0]==minYear and x[1]==min(monthList2), time_data[:])
##    dayList1 = []
##    dayList2 = []
##    for i in xrange(len(underMaxMonth)):
##        dayList1.append(underMaxMonth[i][2])
##    for i in xrange(len(underMinMonth)):
##        dayList2.append(underMinMonth[i][2])
##    underMaxDay = filter(lambda x:x[0]==maxYear and x[1]==max(monthList1) and x[2]==max(dayList1), time_data[:])
##    underMinDay = filter(lambda x:x[0]==minYear and x[1]==min(monthList2) and x[2]==min(dayList2), time_data[:])
##    hourList1 = []
##    hourList2 = []
##    for i in xrange(len(underMaxDay)):
##        hourList1.append(underMaxDay[i][3])
##    for i in xrange(len(underMinDay)):
##        hourList2.append(underMinDay[i][3])
##    underMaxHour = filter(lambda x:x[0]==maxYear and x[1]==max(monthList1) and x[2]==max(dayList1) and x[3]==max(hourList1), time_data[:])
##    underMinHour = filter(lambda x:x[0]==minYear and x[1]==min(monthList2) and x[2]==min(dayList2) and x[3]==min(hourList2), time_data[:])
    maxTimeData = filter(lambda x:x[1]==maxValue, sheet_data[:])[0]
    minTimeData = filter(lambda x:x[1]==minValue, sheet_data[:])[0]
    # print maxTimeData, minTimeData
    maxTimeUnit = xlrd.xldate_as_tuple(maxTimeData[0], 0)
    minTimeUnit = xlrd.xldate_as_tuple(minTimeData[0], 0)
    #minTimeUnit = xlrd.xldate_as_tuple(minTimeData[0], 0)
    #print maxTimeUnit, minTimeUnit

    ### example on how you can get the data
    #sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:", 
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):", 
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):", 
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):", 
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)
    
    
    data = {
            'maxtime': maxTimeUnit,
            'maxvalue': maxValue,
            'mintime': minTimeUnit, 
            'minvalue': minValue,
            'avgcoast': avgValue
    }
    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile)
    #print data

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()
