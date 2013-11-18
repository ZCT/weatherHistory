#!/usr/bin/python
# coding:utf-8
import json
import re
import urllib2
from bs4 import BeautifulSoup
import datetime
from DateToWeekDay import writeExcelFile

__author__ = 'ZrongH'


def loadHistoryWeatherHTML(historyMonth):
    URL = r'http://lishi.tianqi.com/guangzhou/%s.html'
    HistoryWeatherHTMLURL = urllib2.Request(URL % str(historyMonth))
    HistoryWeatherHTMLURL.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
    HistoryWeatherHTMLContent = urllib2.urlopen(HistoryWeatherHTMLURL, timeout=20).read()
    return HistoryWeatherHTMLContent


def loadWeatherDetail(HistoryWeatherHTMLContent):
    soup = BeautifulSoup(HistoryWeatherHTMLContent)
    AllMonthDetail = []
    for div in soup.find_all('div', {'class': 'tqtongji2'}):
        ul = div.findAll('ul')
        ul = ul[1:]
        for oneDay in ul:
            li = oneDay.findAll('li')
            # print li[0].string, int(str(li[1].string)) , int(str(li[2].string))
            averTemp = (int(str(li[1].string)) + int(str(li[2].string)))/2.0
            # oneMonthDetail = li[0].string + ' ' + li[3].string + ' ' +loadDateString(li[0].string) + '\r\n'
            oneMonthDetail = li[0].string + ' ' + str(averTemp) + ' ' + li[3].string
            AllMonthDetail.append(oneMonthDetail)

    return AllMonthDetail
    # print li[0]
    # print str(li[0]).replace('<li>','').replace('</li>','')
    # print str(li[3]).replace('<li>','').replace('</li>','')

# def loadDateString(dateString):
#     weekDate = [r"Monday", r"Tuesday", r"Wednesday", r"Thursday", r"Friday", r"Saturday", r"Sunday"]
#     dateSplit = dateString.split('-')
#     # print dateSplit
#     toDate = datetime.datetime(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))
#     weekDateDetail = (weekDate[int(toDate.weekday())])
#     return weekDateDetail

#
# def writeWeatherIntoFile(OneMonthDetail):
#     outFile = open('weatherWithDate.txt', 'w+')
#     outFile.write(OneMonthDetail)
#     outFile.close()


if __name__ == '__main__':
    weatherList = []
    sheetNumber = 0
    WeatherYearsDetailAll = []
    for year in range(2011, 2014, 1):
        # WeatherDetailAll = []
        for month in range(01, 13, 1):
            if month < 10:
                strMonth = str(r'0' + str(month))
            else:
                strMonth = str(month)

            weatherList.append(str(year) + strMonth)
    #     weatherList = weatherList[:-2]
        if year == 2013:
            weatherList = weatherList[:-2]
    # # print weatherList
        WeatherDetailAll = []

        for yearMonth in weatherList:
            oneMonth = loadWeatherDetail(loadHistoryWeatherHTML(yearMonth))
            for oneDate in oneMonth:
                WeatherDetailAll.append(oneDate)
            # writeWeatherIntoFile(WeatherDetailAll.encode("gbk"))
        WeatherYearsDetailAll.append(WeatherDetailAll)
        weatherList = []
    # for datedsgf in  WeatherYearsDetailAll:
    #     print datedsgf
    writeExcelFile("weatherWithDate.xls", WeatherYearsDetailAll)
        # weatherList = []
        # WeatherDetailAll = []
