import re
import subprocess
import pickle
import os

def parse_file(phrases,hier,pattern,hierlayer=0):           #give a hierarchy value to each line and merge the lines that are divided by page boundaries
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
            
        return hier

def transform_list(input_list):                             #transform the list into a list of strings with the correct spacing (for visual purposes)
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

def hierarchy_creator(filename,rootdir,popopen=False,deleteunused=True):      #main function
    
    #open the file
    text_file = open(f"{rootdir}{filename}_output.txt", "w")
    file = open(f"{rootdir}{filename}.txt", "r")
    hier=[]

    #regex patterns for the different hierarchy levels in order (0 max, 3min)
    pattern = [r"^.{0,7}\((a|b|c|d|e|f|g|h|j|k|l|m|n|o|p|q|r|s+)\)",r"^.{0,7}\((1|2|3|4|5|6|7|8|9|10+)\)",r"^.{0,7}\((i|ii|iii|iv|v|vi|vii|viii|ix|x+)\)",r"^.{0,7}\((A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S+)\)"]

    phrases=[]

    #read the file and put each line in a list deleting the newlines
    for line in file:
        if line=='\n':
            continue
        else:
            phrases.append(line.replace("\n", ""))

    hier=parse_file(phrases,hier,pattern)

    pickle.dump(hier,open(f"{rootdir}{filename}_hier.pkl","wb"))

    text=""
    for i in transform_list(hier):
        print(i,end="")
        text+=i
    text_file.write(text)
    file.close()
    text_file.close()
    if popopen: subprocess.Popen(['notepad.exe', f"{rootdir}{filename}_output.txt"])
    
    if deleteunused:
        #delete the unused files
        os.remove(f"{rootdir}{filename}.txt")