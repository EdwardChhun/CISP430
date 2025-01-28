from fpdf import FPDF

# save FPDF() class into a variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# Set style and size of font 
# Adjust font size to shrink the text
pdf.set_font("Arial", size=12)

# Set the width for text wrapping
line_width = 180  # Adjust width to control wrapping (units are in mm)

# Open the text file in read mode with utf-8 encoding
with open("week2/lab.txt", "r", encoding="utf-8") as f:
    for x in f:
        # Encode text to 'latin1', replacing unsupported characters
        sanitized_text = x.encode("latin1", errors="replace").decode("latin1")
        # Use multi_cell to wrap text within the page width
        pdf.multi_cell(line_width, 10, txt=sanitized_text.strip(), align='L')

# Save the PDF with a specified name
pdf.output('lab.pdf')
