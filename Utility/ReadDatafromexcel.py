import xlrd

import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

def read_data_excel(row,col):
    wb=xlrd.open_workbook(os.path.join(ROOT_DIR,'Data/testData.xlsx'))
    sheet=wb.sheet_by_index(0)
    return sheet.cell_value(row,col)