import xlrd


def main():
    dir = 'full file path if not in dir'
    xcel_file = xlrd.open_workbook(dir + 'file')
    sheet = xcel_file.sheet_by_name("Contact")
    row = 0

    for row in range(sheet.nrows):
        print(sheet.row_values(row)[1..-1])
        row += 1


if __name__ == '__main__':
    main()
