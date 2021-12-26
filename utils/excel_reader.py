import os
from xlrd import open_workbook

path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class readExcel():
    def get_xls(self, xls_name, sheet_name):
        cls = []
        xls_path = os.path.join(path, "casedata", xls_name)
        file = open_workbook(xls_path)
        sheet = file.sheet_by_name(sheet_name)

        rows = sheet.nrows
        for i in range(rows):
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))

        return cls

