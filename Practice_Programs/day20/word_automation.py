import win32com.client


def create_word(file_path):
    """Function to create word."""
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = True

    doc = word.Documents.Add()

    selection = word.Selection
    selection.TypeText("Hey")
    selection.TypeParagraph()
    selection.TypeText("there")

    doc.SaveAs(file_path)

    word.Quit()


create_word(r"C:\Users\Administrator\Desktop\UST Training\Practice_Programs\day20\sample.docx")
