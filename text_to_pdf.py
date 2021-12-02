from fpdf import FPDF
import textwrap


def text_to_pdf(text, filename):
    a3_width_mm = 297
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a3_width_mm / character_width_mm       # can just use width_text = 120 if you are mainly on A3

    pdf = FPDF(orientation='P', unit='mm', format='A3')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = text.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output(filename, 'F')
    
"""
if you dont want to wrap use:
    for line in splitted:
        line = line[:120]
        if len(line) == 0:
            pdf.ln()
        else:
            pdf.cell(0, fontsize_mm, line, ln=1)
            
instead of the stated loop
"""
