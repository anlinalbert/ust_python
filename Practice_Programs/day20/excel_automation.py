import win32com.client


def create_workbook(file_path):
    """Function to create workbook."""
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True

    workbook = excel.Workbooks.Add()

    sheet = workbook.Sheets(1)
    sheet.Cells(1, 1).Value = "Hey"
    sheet.Cells(2, 1).Value = "there"

    workbook.SaveAs(file_path)

    excel.Quit()


create_workbook(r"C:\Users\Administrator\Desktop\UST Training\Practice_Programs\day20\sample.xlsx")
