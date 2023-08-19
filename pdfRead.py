#D:/Vstudio/Vscode/PDFconv

# importing required modules
import PyPDF2
import re

# creating a pdf file object
text_file = open("D:/Vstudio/Vscode/PDFconv/data.txt", "w")

parts = []
# creating a pdf file object
pdfFileObj = open('D:/Vstudio/Vscode/PDFconv/praticaATP-IRaereo.pdf', 'rb')
  
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

def deletewhite(parts,index):
    parts.pop(index)
    if parts[index]=='':
        deletewhite(parts,index)

count = [0,[]]

def deletewhitefor(parts):
    for i in range(len(parts)-1):
        if parts[i]=='':
            count[0]+=1
        if count[0]==1:
            count[1].append(i)
        if count[0]==4:
            count[0]=0
            deletewhite(parts,count[1][-1])
            deletewhitefor(parts)
            break

deletewhitefor(parts)

#ask for user input
for i in count[1]:
    print("insert the text missing between these two phrases: \n",parts[i-1],"\n",parts[i+1])
    parts[i]=input("insert the text: ")


text_body = "".join(parts)
# extracting text from page
print(text_body)
text_file.write(text_body)
# closing the pdf file object
pdfFileObj.close()
text_file.close()