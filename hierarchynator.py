import re


filename="teoriaclassetypeaereo"

file_path=f"D:/Vstudio/Vscode/PDFconv/{filename}.txt"

file=open(file_path,'r')
text_file = open(f"D:/Vstudio/Vscode/PDFconv/{filename}_output.txt", "w")
hier=[]

pattern = [r"^.{0,7}\((a|b|c|d|e|f|g|h|j|k|l|m|n|o|p|q|r|s+)\)",r"^.{0,7}\((1|2|3|4|5|6|7|8|9|10+)\)",r"^.{0,7}\((i|ii|iii|iv|v|vi|vii|viii|ix|x+)\)",r"^.{0,7}\((A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S+)\)"]

phrases=[]

for line in file:
    if line=='\n':
        continue
    else:
        phrases.append(line.replace("\n", ""))

def parse_file(phrases,hier,hierlayer=0):
    for line in phrases:
        for p in range(len(pattern)):
            found=False
            if re.match(pattern[p],line):
                hier.append([p,line])
                found=True
                hierlayer=p
                break
        if not found:
            hier[-1][-1]+=(line)
            #hier.append([hierlayer,line])
        
    return hier

def transform_list(input_list):
    output_list=[]
    for i in range(len(input_list)):
        if input_list[i][0]==0:
            output_list.append(input_list[i][1]+"\n")
        elif input_list[i][0]==1:
            output_list.append("\t"+input_list[i][1]+"\n")
        elif input_list[i][0]==2:
            output_list.append("\t\t"+input_list[i][1]+"\n")
        elif input_list[i][0]==3:
            output_list.append("\t\t\t"+input_list[i][1]+"\n")
    return output_list

#TODO:must add check for hierarchy

hier=parse_file(phrases,hier)

print(hier)
text=""
for i in transform_list(hier):
    print(i,end="")
    text+=i
text_file.write(text)