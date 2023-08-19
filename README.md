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
  
    and then it will also prompt you to check the file and delete the unwanted parts before passing it into the function to determine the hierarchy.
