import docx2txt
import re

# document = Document("Results list for_ UCLA-DOCX.DOCX")

lines = docx2txt.process("Results list for_ UCLA-DOCX.DOCX").split("\n")

for l in range(len(lines)):    
    # Remove some annoying things
    lines[l] = lines[l].replace("...", "") # Kill ellipses 
    lines[l] = re.sub("\s+"," ",lines[l]) # Remove duplicate spaces
    if (re.match("\s+", lines[l][0:1])): # Check for whitespace at beginning of string
        lines[l] = lines[l][1:] # Return the string minus the first character (which is whitespace)

for i in range(100):
    print(str(i) + ": " + lines[i])