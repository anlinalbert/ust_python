import win32com.client


def create_presentation(file_path):
    # Launch PowerPoint application
    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    powerpoint.Visible = True

    # Create a new presentation
    presentation = powerpoint.Presentations.Add()

    # Add a slide
    slide = presentation.Slides.Add(1, 1)
    slide.Shapes[0].TextFrame.TextRange.Text = "Automating PowerPoint"
    slide.Shapes[1].TextFrame.TextRange.Text = "Using PyWin32 for Automation"

    # Save presentation
    presentation.SaveAs(file_path)
    powerpoint.Quit()


create_presentation(r"C:\Users\Administrator\Desktop\UST Training\Practice_Programs\day20\sample.ppt")
