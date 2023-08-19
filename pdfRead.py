#D:/Vstudio/Vscode/PDFconv

# importing required modules
import PyPDF2
import re
import hierarchynator as hier
import subprocess
import enchant
import string

def spellchk(text):
    # Create a dictionary object for spell checking
    
    dictionary = enchant.Dict("en_UK")
    
    patterns = [r'[A-Z0-9]{2,}',r'\(|\)']

    punctuation=r"""!"#$%&'*+,./:;<=>?@[\]^_`{|}~"""

    # Common exceptions to the spell checker
    exceptions=["aeroplane", "pre-flight", "minima", "manoeuvres", "authorised", "maths", "licence"]
    
    # Split the input text
    words = text.split()

    # Check each word for spelling errors
    for word in words:

        # Remove punctuation
        if any(char in punctuation for char in word):
            # Remove punctuation using regex
            word = re.sub(r'[{}]'.format(re.escape(punctuation)), '', word)

        # Check if the word is an acronym or a number or in parenthesis
        if not re.findall(patterns[0], word) and not re.findall(patterns[1], word) and word!='°' and word!='':
            # Check if the word is in the dictionary
            if not dictionary.check(word) and (word not in exceptions):
                if len(dictionary.suggest(word))!=0:
                    # Ask the user if the word is correct or not
                    inpt=input(f"the word \u001b[31m{word}\u001b[0m is not in the dictionary, y: accept \u001b[31m{dictionary.suggest(word)[0]}\u001b[0m n: reject, anything else: replace with : ")
                    if inpt=='y':
                        text=text.replace(word,dictionary.suggest(word)[0])
                    elif inpt=='n' or inpt=='':
                        pass
                    else:
                        text=text.replace(word,inpt)
                else:   #if the word is not in the dictionary and there are no suggestions
                    inpt=input(f"the word \u001b[31m{word}\u001b[0m is not in the dictionary, n: reject, anything else: replace with : ")
                    if inpt=='n':
                        pass
                    else:
                        text=text.replace(word,inpt)


    return text

parts = []

spellcheck = True

#root directory
rootdir = 'D:/Vstudio/Vscode/PDFconv/2/'

#filename
filename="praticaATP-IRaereo"

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

def find_string_in_file(filename,rootdir, search_string):
    line_numbers = []
    for search in search_string:
        with open(f'{rootdir}{filename}.txt', 'r') as file:
            for line_num, line in enumerate(file, start=1):
                if search in line:
                    line_numbers.append(line_num)
                    break
    return line_numbers

#close the files

errors=[]
if spellcheck:
    text_body=spellchk(text_body)
text_file.write(text_body)
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