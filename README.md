# PDFconv

## Environment creator
```
conda create --name PDFconv 
conda activate PDFconv
pip install PyPDF2 enchant
```
## Usage
  - The pdfRead.py file contains 2 variables that must be changed for every file:
    ``` 
    rootdir = #the directory of the file
    filedir = #the name of the file
    spellcheck = #enables the spellchecker
    ```
  - Once ran, the program it will prompt you to input any missig text that isn't encoded as text
    
    <img src=Images/example.png width="70%" alt="non-text example"/>

    and then it will also prompt you to check the file and delete the unwanted parts before passing it into the function to determine the hierarchy.

  - To edit the hierarchy, the regex code in the hierarchy_creator function must be changed.

    ```
    
        pattern = [r"^.{0,7}\((a|b|c|d|e|f|g|h|j|k|l|m|n|o|p|q|r|s+)\)",r"^.{0,7}\((1|2|3|4|5|6|7|8|9|10+)\)",r"^.{0,7}\((i|ii|iii|iv|v|vi|vii|viii|ix|x+)\)",r"^.{0,7}\((A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S+)\)"]


        output:
        (a) Detailed listing for aeroplane structure and equipment, normal operation of systems and malfunctions: 
	        (1)dimensions: minimum required runway width for 180 � turn. 
	        (2) engine including auxiliary power unit: 
		        (i) type of engine or engines; 
		        (ii) in general, function of the following systems or components:
			        (A) engine; 
			        (B) auxiliary power unit; 
			        (C) oil system; 
    ``` 
