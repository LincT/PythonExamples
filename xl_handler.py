import xlrd
import os


def main():
    book = os.environ['LIBRARY_PATH'] + '\\Google Drive\\Work\\Resume Versions\\'
    excel_file = xlrd.open_workbook(book + 'Resume Source Data.xlsm')
    sheet = excel_file.sheet_by_name("Contact")

    for row in range(sheet.nrows):
        print(sheet.row_values(row)[:-1])
        row += 1


if __name__ == '__main__':
    main()
