# coding:utf-8
import datetime
import xlrd
import xlwt

__author__ = 'ZrongH'


def loadWeatherDetailFile(filename):
    fd = open(filename, 'r')
    # weekDate = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    newFileString = []
    fd.readline()
    for line in fd:
        # print line.decode("gbk")
        line = line.decode("gbk")
        line = line[:-2]
        # # print line
        # splitLine = line.split(" ")
        # dateSplit = splitLine[0].split('-')
        # toDate = datetime.datetime(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))
        # # print line.decode("gbk"), weekDate[int(toDate.weekday())]
        # newline = line+str(weekDate[int(toDate.weekday())])+"\r\n"
        # newFileString += newline
        newFileString.append(line)
    fd.close()
    # print newFileString
    return newFileString


def writeExcelFile(filename, newFileStringList):
    # fd = open(filename,"w+")
    # data = xlrd.open_workbook(filename)
    # print newFileStringList
    # table = data.sheets()[sheetNumber]
    sheetNumber = 0
    wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
    for yearStringList in newFileStringList:
        rowIndex = 0
        sheetName = r"sheet" + str(sheetNumber)

        sheet = wbk.add_sheet(sheetName, cell_overwrite_ok=False)  ##第二参数用于确认同一个cell单元是否可以重设值。
        print sheetNumber,'-------------------------------------------'
        for oneInstance in yearStringList:
            # print oneInstance
            stringSplit = oneInstance.split(' ')

            sheet.write(rowIndex, 0, stringSplit[0])
            sheet.write(rowIndex, 1, stringSplit[1])
            sheet.write(rowIndex, 2, stringSplit[2])
            rowIndex += 1
            # print rowIndex

            # style = xlwt.XFStyle()
            # font = xlwt.Font()
            # font.name = 'Times New Roman'
            # font.bold = True
            # style.font = font
            # sheet.write(0, 1, 'some bold Times text', style)
        sheetNumber += 1
    wbk.save(filename)    ##该文件名必须存在

    # fd.write(newFileString)
    # fd.close()


if __name__ == "__main__":
    filename = "weatherWithDate.txt"
    newString = loadWeatherDetailFile(filename)
    writeExcelFile("weatherWithDate.xls", newString)
    # writeFile(filename,newString)
