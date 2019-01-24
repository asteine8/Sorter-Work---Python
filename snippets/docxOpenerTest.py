import docx2txt
import re

# document = Document("Results list for_ UCLA-DOCX.DOCX")

text = docx2txt.process("Results list for_ UCLA-DOCX.DOCX")

print(text)
# for p in document.paragraphs:    
#     # Remove some annoying things
#     pText = p.text
#     pText = pText.replace("...", "")
#     pText = re.sub("\s+"," ",pText)

#     text.append(pText)


# for i in range(20):
#     print(str(i) + ":  " + text[i])