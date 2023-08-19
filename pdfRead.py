#D:/Vstudio/Vscode/converter

# importing required modules
import PyPDF2
import re

# creating a pdf file object
text_file = open("D:/Vstudio/Vscode/converter/data.txt", "w")

parts = []
# creating a pdf file object
pdfFileObj = open('D:/Vstudio/Vscode/converter/praticaATP-IRaereo.pdf', 'rb')
  
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj, strict=True)
  
# printing number of pages in pdf file
file_len=len(pdfReader.pages)

#eliminate header and footer
def visitor_body(text, cm, tm, font_dict, font_size):
    y = tm[5]
    if y > 84 and y < 1050:
        parts.append(text)


for pageObj in pdfReader.pages:
    pageObj.extract_text(visitor_text=visitor_body)
    parts.append("\n")


text_body = "".join(parts)
# extracting text from page
print(text_body)
text_file.write(text_body)
# closing the pdf file object
pdfFileObj.close()
text_file.close()