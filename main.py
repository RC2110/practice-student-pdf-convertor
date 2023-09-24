import pathlib

import pandas as pd
from fpdf  import FPDF

import glob

files = glob.glob("textfiles/*.txt")

print(files)
pdf= FPDF(orientation="P", unit="mm", format="A4")
# pdf.set_auto_page_break(auto=False)
pdf.set_text_color(100,100,100)

for filepaths in files:

    data = pd.read_csv(filepaths)
    pdf.add_page()
    fp = pathlib.Path(filepaths)
    afp=fp.stem
    pdf.set_font(family="Times", style="B", size=15)
    pdf.cell(w=25, h=8, txt=f"{afp.title()}", ln=1, align='L')

    with open(filepaths, 'r') as file:
        content = file.read()
        pdf.set_font(family="Times", style="I", size=12)
        pdf.multi_cell(w=0,h=6,txt=content)

pdf.output("animals.pdf")


