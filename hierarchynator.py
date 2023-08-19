file_path="D:/Vstudio/Vscode/PDFconv/praticaATP-IRaereo.txt"

file=open(file_path,'r')

hier=[]

phrases=[]

for line in file:
    if line=='\n':
        continue
    else:
        phrases.append(line)

def parse_file(phrases,hier):
    for line in phrases:
        if line.startswith('('):
            hier.append([line])
            parse_file(phrases[phrases.index(line)+1:],hier[-1])
        else:
            hier.append(line)
    return hier

#TODO:must add check for hierarchy

parse_file(phrases,hier)

print(hier)