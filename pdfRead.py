#D:/Vstudio/Vscode/PDFconv

# importing required modules
import PyPDF2
import re
import hierarchynator as hier
import subprocess

parts = []

#root directory
rootdir = 'D:/Vstudio/Vscode/PDFconv/3/'

#filename
filename="praticaATPelicottero"

# creating a pdf file object
pdfFileObj = open(f'{rootdir}{filename}.pdf', 'rb')
text_file = open(f"{rootdir}{filename}.txt", 'w')

# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj, strict=False)

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
temp=0


def deletewhitefor(parts):
    for i in range(len(parts)-1):
        if parts[i]=='':
            count[0]+=1
        if count[0]==1:
            temp=i
        if count[0]==4:
            count[0]=0
            count[1].append(temp)
            deletewhite(parts,count[1][-1])
            deletewhitefor(parts)
            break

#find non-text text and report it
deletewhitefor(parts)

search_string=[]

#ask for user input for the non-text
for i in count[1]:
    if parts[i-1]=="\n":
        i-=1
    print("insert the text missing between these two phrases: \n",parts[i-1],"\n",parts[i+1])
    search_string.append(" "+str(input("insert the text: "))+" ")
    parts[i]=search_string[-1]

text_body = "".join(parts)

#writing the text to a file
text_file.write(text_body)

def find_string_in_file(filename,rootdir, search_string):
    line_numbers = []
    with open(f'{rootdir}{filename}.txt', 'r') as file:
        for search in search_string:
            for line_num, line in enumerate(file, start=1):
                if search in line:
                    line_numbers.append(line_num)
    return line_numbers

#close the files
text_file.close()
pdfFileObj.close()

#open the file with notepad and ask for user input before continuing
subprocess.Popen(['notepad.exe', f"{rootdir}{filename}.txt"])
input(u"Please check the \u001b[31m{}.txt\u001b[0m file for any errors and make sure that the file starts at the right point\ncheck also at line \u001b[31m{}\u001b[0m if the text that you have put in is correctly spaced, then press any key to continue".format(filename,str(find_string_in_file(filename,rootdir,search_string))))

try:
    hier.hierarchy_creator(filename,rootdir,popopen=True)
except IndexError:
    subprocess.Popen(['notepad.exe', f"{rootdir}{filename}.txt"])
    input("please check that the file starts with a hierarchy point ex. (a) or (1) or (i) or (A), then press any key to continue")
    hier.hierarchy_creator(filename,rootdir,popopen=True)